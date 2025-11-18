"""
PDF worksheet generator with LaTeX equation rendering.
Creates printable worksheets and answer keys.

FONT SIZE STANDARDS:
- Problem numbers: 12pt Lexend
- Equations: 21pt Lexend (1.75x ratio to problem numbers)
- This ratio should be maintained across ALL worksheet types
"""

import os
import io
from typing import List
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import mathtext
import matplotlib.font_manager as fm
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from equation_generator import Equation
from systems_generator import SystemProblem
from inequalities_generator import InequalityProblem
from properties_generator import PropertyProblem
from word_problems_generator import WordProblem
from multistep_generator import MultiStepEquation
from generators.chapter04.graphing_points import GraphingPointsProblem
from generators.chapter05.graphing_systems import GraphingSystemProblem
from generators.chapter11.graphing_parabolas import ParabolaGraphingProblem
from worksheet_config import get_config, ProblemTypeConfig
from typing import Union


class PDFWorksheetGenerator:
    """Generates PDF worksheets with LaTeX-rendered equations."""

    # Font size standards (maintain 1.75x ratio)
    PROBLEM_NUMBER_FONT_SIZE = 12  # Lexend 12pt for problem numbers
    EQUATION_FONT_SIZE = 21  # Lexend 21pt for equations (1.75x ratio)

    # Page layout constants
    BLEED_EDGE = 0.125 * inch  # Standard print bleed
    TOP_MARGIN = 0.5 * inch
    BOTTOM_MARGIN = 0.5 * inch
    BOTTOM_PADDING = 1.0 * inch  # Static padding to keep problems from extending too low

    # Spacing constraints per problem type (min, max)
    MIN_SPACING = {
        'linear_equation': 0.6 * inch,
        'system_of_equations': 1.0 * inch,
        'inequality': 1.5 * inch,
        'graphing_points': 3.8 * inch,  # Minimum spacing for 3" graphs + text
        'graphing_systems': 3.8 * inch,  # Same as graphing_points
        'graphing_parabolas': 3.8 * inch  # Same as other graphing types
    }

    MAX_SPACING = {
        'linear_equation': 2.5 * inch,
        'system_of_equations': 2.0 * inch,
        'inequality': 2.5 * inch,
        'graphing_points': 4.5 * inch,  # Maximum spacing for graphing problems
        'graphing_systems': 4.5 * inch,  # Same as graphing_points
        'graphing_parabolas': 4.5 * inch  # Same as other graphing types
    }

    def __init__(self):
        """Initialize the PDF generator."""
        # Register custom fonts for ReportLab
        self._register_fonts()

        # Configure matplotlib to use Lexend for all text (including equations)
        try:
            lexend_path = os.path.join(os.path.dirname(__file__), '..', 'Lexend', 'static', 'Lexend-Regular.ttf')
            if os.path.exists(lexend_path):
                fm.fontManager.addfont(lexend_path)
                plt.rcParams['font.family'] = 'Lexend'
                plt.rcParams['font.size'] = 14
                # Use Lexend for math text as well (not LaTeX rendering)
                plt.rcParams['mathtext.fontset'] = 'custom'
                plt.rcParams['mathtext.rm'] = 'Lexend'
                plt.rcParams['mathtext.it'] = 'Lexend:italic'
                plt.rcParams['mathtext.bf'] = 'Lexend:bold'
            else:
                # Fallback to STIX Sans if Lexend not found
                plt.rcParams['mathtext.fontset'] = 'stixsans'
                plt.rcParams['font.size'] = 14
        except Exception as e:
            print(f"Note: Could not configure Lexend for matplotlib: {e}")
            # Fallback to STIX Sans
            plt.rcParams['mathtext.fontset'] = 'stixsans'
            plt.rcParams['font.size'] = 14

    def _register_fonts(self):
        """Register custom fonts with ReportLab."""
        try:
            # Get the parent directory (whymath folder)
            base_dir = os.path.dirname(os.path.dirname(__file__))

            # Register Lexend fonts
            lexend_regular = os.path.join(base_dir, 'Lexend', 'static', 'Lexend-Regular.ttf')
            lexend_bold = os.path.join(base_dir, 'Lexend', 'static', 'Lexend-Bold.ttf')

            if os.path.exists(lexend_regular):
                pdfmetrics.registerFont(TTFont('Lexend', lexend_regular))
            if os.path.exists(lexend_bold):
                pdfmetrics.registerFont(TTFont('Lexend-Bold', lexend_bold))

            # Try to register Poppins fonts (for title, name, date)
            poppins_dir = os.path.join(base_dir, 'Poppins')
            poppins_regular = os.path.join(poppins_dir, 'Poppins-Regular.ttf')
            poppins_bold = os.path.join(poppins_dir, 'Poppins-Bold.ttf')

            if os.path.exists(poppins_regular):
                pdfmetrics.registerFont(TTFont('Poppins', poppins_regular))
            if os.path.exists(poppins_bold):
                pdfmetrics.registerFont(TTFont('Poppins-Bold', poppins_bold))

        except Exception as e:
            print(f"Warning: Could not register custom fonts: {e}")
            print("Falling back to default fonts")

    def _wrap_text(self, c: canvas.Canvas, text: str, x: float, y: float, max_width: float, line_height: float = 0.15) -> float:
        """
        Wrap text to fit within max_width and draw it.

        Args:
            c: Canvas object
            text: Text to wrap
            x: X position to start drawing
            y: Y position to start drawing (top of first line)
            max_width: Maximum width in inches
            line_height: Line height in inches

        Returns:
            Y position after last line of text (for positioning next element)
        """
        words = text.split(' ')
        lines = []
        current_line = []

        for word in words:
            # Try adding word to current line
            test_line = ' '.join(current_line + [word])
            # Get text width in points (convert max_width from inches to points)
            text_width = c.stringWidth(test_line, c._fontname, c._fontsize)

            if text_width <= max_width * 72:  # Convert inches to points (1 inch = 72 points)
                current_line.append(word)
            else:
                # Line is too long, save current line and start new one
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    # Single word is too long, add it anyway
                    lines.append(word)

        # Add remaining words
        if current_line:
            lines.append(' '.join(current_line))

        # Draw all lines
        current_y = y
        for line in lines:
            c.drawString(x, current_y, line)
            current_y -= line_height * inch

        return current_y

    def _calculate_dynamic_spacing(self, problem_type: str, num_problems: int,
                                   start_y: float, end_y: float) -> float:
        """
        Calculate optimal vertical spacing for problems in a column.

        Args:
            problem_type: Type of problem (linear_equation, system_of_equations, inequality)
            num_problems: Number of problems in this column
            start_y: Starting y position (top of column)
            end_y: Ending y position (bottom limit, accounting for footer + bleed + padding)

        Returns:
            Optimal spacing in inches
        """
        # Calculate available space
        # We need to account for the space that the last problem takes up
        # For inequalities, add extra space for the number line
        if problem_type == 'inequality':
            problem_height = 0.8 * inch  # Approximate height for inequality with number line
        elif problem_type == 'system_of_equations':
            problem_height = 0.4 * inch  # Approximate height for two-line system
        elif problem_type == 'graphing_points':
            problem_height = 3.8 * inch  # Height for coordinate plane (3.0" image + 0.15" offset + ~0.65" for wrapped text)
        else:
            problem_height = 0.2 * inch  # Approximate height for single equation

        available_space = start_y - end_y - problem_height

        # Calculate ideal spacing to fill the space
        if num_problems > 1:
            ideal_spacing = available_space / (num_problems - 1)
        else:
            ideal_spacing = available_space

        # Apply constraints
        min_spacing = self.MIN_SPACING.get(problem_type, 0.6 * inch)
        max_spacing = self.MAX_SPACING.get(problem_type, 1.5 * inch)

        optimal_spacing = max(min_spacing, min(ideal_spacing, max_spacing))

        return optimal_spacing

    def render_latex_to_image(self, latex_str: str, fontsize: int = 16) -> ImageReader:
        """
        Render a LaTeX string to an image using matplotlib.

        Args:
            latex_str: LaTeX equation string
            fontsize: Font size for rendering

        Returns:
            ImageReader object for reportlab
        """
        # Create figure with no axes
        fig = plt.figure(figsize=(4, 0.5))
        fig.patch.set_visible(False)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')

        # Render LaTeX text (x=0 for left alignment, no padding)
        ax.text(0, 0.5, f'${latex_str}$', fontsize=fontsize, verticalalignment='center', horizontalalignment='left')

        # Save to bytes buffer with tight bbox and minimal padding
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.005,
                    transparent=False, facecolor='white')
        buf.seek(0)
        plt.close(fig)

        return ImageReader(buf)

    def render_system_to_image(self, eq1: str, eq2: str, fontsize: int = 16) -> ImageReader:
        """
        Render a system of equations as two lines without a brace.

        Args:
            eq1: First equation in LaTeX
            eq2: Second equation in LaTeX
            fontsize: Font size for rendering

        Returns:
            ImageReader object for reportlab
        """
        # Create figure for system (taller to fit two equations)
        fig = plt.figure(figsize=(4, 1.0))
        fig.patch.set_visible(False)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')

        # Render both equations
        ax.text(0.05, 0.70, f'${eq1}$', fontsize=fontsize, verticalalignment='center')
        ax.text(0.05, 0.30, f'${eq2}$', fontsize=fontsize, verticalalignment='center')

        # Save to bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.1,
                    transparent=False, facecolor='white')
        buf.seek(0)
        plt.close(fig)

        return ImageReader(buf)

    def generate_worksheet(self, equations: List[Union[Equation, SystemProblem, InequalityProblem, PropertyProblem, WordProblem, MultiStepEquation, GraphingPointsProblem, GraphingSystemProblem]], output_path: str,
                          title: str = "Math Worksheet",
                          include_answer_key: bool = True):
        """
        Generate a PDF worksheet with equations or systems.

        Args:
            equations: List of Equation or SystemProblem objects
            output_path: Path to save the PDF
            title: Worksheet title
            include_answer_key: Whether to include answer key on separate page
        """
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter

        # Draw worksheet page
        self._draw_worksheet_page(c, equations, title, width, height)

        if include_answer_key:
            c.showPage()  # Start new page
            self._draw_answer_key_page(c, equations, title, width, height)

        c.save()
        print(f"Worksheet saved to: {output_path}")

    def _draw_worksheet_page(self, c: canvas.Canvas, equations: List[Union[Equation, SystemProblem, InequalityProblem, PropertyProblem, WordProblem, MultiStepEquation]],
                            title: str, width: float, height: float):
        """Draw the main worksheet page with problems."""
        # Header with logo in top right
        y_pos = height - 0.5 * inch

        # Draw QR code in top left corner
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            qr_path = os.path.join(base_dir, 'src', 'icons', 'freshmath_qr.png')

            if os.path.exists(qr_path):
                qr_size = 0.55 * inch  # QR code size (0.55 x 0.55 inches)
                # Position 0.25 inches from top and left edges
                qr_x = 0.25 * inch
                qr_y = height - 0.25 * inch - qr_size  # 0.25" from top

                c.drawImage(qr_path, qr_x, qr_y, width=qr_size, height=qr_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            pass  # Silently skip if QR code not available

        # Draw logo in top right (0.75 inches)
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            logo_path = os.path.join(base_dir, 'src', 'icons', 'FreshMath_V3',
                                     'Black', 'FreshMath_Black_Secondary.png')

            if os.path.exists(logo_path):
                logo_size = 0.75 * inch  # 0.75 x 0.75 inches
                # Position in top right corner with margin
                logo_x = width - logo_size - 0.25 * inch
                logo_y = y_pos - logo_size + 0.3 * inch  # Adjust vertical alignment

                c.drawImage(logo_path, logo_x, logo_y, width=logo_size, height=logo_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"Warning: Could not load logo: {e}")

        # Header fields - use Poppins if available, else Lexend
        try:
            c.setFont("Poppins", 12)
        except:
            c.setFont("Lexend", 12)

        # Name on left (positioned after QR code)
        c.drawString(1 * inch, y_pos, "Name: _________________________")

        # Date to the left of logo (in top right area)
        date_x = width - 0.75 * inch - 0.7 * inch  # Position left of logo with some spacing
        c.drawRightString(date_x, y_pos, "Date: _____________")

        # Title below header - use Poppins-Bold if available
        try:
            c.setFont("Poppins-Bold", 18)
        except:
            try:
                c.setFont("Lexend-Bold", 18)
            except:
                c.setFont("Helvetica-Bold", 18)
        y_pos -= 0.5 * inch
        c.drawCentredString(width / 2, y_pos, title)

        # Detect problem type and get configuration
        if equations and isinstance(equations[0], SystemProblem):
            problem_type = 'system_of_equations'
            is_system = True
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
        elif equations and isinstance(equations[0], InequalityProblem):
            problem_type = 'inequality'
            is_system = False
            is_inequality = True
            is_property = False
            is_word_problem = False
            is_multistep = False
        elif equations and isinstance(equations[0], PropertyProblem):
            # Detect which type of properties: add/subtract or mult/div
            if equations[0].property_type in ['multiplication', 'division']:
                problem_type = 'properties_mult_div'
            else:
                problem_type = 'properties_of_equality'
            is_system = False
            is_inequality = False
            is_property = True
            is_word_problem = False
            is_multistep = False
        elif equations and isinstance(equations[0], WordProblem):
            problem_type = 'word_problems'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = True
            is_multistep = False
        elif equations and isinstance(equations[0], MultiStepEquation):
            problem_type = 'multistep_equations'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = True
            is_graphing = False
        elif equations and isinstance(equations[0], GraphingPointsProblem):
            problem_type = 'graphing_points'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
        elif equations and isinstance(equations[0], GraphingSystemProblem):
            problem_type = 'graphing_systems'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
        elif equations and isinstance(equations[0], ParabolaGraphingProblem):
            problem_type = 'graphing_parabolas'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
        else:
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False

        config = get_config(problem_type)

        # Add instructional text for properties and word problems worksheets
        if is_property:
            y_pos -= 0.35 * inch
            try:
                c.setFont("Lexend", 12)
            except:
                c.setFont("Helvetica", 12)
            if problem_type == 'properties_mult_div':
                instructions_text = "Identify the property of equality (Multiplication or Division) used to solve each equation. Show your work."
            else:
                instructions_text = "Identify the property of equality (Addition or Subtraction) used to solve each equation. Show your work."
            c.drawCentredString(width / 2, y_pos, instructions_text)
        elif is_word_problem:
            y_pos -= 0.35 * inch
            try:
                c.setFont("Lexend", 12)
            except:
                c.setFont("Helvetica", 12)
            instructions_text = "Read each word problem carefully. Write an equation and solve for x. Show your work."
            c.drawCentredString(width / 2, y_pos, instructions_text)
        elif is_multistep:
            y_pos -= 0.35 * inch
            try:
                c.setFont("Lexend", 12)
            except:
                c.setFont("Helvetica", 12)
            instructions_text = "Solve each two-step equation. Show your work."
            c.drawCentredString(width / 2, y_pos, instructions_text)

        # Draw problems - use Lexend
        y_pos -= 0.5 * inch
        try:
            c.setFont("Lexend", 12)
        except:
            c.setFont("Helvetica", 12)

        # Calculate usable vertical space with bleed edge and static padding
        header_end = y_pos  # Current position after instructions
        footer_start = self.BOTTOM_MARGIN + self.BLEED_EDGE + self.BOTTOM_PADDING  # 0.625" + 1.0" = 1.625"
        usable_space = header_end - footer_start

        # Use configuration for layout
        problems_per_page = min(len(equations), config.problems_per_page)

        # Determine problems per column based on problem type
        if is_inequality or is_system:
            problems_per_column = 4  # 2 columns × 4 rows
        elif is_graphing:
            problems_per_column = 2  # 2 columns × 2 rows
        else:  # linear equations
            problems_per_column = 5  # First two columns have 5 problems

        # Calculate dynamic spacing for first column
        actual_problems_first_column = min(problems_per_page, problems_per_column)
        spacing = self._calculate_dynamic_spacing(
            problem_type,
            actual_problems_first_column,
            header_end,
            footer_start
        )

        x_start = 1 * inch
        y_start = y_pos

        for idx, equation in enumerate(equations[:problems_per_page]):
            # Layout for different problem types
            if is_inequality:
                # Inequalities: 2 columns x 4 rows
                if idx > 0 and idx % 4 == 0:
                    # Move to second column after 4 problems
                    # Recalculate spacing for remaining problems
                    remaining_problems = min(problems_per_page - idx, 4)
                    spacing = self._calculate_dynamic_spacing(
                        problem_type,
                        remaining_problems,
                        y_start,
                        footer_start
                    )
                    x_start = 4.25 * inch
                    y_pos = y_start
            elif is_system:
                # Systems: single column or 2 columns depending on space
                if idx > 0 and idx % 4 == 0 and idx < 8:
                    # Recalculate spacing for remaining problems
                    remaining_problems = min(problems_per_page - idx, 4)
                    spacing = self._calculate_dynamic_spacing(
                        problem_type,
                        remaining_problems,
                        y_start,
                        footer_start
                    )
                    x_start = 4.25 * inch
                    y_pos = y_start
            elif is_graphing:
                # Graphing: 2 columns x 2 rows
                if idx == 2:
                    # Move to second column for problems 3 and 4
                    x_start = 4.25 * inch
                    y_pos = y_start  # Reset to top for second column
            else:
                # Regular equations: 3 columns of 5
                if idx > 0 and idx % 5 == 0:
                    if idx == 5:
                        # Second column
                        remaining_problems = min(problems_per_page - idx, 5)
                        spacing = self._calculate_dynamic_spacing(
                            problem_type,
                            remaining_problems,
                            y_start,
                            footer_start
                        )
                        x_start = 4.5 * inch
                        y_pos = y_start
                    elif idx == 10:
                        # Third column
                        remaining_problems = min(problems_per_page - idx, 5)
                        spacing = self._calculate_dynamic_spacing(
                            problem_type,
                            remaining_problems,
                            y_start,
                            footer_start
                        )
                        x_start = 1 * inch
                        y_pos = y_start

            # Problem number and equation text - use Lexend
            try:
                c.setFont("Lexend", 12)
            except:
                c.setFont("Helvetica", 12)

            if is_inequality:
                # For inequalities: display equation as plain text next to problem number
                # Convert LaTeX to plain text
                symbol_map = {
                    '\\leq': '≤',
                    '\\geq': '≥',
                    '<': '<',
                    '>': '>'
                }
                ineq_symbol = symbol_map.get(equation.inequality_type, equation.inequality_type)
                # Convert LaTeX equation to plain text (remove LaTeX formatting)
                plain_text = equation.latex.replace('\\leq', '≤').replace('\\geq', '≥').replace('\\', '')
                c.drawString(x_start, y_pos, f"{idx + 1}. {plain_text}")
            elif is_system:
                # For systems: display both equations as plain text
                # Convert LaTeX to plain text
                eq1_plain = equation.equation1_latex.replace('\\', '')
                eq2_plain = equation.equation2_latex.replace('\\', '')
                c.drawString(x_start, y_pos, f"{idx + 1}. {eq1_plain}")
                c.drawString(x_start + 0.25 * inch, y_pos - 0.25 * inch, eq2_plain)
            elif is_property:
                # For properties: display problem number
                c.drawString(x_start, y_pos, f"{idx + 1}.")

                # Render the equation as LaTeX image
                try:
                    img = self.render_latex_to_image(equation.latex, config.latex_fontsize)
                    c.drawImage(
                        img,
                        x_start + 0.25 * inch,
                        y_pos - config.vertical_offset * inch,
                        width=config.image_width * inch,
                        height=config.image_height * inch,
                        preserveAspectRatio=True
                    )
                except Exception as e:
                    # Fallback to plain text if LaTeX rendering fails
                    import traceback
                    traceback.print_exc()
                    c.drawString(x_start + 0.25 * inch, y_pos, equation.equation)
                    print(f"Warning: LaTeX rendering failed for {equation.equation}: {e}")

                c.drawString(x_start + 0.25 * inch, y_pos - 0.5 * inch, "Property:")
            elif is_word_problem:
                # For word problems: display the problem text with wrapping
                # Draw problem number first
                c.drawString(x_start, y_pos, f"{idx + 1}.")
                # Wrap and draw the problem text (full page width minus margins)
                text_end_y = self._wrap_text(c, equation.problem_text, x_start + 0.25 * inch, y_pos, 6.0, line_height=0.18)
                # Add blank lines for students to write equation and solve
                c.drawString(x_start + 0.25 * inch, text_end_y - 0.15 * inch, "Equation: _______________________")
                c.drawString(x_start + 0.25 * inch, text_end_y - 0.4 * inch, "Solution: _______________________")
            elif is_graphing:
                # For graphing problems: display coordinate plane
                c.drawString(x_start, y_pos, f"{idx + 1}.")

                # For graphing points: display the points to plot as text
                if hasattr(equation, 'labels'):
                    c.setFont("Lexend", 10)
                    points_text = ", ".join(equation.labels)
                    # Column width is ~3.5 inches, wrap text to fit
                    text_y = self._wrap_text(c, points_text, x_start + 0.25 * inch, y_pos, 3.0, line_height=0.15)
                elif hasattr(equation, 'equation_latex'):
                    # For parabolas: display equation as LaTeX image
                    try:
                        img = self.render_latex_to_image(equation.equation_latex, 21)  # 21pt font
                        # Align the equation image vertically centered with the problem number
                        c.drawImage(
                            img,
                            x_start + 0.25 * inch,
                            y_pos - 0.09 * inch,  # Reduced offset to align better with 12pt problem numbers
                            width=2.5 * inch,
                            height=0.28 * inch,  # Adjusted for 21pt font
                            preserveAspectRatio=True,
                            mask='auto'
                        )
                        text_y = y_pos - 0.37 * inch
                    except Exception as e:
                        print(f"Warning: Failed to render parabola equation: {e}")
                        text_y = y_pos
                elif hasattr(equation, 'equation1_latex'):
                    # For systems: display both equations as LaTeX images
                    try:
                        img1 = self.render_latex_to_image(equation.equation1_latex, 21)  # 21pt font
                        c.drawImage(
                            img1,
                            x_start + 0.25 * inch,
                            y_pos - 0.09 * inch,  # Reduced offset to align better with 12pt problem numbers
                            width=2.5 * inch,
                            height=0.28 * inch,  # Adjusted for 21pt font
                            preserveAspectRatio=True,
                            mask='auto'
                        )
                        img2 = self.render_latex_to_image(equation.equation2_latex, 21)  # 21pt font
                        c.drawImage(
                            img2,
                            x_start + 0.25 * inch,
                            y_pos - 0.34 * inch,  # Adjusted spacing for 21pt font
                            width=2.5 * inch,
                            height=0.28 * inch,  # Adjusted for 21pt font
                            preserveAspectRatio=True,
                            mask='auto'
                        )
                        text_y = y_pos - 0.60 * inch
                    except Exception as e:
                        print(f"Warning: Failed to render system equations: {e}")
                        text_y = y_pos
                else:
                    text_y = y_pos

                # Draw the blank worksheet image (coordinate plane)
                try:
                    c.drawImage(
                        ImageReader(equation.worksheet_image),
                        x_start,
                        text_y - config.image_height * inch - 0.15 * inch,
                        width=config.image_width * inch,
                        height=config.image_height * inch,
                        preserveAspectRatio=True
                    )
                except Exception as e:
                    print(f"Warning: Failed to render graphing worksheet image: {e}")
            else:
                # For regular equations: display equation as plain text
                plain_text = equation.latex.replace('\\', '')
                c.drawString(x_start, y_pos, f"{idx + 1}. {plain_text}")

            # Render number line for inequalities only
            if is_inequality:
                try:
                    # Inequality: use worksheet image (blank number line)
                    img = ImageReader(equation.worksheet_image)

                    # Number line width - slightly shorter than full column
                    numberline_width = 3.0 * inch
                    # Calculate height based on aspect ratio (8" wide x 1.2" tall for number line only)
                    natural_height = (1.2 / 8.0) * numberline_width
                    # Position number line below the equation text
                    c.drawImage(
                        img,
                        x_start + 0.1 * inch,
                        y_pos - 0.35 * inch - natural_height,  # Below equation text
                        width=numberline_width,
                        height=natural_height,
                        preserveAspectRatio=True
                    )
                except Exception as e:
                    print(f"Warning: Number line rendering failed: {e}")

            y_pos -= spacing

        # Footer - use Lexend
        try:
            c.setFont("Lexend", 10)
        except:
            c.setFont("Helvetica", 10)
        c.drawCentredString(width / 2, 0.5 * inch, "freshmath.org")

    def _draw_logo(self, c: canvas.Canvas, width: float, height: float):
        """Draw the Fresh Math logo in the bottom right corner."""
        try:
            # Get the path to the logo
            base_dir = os.path.dirname(os.path.dirname(__file__))
            logo_path = os.path.join(base_dir, 'src', 'icons', 'FreshMath_V3', 'Black', 'FreshMath_Black_Secondary.png')

            if os.path.exists(logo_path):
                # Logo size (0.8 inches - twice as big)
                logo_size = 0.8 * inch
                # Position in bottom right corner with some margin
                x_pos = width - 1.2 * inch
                y_pos = 0.4 * inch

                # Draw the logo
                c.drawImage(logo_path, x_pos, y_pos, width=logo_size, height=logo_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            # Silently fail if logo can't be loaded
            print(f"Note: Could not load Fresh Math logo: {e}")

    def _draw_answer_key_page(self, c: canvas.Canvas, equations: List[Union[Equation, SystemProblem, InequalityProblem, PropertyProblem, WordProblem, MultiStepEquation]],
                             title: str, width: float, height: float):
        """Draw the answer key page with same layout as worksheet, answers in red."""
        # Header with logo in top right (matching worksheet page)
        y_pos = height - 0.5 * inch

        # Draw QR code in top left corner
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            qr_path = os.path.join(base_dir, 'src', 'icons', 'freshmath_qr.png')

            if os.path.exists(qr_path):
                qr_size = 0.55 * inch  # QR code size (0.55 x 0.55 inches)
                # Position 0.25 inches from top and left edges
                qr_x = 0.25 * inch
                qr_y = height - 0.25 * inch - qr_size  # 0.25" from top

                c.drawImage(qr_path, qr_x, qr_y, width=qr_size, height=qr_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            pass  # Silently skip if QR code not available

        # Draw logo in top right (0.75 inches)
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            logo_path = os.path.join(base_dir, 'src', 'icons', 'FreshMath_V3',
                                     'Black', 'FreshMath_Black_Secondary.png')

            if os.path.exists(logo_path):
                logo_size = 0.75 * inch  # 0.75 x 0.75 inches
                # Position in top right corner with margin
                logo_x = width - logo_size - 0.25 * inch
                logo_y = y_pos - logo_size + 0.3 * inch  # Adjust vertical alignment

                c.drawImage(logo_path, logo_x, logo_y, width=logo_size, height=logo_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"Warning: Could not load logo: {e}")

        # Title - use Poppins-Bold if available
        try:
            c.setFont("Poppins-Bold", 18)
        except:
            try:
                c.setFont("Lexend-Bold", 18)
            except:
                c.setFont("Helvetica-Bold", 18)
        y_pos -= 0.5 * inch
        c.drawCentredString(width / 2, y_pos, f"{title} - Answer Key")

        # Detect problem type and get configuration
        if equations and isinstance(equations[0], SystemProblem):
            problem_type = 'system_of_equations'
            is_system = True
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
        elif equations and isinstance(equations[0], InequalityProblem):
            problem_type = 'inequality'
            is_system = False
            is_inequality = True
            is_property = False
            is_word_problem = False
            is_multistep = False
        elif equations and isinstance(equations[0], PropertyProblem):
            # Detect which type of properties: add/subtract or mult/div
            if equations[0].property_type in ['multiplication', 'division']:
                problem_type = 'properties_mult_div'
            else:
                problem_type = 'properties_of_equality'
            is_system = False
            is_inequality = False
            is_property = True
            is_word_problem = False
            is_multistep = False
        elif equations and isinstance(equations[0], WordProblem):
            problem_type = 'word_problems'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = True
            is_multistep = False
        elif equations and isinstance(equations[0], MultiStepEquation):
            problem_type = 'multistep_equations'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = True
            is_graphing = False
        elif equations and isinstance(equations[0], GraphingPointsProblem):
            problem_type = 'graphing_points'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
        elif equations and isinstance(equations[0], GraphingSystemProblem):
            problem_type = 'graphing_systems'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
        elif equations and isinstance(equations[0], ParabolaGraphingProblem):
            problem_type = 'graphing_parabolas'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
        else:
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False

        config = get_config(problem_type)

        # Start drawing problems - use same layout as worksheet
        y_pos -= 0.5 * inch
        try:
            c.setFont("Lexend", 12)
        except:
            c.setFont("Helvetica", 12)

        # Calculate usable vertical space with bleed edge and static padding (same as worksheet)
        header_end = y_pos
        footer_start = self.BOTTOM_MARGIN + self.BLEED_EDGE + self.BOTTOM_PADDING
        usable_space = header_end - footer_start

        # Use configuration for layout
        problems_per_page = min(len(equations), config.problems_per_page)

        # Determine problems per column based on problem type
        if is_inequality or is_system:
            problems_per_column = 4  # 2 columns × 4 rows
        elif is_graphing:
            problems_per_column = 2  # 2 columns × 2 rows
        else:  # linear equations
            problems_per_column = 5  # First two columns have 5 problems

        # Calculate dynamic spacing for first column (same as worksheet)
        actual_problems_first_column = min(problems_per_page, problems_per_column)
        spacing = self._calculate_dynamic_spacing(
            problem_type,
            actual_problems_first_column,
            header_end,
            footer_start
        )

        x_start = 1 * inch
        y_start = y_pos

        if is_inequality:
            # For inequalities: show number lines with solutions in 2-column layout
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 2 columns x 4 rows (same as worksheet)
                if idx > 0 and idx % 4 == 0:
                    # Move to second column after 4 problems
                    # Recalculate spacing for remaining problems
                    remaining_problems = min(problems_per_page - idx, 4)
                    spacing = self._calculate_dynamic_spacing(
                        problem_type,
                        remaining_problems,
                        y_start,
                        footer_start
                    )
                    x_start = 4.25 * inch
                    y_pos = y_start

                # Problem number and equation text (matching worksheet format) - use Lexend
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)
                # Convert LaTeX to plain text
                symbol_map = {
                    '\\leq': '≤',
                    '\\geq': '≥',
                    '<': '<',
                    '>': '>'
                }
                plain_text = equation.latex.replace('\\leq', '≤').replace('\\geq', '≥').replace('\\', '')
                c.drawString(x_start, y_pos, f"{idx + 1}. {plain_text}")

                # Render solved number line with solution
                try:
                    # Use answer image (number line with solution)
                    img = ImageReader(equation.answer_image)

                    # Draw number line
                    numberline_width = 3.0 * inch
                    natural_height = (1.2 / 8.0) * numberline_width
                    image_bottom = y_pos - 0.35 * inch - natural_height
                    c.drawImage(
                        img,
                        x_start + 0.1 * inch,
                        image_bottom,
                        width=numberline_width,
                        height=natural_height,
                        preserveAspectRatio=True
                    )

                    # Draw algebraic solution below the number line in RED - use Lexend
                    try:
                        c.setFont("Lexend", 12)
                    except:
                        c.setFont("Helvetica", 12)
                    ineq_symbol = symbol_map.get(equation.inequality_type, equation.inequality_type)
                    if equation.solution == int(equation.solution):
                        solution_str = f"x {ineq_symbol} {int(equation.solution)}"
                    else:
                        solution_str = f"x {ineq_symbol} {equation.solution:.2f}"

                    # Set color to red for the solution
                    c.setFillColorRGB(1, 0, 0)  # Red color
                    c.drawString(x_start + 0.1 * inch, image_bottom - 0.25 * inch, solution_str)
                    c.setFillColorRGB(0, 0, 0)  # Reset to black

                except Exception as e:
                    print(f"Warning: Answer key rendering failed: {e}")

                y_pos -= spacing

        elif is_system:
            # For systems: 2 columns x 4 rows layout with answers in red
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 2 columns x 4 rows (same as worksheet)
                if idx > 0 and idx % 4 == 0:
                    # Move to second column after 4 problems
                    # Recalculate spacing for remaining problems
                    remaining_problems = min(problems_per_page - idx, 4)
                    spacing = self._calculate_dynamic_spacing(
                        problem_type,
                        remaining_problems,
                        y_start,
                        footer_start
                    )
                    x_start = 4.25 * inch
                    y_pos = y_start

                # Display problem number and both equations as plain text
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                eq1_plain = equation.equation1_latex.replace('\\', '')
                eq2_plain = equation.equation2_latex.replace('\\', '')
                c.drawString(x_start, y_pos, f"{idx + 1}. {eq1_plain}")
                c.drawString(x_start + 0.25 * inch, y_pos - 0.25 * inch, eq2_plain)

                # Display answer in RED below the equations
                c.setFillColorRGB(1, 0, 0)  # Red color
                c.drawString(x_start + 0.25 * inch, y_pos - 0.55 * inch, equation.solution)
                c.setFillColorRGB(0, 0, 0)  # Reset to black

                y_pos -= spacing

        elif is_property:
            # For properties: 2 columns x 5 rows layout with answers in red
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 2 columns x 5 rows (same as worksheet)
                if idx > 0 and idx % 5 == 0:
                    # Move to second column after 5 problems
                    # Recalculate spacing for remaining problems
                    remaining_problems = min(problems_per_page - idx, 5)
                    spacing = self._calculate_dynamic_spacing(
                        problem_type,
                        remaining_problems,
                        y_start,
                        footer_start
                    )
                    x_start = 4.25 * inch
                    y_pos = y_start

                # Display problem number
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                c.drawString(x_start, y_pos, f"{idx + 1}.")

                # Render the equation as LaTeX image
                try:
                    img = self.render_latex_to_image(equation.latex, config.latex_fontsize)
                    c.drawImage(
                        img,
                        x_start + 0.25 * inch,
                        y_pos - config.vertical_offset * inch,
                        width=config.image_width * inch,
                        height=config.image_height * inch,
                        preserveAspectRatio=True
                    )
                except Exception as e:
                    # Fallback to plain text if LaTeX rendering fails
                    c.drawString(x_start + 0.25 * inch, y_pos, equation.equation)
                    print(f"Warning: LaTeX rendering failed for {equation.equation}: {e}")

                # Display property name and solution in RED
                c.setFillColorRGB(1, 0, 0)  # Red color
                property_name = f"{equation.property_type.title()} Property (x = {equation.solution})"
                c.drawString(x_start + 0.25 * inch, y_pos - 0.5 * inch, f"Property: {property_name}")
                c.setFillColorRGB(0, 0, 0)  # Reset to black

                y_pos -= spacing

        elif is_word_problem:
            # For word problems: single column layout with answers in red
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Display problem text with wrapping
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                # Draw problem number first
                c.drawString(x_start, y_pos, f"{idx + 1}.")
                # Wrap and draw the problem text (full page width minus margins)
                text_end_y = self._wrap_text(c, equation.problem_text, x_start + 0.25 * inch, y_pos, 6.0, line_height=0.18)

                # Display equation and solution in RED
                c.setFillColorRGB(1, 0, 0)  # Red color
                c.drawString(x_start + 0.25 * inch, text_end_y - 0.15 * inch, f"Equation: {equation.equation}")
                c.drawString(x_start + 0.25 * inch, text_end_y - 0.4 * inch, f"Solution: x = {equation.solution}")
                c.setFillColorRGB(0, 0, 0)  # Reset to black

                y_pos -= spacing

        elif is_graphing:
            # For graphing problems: 2 columns x 2 rows layout with plotted points
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 2 columns x 2 rows
                if idx == 2:
                    # Move to second column for problems 3 and 4
                    x_start = 4.25 * inch
                    y_pos = y_start  # Reset to top for second column

                # Display problem number and points
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                c.drawString(x_start, y_pos, f"{idx + 1}.")

                # For graphing points: display the points with solutions
                if hasattr(equation, 'labels'):
                    c.setFont("Lexend", 10)
                    points_text = ", ".join(equation.labels)
                    text_y = self._wrap_text(c, points_text, x_start + 0.25 * inch, y_pos, 3.0, line_height=0.15)
                elif hasattr(equation, 'equation_latex'):
                    # For parabolas: display equation as LaTeX image
                    try:
                        img = self.render_latex_to_image(equation.equation_latex, 21)  # 21pt font
                        # Align the equation image vertically centered with the problem number
                        c.drawImage(
                            img,
                            x_start + 0.25 * inch,
                            y_pos - 0.09 * inch,  # Reduced offset to align better with 12pt problem numbers
                            width=2.5 * inch,
                            height=0.28 * inch,  # Adjusted for 21pt font
                            preserveAspectRatio=True,
                            mask='auto'
                        )
                        text_y = y_pos - 0.37 * inch
                    except Exception as e:
                        print(f"Warning: Failed to render parabola equation: {e}")
                        text_y = y_pos
                elif hasattr(equation, 'equation1_latex'):
                    # For systems: display both equations as LaTeX images
                    try:
                        img1 = self.render_latex_to_image(equation.equation1_latex, 21)  # 21pt font
                        c.drawImage(
                            img1,
                            x_start + 0.25 * inch,
                            y_pos - 0.09 * inch,  # Reduced offset to align better with 12pt problem numbers
                            width=2.5 * inch,
                            height=0.28 * inch,  # Adjusted for 21pt font
                            preserveAspectRatio=True,
                            mask='auto'
                        )
                        img2 = self.render_latex_to_image(equation.equation2_latex, 21)  # 21pt font
                        c.drawImage(
                            img2,
                            x_start + 0.25 * inch,
                            y_pos - 0.34 * inch,  # Adjusted spacing for 21pt font
                            width=2.5 * inch,
                            height=0.28 * inch,  # Adjusted for 21pt font
                            preserveAspectRatio=True,
                            mask='auto'
                        )
                        text_y = y_pos - 0.60 * inch
                    except Exception as e:
                        print(f"Warning: Failed to render system equations: {e}")
                        text_y = y_pos
                else:
                    text_y = y_pos

                # Draw the answer image (coordinate plane with solution)
                try:
                    c.drawImage(
                        ImageReader(equation.answer_image),
                        x_start,
                        text_y - config.image_height * inch - 0.15 * inch,
                        width=config.image_width * inch,
                        height=config.image_height * inch,
                        preserveAspectRatio=True
                    )
                except Exception as e:
                    print(f"Warning: Failed to render graphing answer image: {e}")

                y_pos -= spacing

        else:
            # For linear equations: 3 columns x 5 rows layout with answers in red
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 3 columns of 5 problems each (same as worksheet)
                if idx > 0 and idx % 5 == 0:
                    if idx == 5:
                        # Second column
                        remaining_problems = min(problems_per_page - idx, 5)
                        spacing = self._calculate_dynamic_spacing(
                            problem_type,
                            remaining_problems,
                            y_start,
                            footer_start
                        )
                        x_start = 4.5 * inch
                        y_pos = y_start
                    elif idx == 10:
                        # Third column
                        remaining_problems = min(problems_per_page - idx, 5)
                        spacing = self._calculate_dynamic_spacing(
                            problem_type,
                            remaining_problems,
                            y_start,
                            footer_start
                        )
                        x_start = 1 * inch
                        y_pos = y_start

                # Display problem number and equation as plain text
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                plain_text = equation.latex.replace('\\', '')
                c.drawString(x_start, y_pos, f"{idx + 1}. {plain_text}")

                # Display answer in RED below the equation
                c.setFillColorRGB(1, 0, 0)  # Red color
                if equation.solution == int(equation.solution):
                    solution_str = f"x = {int(equation.solution)}"
                else:
                    solution_str = f"x = {equation.solution:.2f}"
                c.drawString(x_start + 0.25 * inch, y_pos - 0.25 * inch, solution_str)
                c.setFillColorRGB(0, 0, 0)  # Reset to black

                y_pos -= spacing

        # Footer - use Lexend
        try:
            c.setFont("Lexend", 10)
        except:
            c.setFont("Helvetica", 10)
        c.drawCentredString(width / 2, 0.5 * inch, "freshmath.org")


# Example usage and testing
if __name__ == "__main__":
    from equation_generator import LinearEquationGenerator

    # Generate sample equations
    generator = LinearEquationGenerator()
    equations = generator.generate_worksheet('medium', 10)

    # Create PDF
    pdf_gen = PDFWorksheetGenerator()
    output_file = "test_worksheet.pdf"
    pdf_gen.generate_worksheet(equations, output_file,
                               title="Linear Equations Practice",
                               include_answer_key=True)

    print(f"\nTest worksheet created: {output_file}")
    print(f"Generated {len(equations)} problems")
