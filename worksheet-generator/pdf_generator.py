"""
PDF worksheet generator with LaTeX equation rendering.
Creates printable worksheets and answer keys.
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
from worksheet_config import get_config, ProblemTypeConfig
from typing import Union


class PDFWorksheetGenerator:
    """Generates PDF worksheets with LaTeX-rendered equations."""

    # Page layout constants
    BLEED_EDGE = 0.125 * inch  # Standard print bleed
    TOP_MARGIN = 0.5 * inch
    BOTTOM_MARGIN = 0.5 * inch
    BOTTOM_PADDING = 1.0 * inch  # Static padding to keep problems from extending too low

    # Spacing constraints per problem type (min, max)
    MIN_SPACING = {
        'linear_equation': 0.6 * inch,
        'system_of_equations': 1.0 * inch,
        'inequality': 1.5 * inch
    }

    MAX_SPACING = {
        'linear_equation': 2.5 * inch,
        'system_of_equations': 2.0 * inch,
        'inequality': 2.5 * inch
    }

    def __init__(self):
        """Initialize the PDF generator."""
        # Configure matplotlib for LaTeX rendering
        plt.rcParams['mathtext.fontset'] = 'cm'  # Computer Modern font
        plt.rcParams['font.size'] = 14

        # Register custom fonts for ReportLab
        self._register_fonts()

        # Try to configure matplotlib to use Lexend for number line labels
        try:
            lexend_path = os.path.join(os.path.dirname(__file__), '..', 'Lexend', 'static', 'Lexend-Regular.ttf')
            if os.path.exists(lexend_path):
                fm.fontManager.addfont(lexend_path)
                plt.rcParams['font.family'] = 'Lexend'
        except Exception as e:
            print(f"Note: Could not configure Lexend for matplotlib: {e}")

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

        # Render LaTeX text
        ax.text(0.05, 0.5, f'${latex_str}$', fontsize=fontsize, verticalalignment='center')

        # Save to bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.1,
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

    def render_blank_numberline(self, min_val: int, max_val: int,
                               solution: float, is_solution_left: bool,
                               inequality_type: str, show_solution: bool = False) -> ImageReader:
        """
        Render just a number line without equation text.

        Args:
            min_val: Minimum value on number line
            max_val: Maximum value on number line
            solution: The boundary value
            is_solution_left: True if solution is to the left (x < value)
            inequality_type: '<', '>', '<=', '>='
            show_solution: If True, show solution on number line; if False, show blank line

        Returns:
            ImageReader object for reportlab
        """
        # Create figure with just the number line
        fig, ax_line = plt.subplots(1, 1, figsize=(8, 1.2))

        # Number line using matplotlib's native axis
        ax_line.set_xlim(min_val - 0.5, max_val + 0.5)
        ax_line.set_ylim(-1, 1)
        # Don't use equal aspect - let it stretch to fill width

        # Style the axes - only show bottom spine
        ax_line.spines['left'].set_visible(False)
        ax_line.spines['right'].set_visible(False)
        ax_line.spines['top'].set_visible(False)
        ax_line.spines['bottom'].set_position(('data', 0))
        ax_line.spines['bottom'].set_linewidth(3)
        ax_line.yaxis.set_visible(False)

        # Set x-axis ticks and labels
        ax_line.set_xticks(range(min_val, max_val + 1))
        ax_line.tick_params(axis='x', width=3, length=10, labelsize=14)

        # Draw solution only if show_solution is True
        if show_solution:
            # Draw solution point
            is_equal = inequality_type in ['\\leq', '\\geq']
            if is_equal:
                # Closed circle
                ax_line.plot(solution, 0, 'o', markersize=15, color='blue',
                            markerfacecolor='blue', markeredgewidth=3)
            else:
                # Open circle
                ax_line.plot(solution, 0, 'o', markersize=15, color='blue',
                            fillstyle='none', markeredgewidth=3)

            # Draw arrow showing solution region
            if is_solution_left:
                ax_line.annotate('', xy=(min_val - 0.3, 0), xytext=(solution, 0),
                               arrowprops=dict(arrowstyle='->', color='blue', lw=4))
            else:
                ax_line.annotate('', xy=(max_val + 0.3, 0), xytext=(solution, 0),
                               arrowprops=dict(arrowstyle='->', color='blue', lw=4))

        # Save to buffer
        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight',
                    pad_inches=0.1, facecolor='white')
        buf.seek(0)
        plt.close(fig)

        return ImageReader(buf)

    def render_inequality_with_numberline(self, latex_str: str, min_val: int, max_val: int,
                                         solution: float, is_solution_left: bool,
                                         inequality_type: str, fontsize: int = 18,
                                         show_solution: bool = True) -> ImageReader:
        """
        Render an inequality with a number line.

        Args:
            latex_str: Inequality in LaTeX format
            min_val: Minimum value on number line
            max_val: Maximum value on number line
            solution: The boundary value
            is_solution_left: True if solution is to the left (x < value)
            inequality_type: '<', '>', '<=', '>='
            fontsize: Font size for inequality
            show_solution: If True, show solution on number line; if False, show blank line

        Returns:
            ImageReader object for reportlab
        """
        # Create figure with two subplots stacked vertically
        fig, (ax_eq, ax_line) = plt.subplots(2, 1, figsize=(8, 2.5),
                                              gridspec_kw={'height_ratios': [1, 2]})

        # Top subplot: inequality equation
        ax_eq.axis('off')
        ax_eq.text(0.5, 0.5, f'${latex_str}$', fontsize=fontsize,
                   ha='center', va='center')

        # Bottom subplot: number line using matplotlib's native axis
        ax_line.set_xlim(min_val - 0.5, max_val + 0.5)
        ax_line.set_ylim(-1, 1)
        ax_line.set_aspect('equal')

        # Style the axes - only show bottom spine
        ax_line.spines['left'].set_visible(False)
        ax_line.spines['right'].set_visible(False)
        ax_line.spines['top'].set_visible(False)
        ax_line.spines['bottom'].set_position(('data', 0))
        ax_line.spines['bottom'].set_linewidth(3)
        ax_line.yaxis.set_visible(False)

        # Set x-axis ticks and labels
        ax_line.set_xticks(range(min_val, max_val + 1))
        ax_line.tick_params(axis='x', width=3, length=10, labelsize=14)

        # Draw solution only if show_solution is True
        if show_solution:
            # Draw solution point
            is_equal = inequality_type in ['\\leq', '\\geq']
            if is_equal:
                # Closed circle
                ax_line.plot(solution, 0, 'o', markersize=15, color='blue',
                            markerfacecolor='blue', markeredgewidth=3)
            else:
                # Open circle
                ax_line.plot(solution, 0, 'o', markersize=15, color='blue',
                            fillstyle='none', markeredgewidth=3)

            # Draw arrow showing solution region
            if is_solution_left:
                ax_line.annotate('', xy=(min_val - 0.3, 0), xytext=(solution, 0),
                               arrowprops=dict(arrowstyle='->', color='blue', lw=4))
            else:
                ax_line.annotate('', xy=(max_val + 0.3, 0), xytext=(solution, 0),
                               arrowprops=dict(arrowstyle='->', color='blue', lw=4))

        # Save to buffer
        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight',
                    pad_inches=0.1, facecolor='white')
        buf.seek(0)
        plt.close(fig)

        return ImageReader(buf)

    def generate_worksheet(self, equations: List[Union[Equation, SystemProblem, InequalityProblem]], output_path: str,
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

    def _draw_worksheet_page(self, c: canvas.Canvas, equations: List[Union[Equation, SystemProblem, InequalityProblem]],
                            title: str, width: float, height: float):
        """Draw the main worksheet page with problems."""
        # Header with logo in top right
        y_pos = height - 0.5 * inch

        # Draw QR code in top left corner
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            qr_path = os.path.join(base_dir, 'src', 'icons', 'freshmath_qr.png')

            if os.path.exists(qr_path):
                qr_size = 0.6 * inch  # QR code size
                # Position 0.25 inches from top and left edges
                qr_x = 0.25 * inch
                qr_y = height - 0.25 * inch - qr_size  # 0.25" from top

                c.drawImage(qr_path, qr_x, qr_y, width=qr_size, height=qr_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            pass  # Silently skip if QR code not available

        # Draw logo in top right (1.2 inches - reduced by 25%)
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            logo_path = os.path.join(base_dir, 'src', 'icons', 'FreshMath_V3',
                                     'Black', 'FreshMath_Black_Secondary.png')

            if os.path.exists(logo_path):
                logo_size = 1.2 * inch  # Reduced by 25% from 1.6 inches
                # Position in top right corner with margin
                logo_x = width - logo_size - 0.25 * inch
                logo_y = y_pos - logo_size + 0.3 * inch  # Adjust vertical alignment

                c.drawImage(logo_path, logo_x, logo_y, width=logo_size, height=logo_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"Warning: Could not load logo: {e}")

        # Header fields - use Poppins if available, else Lexend
        try:
            c.setFont("Poppins", 11)
        except:
            c.setFont("Lexend", 11)

        # Name on left (positioned after QR code)
        c.drawString(1 * inch, y_pos, "Name: _________________________")

        # Date to the left of logo (in top right area)
        date_x = width - 1.2 * inch - 0.7 * inch  # Position left of logo with some spacing
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
        elif equations and isinstance(equations[0], InequalityProblem):
            problem_type = 'inequality'
            is_system = False
            is_inequality = True
        else:
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False

        config = get_config(problem_type)

        # Draw problems - use Lexend
        y_pos -= 0.5 * inch
        try:
            c.setFont("Lexend", 11)
        except:
            c.setFont("Helvetica", 11)

        # Calculate usable vertical space with bleed edge and static padding
        header_end = y_pos  # Current position after instructions
        footer_start = self.BOTTOM_MARGIN + self.BLEED_EDGE + self.BOTTOM_PADDING  # 0.625" + 1.0" = 1.625"
        usable_space = header_end - footer_start

        # Use configuration for layout
        problems_per_page = min(len(equations), config.problems_per_page)

        # Determine problems per column based on problem type
        if is_inequality or is_system:
            problems_per_column = 4  # 2 columns × 4 rows
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
                c.setFont("Lexend", 11)
            except:
                c.setFont("Helvetica", 11)

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
            else:
                # For regular equations: display equation as plain text
                plain_text = equation.latex.replace('\\', '')
                c.drawString(x_start, y_pos, f"{idx + 1}. {plain_text}")

            # Render number line for inequalities only
            if is_inequality:
                try:
                    # Inequality: render just BLANK number line for students to fill in
                    img = self.render_blank_numberline(
                        equation.number_line_min,
                        equation.number_line_max,
                        equation.solution,
                        equation.is_solution_left,
                        equation.inequality_type,
                        show_solution=False  # Blank number line on worksheet
                    )

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

    def _draw_answer_key_page(self, c: canvas.Canvas, equations: List[Union[Equation, SystemProblem, InequalityProblem]],
                             title: str, width: float, height: float):
        """Draw the answer key page with same layout as worksheet, answers in red."""
        # Header with logo in top right (matching worksheet page)
        y_pos = height - 0.5 * inch

        # Draw QR code in top left corner
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            qr_path = os.path.join(base_dir, 'src', 'icons', 'freshmath_qr.png')

            if os.path.exists(qr_path):
                qr_size = 0.6 * inch  # QR code size
                # Position 0.25 inches from top and left edges
                qr_x = 0.25 * inch
                qr_y = height - 0.25 * inch - qr_size  # 0.25" from top

                c.drawImage(qr_path, qr_x, qr_y, width=qr_size, height=qr_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            pass  # Silently skip if QR code not available

        # Draw logo in top right (1.2 inches - reduced by 25%)
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            logo_path = os.path.join(base_dir, 'src', 'icons', 'FreshMath_V3',
                                     'Black', 'FreshMath_Black_Secondary.png')

            if os.path.exists(logo_path):
                logo_size = 1.2 * inch  # Reduced by 25% from 1.6 inches
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
        elif equations and isinstance(equations[0], InequalityProblem):
            problem_type = 'inequality'
            is_system = False
            is_inequality = True
        else:
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False

        config = get_config(problem_type)

        # Start drawing problems - use same layout as worksheet
        y_pos -= 0.5 * inch
        try:
            c.setFont("Lexend", 11)
        except:
            c.setFont("Helvetica", 11)

        # Calculate usable vertical space with bleed edge and static padding (same as worksheet)
        header_end = y_pos
        footer_start = self.BOTTOM_MARGIN + self.BLEED_EDGE + self.BOTTOM_PADDING
        usable_space = header_end - footer_start

        # Use configuration for layout
        problems_per_page = min(len(equations), config.problems_per_page)

        # Determine problems per column based on problem type
        if is_inequality or is_system:
            problems_per_column = 4  # 2 columns × 4 rows
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
                    c.setFont("Lexend", 11)
                except:
                    c.setFont("Helvetica", 11)
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
                    img = self.render_blank_numberline(
                        equation.number_line_min,
                        equation.number_line_max,
                        equation.solution,
                        equation.is_solution_left,
                        equation.inequality_type,
                        show_solution=True  # Show solution on answer key
                    )

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
                        c.setFont("Lexend", 11)
                    except:
                        c.setFont("Helvetica", 11)
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
                    c.setFont("Lexend", 11)
                except:
                    c.setFont("Helvetica", 11)

                eq1_plain = equation.equation1_latex.replace('\\', '')
                eq2_plain = equation.equation2_latex.replace('\\', '')
                c.drawString(x_start, y_pos, f"{idx + 1}. {eq1_plain}")
                c.drawString(x_start + 0.25 * inch, y_pos - 0.25 * inch, eq2_plain)

                # Display answer in RED below the equations
                c.setFillColorRGB(1, 0, 0)  # Red color
                c.drawString(x_start + 0.25 * inch, y_pos - 0.55 * inch, equation.solution)
                c.setFillColorRGB(0, 0, 0)  # Reset to black

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
                    c.setFont("Lexend", 11)
                except:
                    c.setFont("Helvetica", 11)

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
