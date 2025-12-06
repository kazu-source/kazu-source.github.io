"""
PDF worksheet generator with LaTeX equation rendering.
Creates printable worksheets and answer keys.

FONT SIZE STANDARDS:
- Problem numbers: 12pt Lexend
- Equations: 21pt Lexend (1.75x ratio to problem numbers)
- This ratio should be maintained across ALL worksheet types
"""

import os
import sys
import io
import re
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


def get_base_path():
    """Get the base path for bundled resources (fonts, etc.)."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return sys._MEIPASS
    else:
        # Running as script - fonts are in parent directory
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Legacy imports with fallback to stub classes
try:
    from equation_generator import Equation
except ImportError:
    class Equation: pass  # Stub class for backwards compatibility

try:
    from systems_generator import SystemProblem
except ImportError:
    class SystemProblem: pass  # Stub class

try:
    from inequalities_generator import InequalityProblem
except ImportError:
    class InequalityProblem: pass  # Stub class

from generators.High_School.Algebra.Unit_3.compound_inequalities_generator import CompoundInequalityProblem

try:
    from properties_generator import PropertyProblem
except ImportError:
    class PropertyProblem: pass  # Stub class

try:
    from word_problems_generator import WordProblem
except ImportError:
    class WordProblem: pass  # Stub class

try:
    from multistep_generator import MultiStepEquation
except ImportError:
    class MultiStepEquation: pass  # Stub class
from generators.High_School.Algebra.Unit_1.evaluating_expressions_generator import EvaluatingProblem
from generators.High_School.Algebra.Unit_1.substitution_generator import SubstitutionProblem
from generators.High_School.Algebra.Unit_4.graphing_points import GraphingPointsProblem
from generators.High_School.Algebra.Unit_4.graphing_lines import GraphingLineProblem
from generators.High_School.Algebra.Unit_4.graphing_slope_intercept import SlopeInterceptProblem
from generators.High_School.Algebra.Unit_4.graphing_point_slope import PointSlopeProblem
from generators.High_School.Algebra.Unit_4.graphing_standard_form import StandardFormProblem
from generators.High_School.Algebra.Unit_4.slope_generator import SlopeProblem
from generators.High_School.Algebra.Unit_4.intercepts_generator import InterceptsProblem
from generators.High_School.Algebra.Unit_4.writing_slope_intercept import WritingSlopeInterceptProblem
from generators.High_School.Algebra.Unit_5.graphing_systems import GraphingSystemProblem
from generators.High_School.Algebra.Unit_5.systems_substitution import SubstitutionSystemProblem
from generators.High_School.Algebra.Unit_5.systems_elimination import EliminationSystemProblem
from generators.High_School.Algebra.Unit_6.functions_generator import FunctionsProblem
from generators.High_School.Algebra.Unit_6.domain_range_generator import DomainRangeProblem
from generators.High_School.Algebra.Unit_10.quadratic_graphing_generator import QuadraticGraphProblem
from generators.High_School.Algebra.Unit_4.graphing_parabolas import ParabolaGraphingProblem
from worksheet_config import get_config, ProblemTypeConfig
from typing import Union


class PDFWorksheetGenerator:
    """Generates PDF worksheets with LaTeX-rendered equations."""

    # Font size standards (maintain 1.75x ratio)
    
    def _get_problem_latex(self, problem):
        """Get LaTeX representation from any problem type."""
        if hasattr(problem, 'latex'):
            return problem.latex
        elif hasattr(problem, 'problem_latex'):
            return problem.problem_latex
        elif hasattr(problem, 'equation_latex'):
            return problem.equation_latex
        elif hasattr(problem, 'slope_latex'):
            return problem.slope_latex
        elif hasattr(problem, 'equation1') and hasattr(problem, 'equation2'):
            # For system problems
            return f"{problem.equation1}\\\\{problem.equation2}"
        elif hasattr(problem, 'function_notation'):
            return problem.function_notation
        else:
            return str(problem)
    
    def _get_problem_solution(self, problem):
        """Get solution from any problem type."""
        if hasattr(problem, 'solution'):
            return problem.solution
        elif hasattr(problem, 'answer_latex'):
            return problem.answer_latex
        elif hasattr(problem, 'solution_latex'):
            return problem.solution_latex
        elif isinstance(problem, (SubstitutionSystemProblem, EliminationSystemProblem)):
            if hasattr(problem, 'solution_x') and hasattr(problem, 'solution_y'):
                return f"({problem.solution_x}, {problem.solution_y})"
            elif hasattr(problem, 'solution_latex'):
                return problem.solution_latex
            else:
                return "See work shown"
        elif isinstance(problem, InterceptsProblem):
            intercepts = []
            if hasattr(problem, 'x_intercept') and problem.x_intercept:
                intercepts.append(f"x-intercept: {problem.x_intercept}")
            if hasattr(problem, 'y_intercept') and problem.y_intercept:
                intercepts.append(f"y-intercept: {problem.y_intercept}")
            return ", ".join(intercepts) if intercepts else "See answer key"
        elif isinstance(problem, SlopeProblem):
            return f"m = {problem.slope_fraction}"
        elif isinstance(problem, WritingSlopeInterceptProblem):
            return getattr(problem, 'answer_latex', getattr(problem, 'equation_latex', 'See work shown'))
        elif isinstance(problem, QuadraticGraphProblem):
            # Return key information for quadratic graph
            parts = []
            if hasattr(problem, 'vertex'):
                parts.append(f"Vertex: {problem.vertex}")
            if hasattr(problem, 'x_intercepts') and problem.x_intercepts:
                parts.append(f"x-intercepts: {problem.x_intercepts}")
            if hasattr(problem, 'y_intercept'):
                parts.append(f"y-intercept: {problem.y_intercept}")
            return ", ".join(parts) if parts else "See graph"
        elif isinstance(problem, (FunctionsProblem, DomainRangeProblem)):
            return getattr(problem, 'answer', getattr(problem, 'answer_latex', 'See work shown'))
        elif hasattr(problem, 'solution_x') and hasattr(problem, 'solution_y'):
            return f"({problem.solution_x}, {problem.solution_y})"
        else:
            return "See answer key"
    PROBLEM_NUMBER_FONT_SIZE = 12  # Lexend 12pt for problem numbers
    EQUATION_FONT_SIZE = 21  # Lexend 21pt for equations (1.75x ratio)

    # Page layout constants
    BLEED_EDGE = 0.125 * inch  # Standard print bleed
    TOP_MARGIN = 0.5 * inch
    BOTTOM_MARGIN = 0.5 * inch
    BOTTOM_PADDING = 1.0 * inch  # Static padding to keep problems from extending too low

    # Spacing constraints per problem type (min, max)
    MIN_SPACING = {
        'linear_equation': 0.5 * inch,  # Reduced for tighter spacing
        'multistep_equations': 0.5 * inch,  # Reduced for better vertical distribution
        'system_of_equations': 0.9 * inch,  # Slightly reduced for tighter spacing
        'inequality': 1.5 * inch,
        'word_problems': 2.0 * inch,  # Larger spacing for word problems to allow work space
        'graphing_points': 3.8 * inch,  # Minimum spacing for 3" graphs + text
        'graphing_lines': 3.8 * inch,  # Same as graphing_points
        'slope_intercept': 3.8 * inch,  # Same as graphing_points
        'point_slope': 3.8 * inch,  # Same as graphing_points
        'standard_form': 3.8 * inch,  # Same as graphing_points
        'graphing_systems': 3.8 * inch,  # Same as graphing_points
        'graphing_parabolas': 3.8 * inch  # Same as other graphing types
    }

    MAX_SPACING = {
        'linear_equation': 2.3 * inch,  # Slightly reduced for tighter spacing
        'multistep_equations': 2.3 * inch,  # Same as linear equations
        'system_of_equations': 1.8 * inch,  # Slightly reduced for tighter spacing
        'inequality': 2.5 * inch,
        'word_problems': 4.0 * inch,  # Maximum spacing for word problems to spread them out
        'graphing_points': 4.5 * inch,  # Maximum spacing for graphing problems
        'graphing_lines': 4.5 * inch,  # Same as graphing_points
        'slope_intercept': 4.5 * inch,  # Same as graphing_points
        'point_slope': 4.5 * inch,  # Same as graphing_points
        'standard_form': 4.5 * inch,  # Same as graphing_points
        'graphing_systems': 4.5 * inch,  # Same as graphing_points
        'graphing_parabolas': 4.5 * inch  # Same as other graphing types
    }

    def __init__(self):
        """Initialize the PDF generator."""
        # Register custom fonts for ReportLab
        self._register_fonts()

        # Configure matplotlib to use Lexend for all text (including equations)
        try:
            base_dir = get_base_path()
            lexend_path = os.path.join(base_dir, 'Lexend', 'static', 'Lexend-Regular.ttf')
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
            # Get the base path for fonts (works for both script and exe)
            base_dir = get_base_path()

            # Register Lexend fonts
            lexend_regular = os.path.join(base_dir, 'Lexend', 'static', 'Lexend-Regular.ttf')
            lexend_bold = os.path.join(base_dir, 'Lexend', 'static', 'Lexend-Bold.ttf')

            if os.path.exists(lexend_regular):
                pdfmetrics.registerFont(TTFont('Lexend', lexend_regular))
            else:
                raise FileNotFoundError(f"Lexend font not found at {lexend_regular}")

            if os.path.exists(lexend_bold):
                pdfmetrics.registerFont(TTFont('Lexend-Bold', lexend_bold))

            # Try to register Poppins fonts (for title, name, date)
            poppins_dir = os.path.join(base_dir, 'Poppins')
            poppins_regular = os.path.join(poppins_dir, 'Poppins-Regular.ttf')
            poppins_bold = os.path.join(poppins_dir, 'Poppins-Bold.ttf')

            if os.path.exists(poppins_regular):
                pdfmetrics.registerFont(TTFont('Poppins', poppins_regular))
            else:
                raise FileNotFoundError(f"Poppins font not found at {poppins_regular}")

            if os.path.exists(poppins_bold):
                pdfmetrics.registerFont(TTFont('Poppins-Bold', poppins_bold))

        except Exception as e:
            print(f"Warning: Could not register custom fonts: {e}")
            print(f"Base path: {get_base_path()}")
            print("Falling back to default fonts")
            raise  # Re-raise to make font issues visible

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

    def _draw_text_with_exponents(self, c: canvas.Canvas, text: str, x: float, y: float, font_size: int, max_width: float = None, line_height: float = 0.25) -> tuple:
        """
        Draw text with proper exponent (superscript) rendering.

        Args:
            c: Canvas object
            text: Text with exponents (e.g., "x^2 + 3y^3")
            x: X position to start drawing
            y: Y position (baseline)
            font_size: Font size for main text
            max_width: Maximum width in points before wrapping (None = no limit)
            line_height: Line height in inches for wrapped lines

        Returns:
            Tuple of (width in points, height in inches used)
        """
        current_x = x
        current_y = y
        start_x = x
        lines_used = 0
        i = 0

        while i < len(text):
            if i < len(text) - 1 and text[i+1] == '^':
                # Character followed by ^, draw it then handle the exponent
                c.setFont('Lexend', font_size)
                char_width = c.stringWidth(text[i], 'Lexend', font_size)

                # Check if we need to wrap
                if max_width and (current_x - start_x + char_width) > max_width:
                    current_y -= line_height * inch
                    current_x = start_x
                    lines_used += 1

                c.drawString(current_x, current_y, text[i])
                current_x += char_width

                # Skip the ^ character
                i += 2

                # Get the exponent - handle both x^2 and x^{2} formats
                exponent = ''
                # Check if exponent is wrapped in curly braces
                if i < len(text) and text[i] == '{':
                    i += 1  # Skip opening brace
                    while i < len(text) and text[i] != '}':
                        exponent += text[i]
                        i += 1
                    if i < len(text) and text[i] == '}':
                        i += 1  # Skip closing brace
                else:
                    # No braces, just get digits
                    while i < len(text) and (text[i].isdigit() or text[i] == '-'):
                        exponent += text[i]
                        i += 1

                # Draw exponent as superscript (smaller font, raised)
                exp_font_size = int(font_size * 0.7)  # 70% of main font
                c.setFont('Lexend', exp_font_size)
                exp_y = current_y + font_size * 0.4  # Raise by 40% of font size
                exp_width = c.stringWidth(exponent, 'Lexend', exp_font_size)

                # Check if exponent fits (usually very small, but check anyway)
                if max_width and (current_x - start_x + exp_width) > max_width:
                    current_y -= line_height * inch
                    current_x = start_x
                    lines_used += 1
                    exp_y = current_y + font_size * 0.4

                c.drawString(current_x, exp_y, exponent)
                current_x += exp_width
            else:
                # Regular character
                c.setFont('Lexend', font_size)
                char_width = c.stringWidth(text[i], 'Lexend', font_size)

                # Check if we need to wrap
                if max_width and (current_x - start_x + char_width) > max_width:
                    current_y -= line_height * inch
                    current_x = start_x
                    lines_used += 1

                c.drawString(current_x, current_y, text[i])
                current_x += char_width
                i += 1

        # Calculate total width and height used
        total_width = current_x - start_x
        total_height = lines_used * line_height  # in inches

        return (total_width, total_height)

    def _draw_equation_with_fractions(self, c: canvas.Canvas, equation_text: str, x: float, y: float, font_size: int = 21, max_width: float = None, line_height: float = 0.25) -> tuple:
        """
        Draw an equation with proper fraction and exponent rendering.

        Args:
            c: Canvas object
            equation_text: LaTeX equation text (e.g., "\\frac{x}{4} + 9 = 11" or "x^2 + 3")
            x: X position to start drawing
            y: Y position (baseline for text)
            font_size: Font size for equation text
            max_width: Maximum width in points before wrapping (None = no limit)
            line_height: Line height in inches for wrapped lines

        Returns:
            Tuple of (width in points, height in inches used)
        """
        # Check if this equation contains square roots
        # If so, render it as a LaTeX image instead of text
        if '\\sqrt' in equation_text:
            try:
                # Render the entire equation as a LaTeX image
                # Use the same font_size to maintain consistency
                img = self.render_latex_to_image(equation_text, font_size)

                # Get the actual image dimensions to calculate proper scaling
                img_width, img_height = img.getSize()

                # Calculate the scaling factor based on font size
                # At 12pt font, we want the image height to be approximately 0.5 inches
                # This matches the visual height of 12pt Lexend text
                target_height = (font_size / 12.0) * 0.5 * inch

                # Calculate width maintaining aspect ratio
                aspect_ratio = img_width / img_height
                target_width = target_height * aspect_ratio

                # Draw the image at the specified position with calculated dimensions
                # Align with text baseline: for 12pt text, descenders go ~3pt below baseline
                # Our square root symbol should align with text baseline
                # The rendered image has the square root symbol centered, so we offset by ~31% of height
                y_offset = target_height * 0.31

                c.drawImage(
                    img,
                    x,
                    y - y_offset,  # Position so square root baseline aligns with text baseline
                    width=target_width,
                    height=target_height,
                    preserveAspectRatio=True,
                    mask='auto'
                )
                return (target_width, 0)  # Return width in points, no wrapping
            except Exception as e:
                print(f"Warning: Failed to render equation as LaTeX image: {e}")
                # Fall through to text rendering

        # Replace LaTeX symbols with Unicode equivalents before removing backslashes
        text = equation_text.replace('\\cdot', '·')  # Replace \cdot with middle dot
        text = text.replace('\\times', '×')  # Replace \times with multiplication sign
        text = text.replace('\\lt', '<')  # Replace \lt with <
        text = text.replace('\\gt', '>')  # Replace \gt with >
        text = text.replace('\\leq', '≤')  # Replace \leq with ≤
        text = text.replace('\\geq', '≥')  # Replace \geq with ≥
        text = text.replace('\\left', '')  # Remove \left (sizing command)
        text = text.replace('\\right', '')  # Remove \right (sizing command)

        # Remove remaining backslashes
        text = text.replace('\\', '')
        # Remove text{} wrappers: text{content} -> content
        text = re.sub(r'text\{([^}]*)\}', r'\1', text)

        # Check if we have fractions or exponents
        has_fractions = 'frac{' in text
        has_exponents = '^' in text

        if not has_fractions and not has_exponents:
            # No special formatting needed, just draw normally
            c.setFont('Lexend', font_size)
            text_width = c.stringWidth(text, 'Lexend', font_size)

            # Check if wrapping is needed
            if max_width and text_width > max_width:
                # Use text wrapping for plain text
                height_used = self._wrap_text(c, text, x, y, max_width / inch, line_height)
                return (max_width, height_used)
            else:
                c.drawString(x, y, text)
                return (text_width, 0)

        # If we only have exponents (no fractions), handle them separately for efficiency
        if has_exponents and not has_fractions:
            width = self._draw_text_with_exponents(c, text, x, y, font_size, max_width, line_height)
            # _draw_text_with_exponents will be updated to return tuple, for now handle both cases
            if isinstance(width, tuple):
                return width
            else:
                return (width, 0)

        # Find all fractions in the text using regex
        # Pattern: frac{numerator}{denominator}
        fraction_pattern = r'frac\{([^}]+)\}\{([^}]+)\}'
        fractions = list(re.finditer(fraction_pattern, text))

        # We have fractions - need to draw them specially
        current_x = x
        current_y = y
        start_x = x
        last_end = 0
        lines_used = 0

        # Fraction rendering parameters - adjusted for proper spacing and font size
        fraction_font_size = 12  # Keep fraction components at 12pt (same as equation text)
        fraction_spacing = 0.05 * inch  # Extra spacing around fractions

        # Vertical positioning (in points, relative to baseline)
        # The fraction bar should align with the mathematical axis (where minus/plus signs center)
        numerator_offset = 8  # Points above baseline
        denominator_offset = -8  # Points below baseline
        bar_offset = 4  # Math axis position for 12pt text

        for match in fractions:
            # Draw text before this fraction
            before_text = text[last_end:match.start()]
            if before_text:
                c.setFont('Lexend', font_size)
                text_width = c.stringWidth(before_text, 'Lexend', font_size)

                # Check if we need to wrap
                if max_width and (current_x - start_x + text_width) > max_width:
                    current_y -= line_height * inch
                    current_x = start_x
                    lines_used += 1

                c.drawString(current_x, current_y, before_text)
                current_x += text_width

            # Get numerator and denominator
            numerator = match.group(1)
            denominator = match.group(2)

            # Calculate fraction dimensions
            c.setFont('Lexend', fraction_font_size)
            num_width = c.stringWidth(numerator, 'Lexend', fraction_font_size)
            denom_width = c.stringWidth(denominator, 'Lexend', fraction_font_size)
            fraction_width = max(num_width, denom_width) + 4  # Add 4 points padding
            total_fraction_width = fraction_width + 2 * fraction_spacing

            # Check if fraction fits on current line
            if max_width and (current_x - start_x + total_fraction_width) > max_width:
                current_y -= line_height * inch
                current_x = start_x
                lines_used += 1

            # Add spacing before fraction
            current_x += fraction_spacing

            # Draw numerator (centered above the baseline)
            num_x = current_x + (fraction_width - num_width) / 2
            num_y = current_y + numerator_offset
            c.drawString(num_x, num_y, numerator)

            # Draw fraction bar
            bar_y = current_y + bar_offset
            c.setLineWidth(0.5)  # Thinner line for cleaner look
            c.line(current_x, bar_y, current_x + fraction_width, bar_y)

            # Draw denominator (centered below the bar with proper gap)
            denom_x = current_x + (fraction_width - denom_width) / 2
            denom_y = current_y + denominator_offset
            c.drawString(denom_x, denom_y, denominator)

            # Move past the fraction
            current_x += fraction_width + fraction_spacing
            last_end = match.end()

        # Draw any remaining text after the last fraction
        remaining_text = text[last_end:]
        if remaining_text:
            c.setFont('Lexend', font_size)
            text_width = c.stringWidth(remaining_text, 'Lexend', font_size)

            # Check if we need to wrap
            if max_width and (current_x - start_x + text_width) > max_width:
                current_y -= line_height * inch
                current_x = start_x
                lines_used += 1

            c.drawString(current_x, current_y, remaining_text)
            current_x += text_width

        # Calculate total width and height used
        total_width = current_x - start_x
        total_height = lines_used * line_height  # in inches

        return (total_width, total_height)

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
        elif problem_type in ['graphing_points', 'graphing_lines', 'slope_intercept', 'point_slope', 'standard_form', 'graphing_systems', 'graphing_parabolas']:
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
        min_spacing = self.MIN_SPACING.get(problem_type, 0.5 * inch)  # Default minimum spacing reduced to 0.5"
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
        # Check if this is a text-heavy problem (contains \text{, \mathrm{, or has more text than math)
        # Heuristic: if it contains words like "If", "Is", "Find", "Which", "Input", "Rule", etc.
        text_indicators = ['If ', 'Is ', 'Find ', 'Which ', 'Verify', 'Input:', 'Rule:', 'Output:']
        has_text_content = any(indicator in latex_str for indicator in text_indicators)

        if '\\text{' in latex_str or '\\mathrm{' in latex_str or has_text_content:
            # Use plain text rendering with embedded math
            return self._render_text_with_math(latex_str, fontsize)

        # Create figure with no axes
        fig = plt.figure(figsize=(4, 0.5))
        fig.patch.set_visible(False)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')

        # Render LaTeX text (x=0 for left alignment, baseline alignment to minimize vertical space)
        ax.text(0, 0.3, f'${latex_str}$', fontsize=fontsize, verticalalignment='baseline', horizontalalignment='left')

        # Save to bytes buffer with tight bbox and zero padding to eliminate whitespace
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0,
                    transparent=False, facecolor='white')
        buf.seek(0)
        plt.close(fig)

        return ImageReader(buf)

    def _render_text_with_math(self, latex_str: str, fontsize: int = 16) -> ImageReader:
        """
        Render text-heavy problems as plain text (convert LaTeX text commands to plain text).

        Args:
            latex_str: LaTeX string with text or mathrm commands
            fontsize: Font size for rendering

        Returns:
            ImageReader object for reportlab
        """
        import re

        # Convert \text{...} and \mathrm{...} to plain text (remove LaTeX commands, convert \  to spaces)
        # Replace escaped spaces with actual spaces
        processed = latex_str.replace('\\ ', ' ')

        # Remove \text{ and \mathrm{ commands but keep content
        processed = re.sub(r'\\text\{([^}]*)\}', r'\1', processed)
        processed = re.sub(r'\\mathrm\{([^}]*)\}', r'\1', processed)

        # Create figure
        fig = plt.figure(figsize=(6, 0.5))
        fig.patch.set_visible(False)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')

        # Render as plain text (not wrapped in $...$)
        ax.text(0, 0.5, processed, fontsize=fontsize, verticalalignment='center',
                horizontalalignment='left', family='sans-serif')

        # Save to bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.005,
                    transparent=False, facecolor='white')
        buf.seek(0)
        plt.close(fig)

        return ImageReader(buf)

    def render_system_to_image(self, eq1: str, eq2: str, fontsize: int = 16) -> ImageReader:
        """
        Render system equations with LaTeX array environment for perfect alignment.

        Args:
            eq1: First equation (e.g., "2x + 3y = 13")
            eq2: Second equation (e.g., "x - y = -1")
            fontsize: Font size for rendering

        Returns:
            ImageReader object for reportlab
        """
        import re

        # Parse equations to add phantom spacing for alignment
        # We'll use LaTeX array environment with right-aligned columns

        def format_for_array(eq):
            """Convert 'ax + by = c' to array format with alignment."""
            if '=' not in eq:
                return eq

            left, right = eq.split('=', 1)
            left = left.strip()
            right = right.strip()

            # Parse left side: find x term, operator, y term
            x_match = re.search(r'([+-]?\s*\d*)\s*x', left)
            y_match = re.search(r'x\s*([+-])\s*(\d*)\s*y', left)

            if not x_match or not y_match:
                return eq

            # Get x coefficient
            x_coef = x_match.group(1).replace(' ', '')
            if x_coef == '' or x_coef == '+':
                x_coef = '1'
            elif x_coef == '-':
                x_coef = '-1'

            # Get y parts
            y_sign = y_match.group(1)
            y_coef = y_match.group(2)
            if not y_coef:
                y_coef = '1'

            # Format with alignment: coef & x & sign & coef & y & = & constant
            return f"{x_coef} & x & {y_sign} & {y_coef} & y & = & {right}"

        # Format both equations
        formatted1 = format_for_array(eq1)
        formatted2 = format_for_array(eq2)

        # Create LaTeX array with column alignment (r = right, c = center, l = left)
        # Format: rcrcrcl means: right coef, center x, right sign, center coef, right y, center =, left constant
        latex_array = r'\begin{array}{rcrcrcl}' + formatted1 + r' \\' + formatted2 + r'\end{array}'

        # Create figure
        fig = plt.figure(figsize=(4, 1.0))
        fig.patch.set_visible(False)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')

        # Render the array
        ax.text(0.5, 0.5, f'${latex_array}$', fontsize=fontsize,
               verticalalignment='center', horizontalalignment='center')

        # Save to buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.05,
                    transparent=False, facecolor='white')
        buf.seek(0)
        plt.close(fig)

        return ImageReader(buf)

    def generate_worksheet(self, equations: List[Union[Equation, SystemProblem, InequalityProblem, CompoundInequalityProblem, PropertyProblem, WordProblem, MultiStepEquation, GraphingPointsProblem, GraphingLineProblem, SlopeInterceptProblem, PointSlopeProblem, StandardFormProblem, GraphingSystemProblem, ParabolaGraphingProblem, SlopeProblem, InterceptsProblem, WritingSlopeInterceptProblem, SubstitutionSystemProblem, EliminationSystemProblem, FunctionsProblem, DomainRangeProblem, QuadraticGraphProblem]], output_path: str,
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

        # Check if this is a challenge worksheet
        is_challenge = "Challenge" in title

        # Determine max problems per page based on problem type
        # Challenge worksheets always use 8 problems per page
        if is_challenge:
            max_problems_per_page = 8
        elif equations:
            # Determine problem type to get appropriate config
            if isinstance(equations[0], SystemProblem):
                from worksheet_config import get_config
                config = get_config('system_of_equations')
                max_problems_per_page = config.problems_per_page
            elif isinstance(equations[0], InequalityProblem) or isinstance(equations[0], CompoundInequalityProblem):
                from worksheet_config import get_config
                config = get_config('inequality')
                max_problems_per_page = config.problems_per_page
            elif isinstance(equations[0], (GraphingPointsProblem, GraphingLineProblem, SlopeInterceptProblem,
                                          PointSlopeProblem, StandardFormProblem, GraphingSystemProblem,
                                          ParabolaGraphingProblem, SlopeProblem, InterceptsProblem,
                                          WritingSlopeInterceptProblem, QuadraticGraphProblem)):
                from worksheet_config import get_config
                config = get_config('graphing_points')
                max_problems_per_page = config.problems_per_page
            elif isinstance(equations[0], (SubstitutionSystemProblem, EliminationSystemProblem)):
                from worksheet_config import get_config
                config = get_config('system_of_equations')
                max_problems_per_page = config.problems_per_page
            elif isinstance(equations[0], (FunctionsProblem, DomainRangeProblem)):
                from worksheet_config import get_config
                config = get_config('functions')
                max_problems_per_page = config.problems_per_page if hasattr(get_config('functions'), 'problems_per_page') else 8
            else:
                max_problems_per_page = 10  # Default for linear equations
        else:
            max_problems_per_page = 10

        # Generate worksheet pages (one page per max_problems_per_page problems)
        num_worksheet_pages = (len(equations) + max_problems_per_page - 1) // max_problems_per_page
        for page_idx in range(num_worksheet_pages):
            if page_idx > 0:
                c.showPage()  # Start new page for pages after the first
            start_idx = page_idx * max_problems_per_page
            end_idx = min(start_idx + max_problems_per_page, len(equations))
            page_problems = equations[start_idx:end_idx]
            self._draw_worksheet_page(c, page_problems, title, width, height, start_problem_number=start_idx + 1)

        if include_answer_key:
            # Answer key uses the same pagination as the worksheet
            # This ensures consistency: if worksheet has 8 problems per page, answer key does too
            problems_per_answer_page = max_problems_per_page

            # Generate answer key pages
            num_answer_pages = (len(equations) + problems_per_answer_page - 1) // problems_per_answer_page
            for page_idx in range(num_answer_pages):
                c.showPage()  # Start new page for answer key
                start_idx = page_idx * problems_per_answer_page
                end_idx = min(start_idx + problems_per_answer_page, len(equations))
                page_problems = equations[start_idx:end_idx]
                self._draw_answer_key_page(c, page_problems, title, width, height, start_problem_number=start_idx + 1)

        c.save()
        print(f"Worksheet saved to: {output_path}")

    def _draw_worksheet_page(self, c: canvas.Canvas, equations: List[Union[Equation, SystemProblem, InequalityProblem, CompoundInequalityProblem, PropertyProblem, WordProblem, MultiStepEquation]],
                            title: str, width: float, height: float, start_problem_number: int = 1):
        """Draw the main worksheet page with problems."""
        # Header with logo in top right
        y_pos = height - 0.5 * inch

        # Draw QR code in top left corner
        try:
            base_dir = get_base_path()
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

        # Draw logo in top right (0.6 inches)
        try:
            base_dir = get_base_path()
            logo_path = os.path.join(base_dir, 'src', 'icons', 'FreshMath_V3',
                                     'Black', 'FreshMath_Black_Secondary.png')

            if os.path.exists(logo_path):
                logo_size = 0.6 * inch  # 0.6 x 0.6 inches
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

        # Use the full title as provided
        display_title = title

        c.drawCentredString(width / 2, y_pos, display_title)

        # Reserve space for instructions (will be drawn after problem type detection)
        instructions_y_pos = y_pos - 0.3 * inch

        # Detect problem type and get configuration
        if equations and isinstance(equations[0], SystemProblem):
            problem_type = 'system_of_equations'
            is_system = True
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = False
            is_substitution = False
        elif equations and (isinstance(equations[0], InequalityProblem) or isinstance(equations[0], CompoundInequalityProblem)):
            problem_type = 'inequality'
            is_system = False
            is_inequality = True
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = False
            is_substitution = False
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
            is_graphing = False
        elif equations and isinstance(equations[0], WordProblem):
            problem_type = 'word_problems'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = True
            is_multistep = False
            is_graphing = False
        elif equations and isinstance(equations[0], MultiStepEquation):
            problem_type = 'multistep_equations'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = True
            is_graphing = False
            is_evaluating = False
            is_substitution = False
        elif equations and isinstance(equations[0], EvaluatingProblem):
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = True
            is_substitution = False
        elif equations and isinstance(equations[0], SubstitutionProblem):
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = False
            is_substitution = True
        elif equations and (isinstance(equations[0], GraphingPointsProblem) or
                           isinstance(equations[0], GraphingLineProblem) or
                           isinstance(equations[0], SlopeInterceptProblem) or
                           isinstance(equations[0], PointSlopeProblem) or
                           isinstance(equations[0], StandardFormProblem)):
            # Determine specific problem type
            if isinstance(equations[0], GraphingPointsProblem):
                problem_type = 'graphing_points'
            elif isinstance(equations[0], GraphingLineProblem):
                problem_type = 'graphing_lines'
            elif isinstance(equations[0], SlopeInterceptProblem):
                problem_type = 'slope_intercept'
            elif isinstance(equations[0], PointSlopeProblem):
                problem_type = 'point_slope'
            else:  # StandardFormProblem
                problem_type = 'standard_form'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
            is_evaluating = False
            is_substitution = False
        elif equations and isinstance(equations[0], GraphingSystemProblem):
            problem_type = 'graphing_systems'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
            is_evaluating = False
            is_substitution = False
        elif equations and isinstance(equations[0], ParabolaGraphingProblem):
            problem_type = 'graphing_parabolas'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
            is_evaluating = False
            is_substitution = False
        else:
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = False
            is_substitution = False

        config = get_config(problem_type)

        # Draw instructions below title in italics (universal for all worksheets)
        y_pos = instructions_y_pos
        # Use Helvetica-Oblique for italics (Lexend doesn't have italic variant)
        c.setFont("Helvetica-Oblique", 11)

        # Use instructions from config
        instructions_text = config.instructions if hasattr(config, 'instructions') else "Solve each problem."
        c.drawCentredString(width / 2, y_pos, instructions_text)

        # Draw problems - use Lexend
        y_pos -= 0.4 * inch
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
            # Calculate actual number of rows needed (2 columns)
            num_rows = (problems_per_page + 1) // 2  # Ceiling division for 2-column layout
            problems_per_column = num_rows  # Each column gets this many problems
        elif is_graphing:
            problems_per_column = 2  # 2 columns × 2 rows
            num_rows = 2  # 2 rows for spacing calculation (not problems per column)
        elif problems_per_page == 8:
            # For any 8-problem worksheet, use 2-column layout with 4 rows
            # This gives the same compact spacing as inequalities
            num_rows = 4  # 4 rows for spacing calculation
            problems_per_column = 4  # Each column gets 4 problems
        else:  # linear equations with more than 8 problems
            problems_per_column = 5  # First two columns have 5 problems
            num_rows = 5  # 5 rows for spacing calculation

        # Calculate dynamic spacing based on number of rows
        # For 2-column layouts, we need spacing between rows, not between all problems
        actual_problems_first_column = min(problems_per_page, problems_per_column)
        spacing = self._calculate_dynamic_spacing(
            problem_type,
            num_rows,
            header_end,
            footer_start
        )

        x_start = 1 * inch
        y_start = y_pos

        for idx, equation in enumerate(equations[:problems_per_page]):
            # Layout for different problem types - LEFT TO RIGHT ordering
            if is_inequality:
                # Inequalities: 2 columns x 4 rows (left-to-right: 1,2 in row 1, 3,4 in row 2, etc.)
                row = idx // 2
                col = idx % 2
                if col == 0:
                    x_start = 1 * inch
                    if row == 0:
                        y_pos = y_start
                    else:
                        y_pos = y_start - (row * spacing)
                else:
                    x_start = 4.25 * inch
                    # y_pos stays same as left column
            elif is_system:
                # Systems: 2 columns x 4 rows (left-to-right)
                row = idx // 2
                col = idx % 2
                if col == 0:
                    x_start = 1 * inch
                    if row == 0:
                        y_pos = y_start
                    else:
                        y_pos = y_start - (row * spacing)
                else:
                    x_start = 4.25 * inch
                    # y_pos stays same as left column
            elif is_graphing:
                # Graphing: 2 columns x 2 rows (left-to-right: 1,2 in row 1, 3,4 in row 2)
                row = idx // 2
                col = idx % 2
                if col == 0:
                    x_start = 1 * inch
                    if row == 0:
                        y_pos = y_start
                    else:
                        y_pos = y_start - (row * spacing)
                else:
                    x_start = 4.25 * inch
                    # y_pos stays same as left column
            elif is_word_problem:
                # Word problems: single column layout (one problem per row)
                x_start = 1 * inch
                if idx == 0:
                    y_pos = y_start
                else:
                    y_pos -= spacing
            else:
                # Regular equations: 2 columns layout with left-to-right ordering
                # Problems fill left-to-right: 1,2 in row 1, 3,4 in row 2, etc.
                if problems_per_page == 8:
                    # For 8 problems: use 2 columns x 4 rows (same as inequalities)
                    row = idx // 2
                    col = idx % 2
                    if col == 0:
                        x_start = 1 * inch
                    else:
                        x_start = 4.5 * inch
                    y_pos = y_start - (row * spacing)
                else:
                    # For more than 8 problems (typically 10-15): use 2 columns x 5 rows
                    # After 10 problems (5 rows x 2 columns), continue at top of page below the first set
                    if idx < 10:
                        # First 10 problems: 2 columns x 5 rows
                        row = idx // 2
                        col = idx % 2
                        if col == 0:
                            x_start = 1 * inch
                        else:
                            x_start = 4.5 * inch
                        y_pos = y_start - (row * spacing)
                    else:
                        # Problems 11-15: continue below in left column
                        adjusted_idx = idx - 10
                        row = adjusted_idx
                        x_start = 1 * inch
                        y_pos = y_start - ((5 + row) * spacing)

            # Problem number and equation text - use Lexend
            try:
                c.setFont("Lexend", 12)
            except:
                c.setFont("Helvetica", 12)

            if is_inequality:
                # For inequalities: display equation as plain text next to problem number
                # Convert LaTeX to plain text
                latex = self._get_problem_latex(equation)
                plain_text = latex.replace('\\leq', '≤').replace('\\geq', '≥').replace('\\text{ or }', ' or ').replace('\\', '')
                c.drawString(x_start, y_pos, f"{start_problem_number + idx}. {plain_text}")
            elif is_system:
                # For systems: display both equations as plain text
                # Convert LaTeX to plain text
                if isinstance(equation, (SubstitutionSystemProblem, EliminationSystemProblem)):
                    eq1_plain = getattr(equation, 'equation1', getattr(equation, 'equation1_latex', '')).replace('\\', '')
                    eq2_plain = getattr(equation, 'equation2', getattr(equation, 'equation2_latex', '')).replace('\\', '')
                else:
                    eq1_plain = equation.equation1_latex.replace('\\', '')
                    eq2_plain = equation.equation2_latex.replace('\\', '')
                c.drawString(x_start, y_pos, f"{start_problem_number + idx}. {eq1_plain}")
                c.drawString(x_start + 0.25 * inch, y_pos - 0.25 * inch, eq2_plain)
            elif is_property:
                # For properties: display equation with proper fraction rendering
                c.setFont('Lexend', 12)
                c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")
                # Draw equation with fractions properly rendered
                latex = self._get_problem_latex(equation)
                width_used, height_used = self._draw_equation_with_fractions(c, latex, x_start + 0.25 * inch, y_pos, 12, max_width=3.0 * inch)
                c.drawString(x_start, y_pos - 0.35 * inch, "Property:")
            elif is_word_problem or hasattr(equation, 'problem_text'):
                # For word problems: display the problem text with wrapping
                # Draw problem number first
                c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")
                # Wrap and draw the problem text (full page width minus margins)
                problem_text = getattr(equation, 'problem_text', self._get_problem_latex(equation))
                text_end_y = self._wrap_text(c, problem_text, x_start + 0.25 * inch, y_pos, 6.0, line_height=0.18)
                # Add blank lines for students to write equation and solve
                c.drawString(x_start + 0.25 * inch, text_end_y - 0.15 * inch, "Equation: _______________________")
                c.drawString(x_start + 0.25 * inch, text_end_y - 0.4 * inch, "Solution: _______________________")
            elif is_graphing:
                # For graphing problems: display coordinate plane
                c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")

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
                    # For systems: display both equations as aligned LaTeX image
                    try:
                        system_img = self.render_system_to_image(equation.equation1_latex, equation.equation2_latex, 21)
                        c.drawImage(
                            system_img,
                            x_start + 0.25 * inch,
                            y_pos - 0.25 * inch,
                            width=2.5 * inch,
                            height=0.6 * inch,
                            preserveAspectRatio=True,
                            mask='auto'
                        )
                        text_y = y_pos - 0.85 * inch
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
                # For regular equations: check if they have fractions or are text-heavy
                # First convert LaTeX symbols to Unicode BEFORE stripping backslashes
                plain_text = equation.latex
                # Convert math symbols to Unicode equivalents
                plain_text = re.sub(r'\\sqrt\[3\]\{([^}]+)\}', r'∛\1', plain_text)  # Cube root
                plain_text = re.sub(r'\\sqrt\{([^}]+)\}', r'√\1', plain_text)  # Square root
                plain_text = plain_text.replace('\\pi', 'π')  # Pi
                plain_text = plain_text.replace('\\approx', '≈')  # Approximately
                plain_text = plain_text.replace('\\cdot', '·')  # Middle dot
                plain_text = plain_text.replace('\\times', '×')  # Multiplication
                plain_text = plain_text.replace('\\lt', '<')  # Less than
                plain_text = plain_text.replace('\\gt', '>')  # Greater than
                plain_text = plain_text.replace('\\leq', '≤')  # Less than or equal
                plain_text = plain_text.replace('\\geq', '≥')  # Greater than or equal
                plain_text = plain_text.replace('\\left', '')  # Remove sizing commands
                plain_text = plain_text.replace('\\right', '')
                # Now remove remaining backslashes
                plain_text = plain_text.replace('\\', '')
                # Remove text{} wrappers: text{content} -> content
                plain_text = re.sub(r'text\{([^}]*)\}', r'\1', plain_text)

                # Check if this is a text-heavy problem that needs wrapping
                text_indicators = ['If ', 'Is ', 'Find ', 'Which ', 'Verify', 'Input:', 'Rule:', 'Output:', 'Evaluate', 'Between ', 'Approximate ', 'Order ']
                needs_wrapping = any(indicator in plain_text for indicator in text_indicators)

                if needs_wrapping:
                    # Text-heavy problem: draw number, then wrap text
                    # For text-heavy, convert fractions to slash notation
                    plain_text = re.sub(r'frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', plain_text)
                    c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")
                    # Wrap text to fit column width (3.0 inches for 3-column layout)
                    self._wrap_text(c, plain_text, x_start + 0.25 * inch, y_pos, 3.0, line_height=0.18)
                else:
                    # Simple equation: draw with proper fraction rendering
                    # Note: Equations use same 12pt font as problem numbers (not 21pt)
                    c.setFont('Lexend', 12)
                    c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")
                    # Draw equation with fractions (using 12pt to match other simple equations)
                    # Pass max_width of 3.0 inches to prevent overflow
                    width_used, height_used = self._draw_equation_with_fractions(c, equation.latex, x_start + 0.25 * inch, y_pos, 12, max_width=3.0 * inch)

            # Render number line for inequalities only
            if is_inequality:
                try:
                    # Inequality: use worksheet image (blank number line)
                    img = ImageReader(equation.worksheet_image)

                    # Number line width - slightly shorter than full column
                    numberline_width = 3.5 * inch
                    # Calculate height based on aspect ratio (8" wide x 1.2" tall for number line only)
                    natural_height = (1.2 / 8.0) * numberline_width
                    # Position number line below the equation text (moved 0.25" closer)
                    c.drawImage(
                        img,
                        x_start - 0.15 * inch,  # Moved 0.25" left from previous 0.1"
                        y_pos - 0.10 * inch - natural_height,  # Below equation text, 0.25" closer than before
                        width=numberline_width,
                        height=natural_height,
                        preserveAspectRatio=True
                    )
                except Exception as e:
                    print(f"Warning: Number line rendering failed: {e}")

            # Only decrement y_pos for specific layouts
            # For 2-column layouts (systems, inequalities, graphing), don't decrement here
            # The row calculation handles y positioning
            if not (is_system or is_inequality or is_graphing or is_word_problem):
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
            base_dir = get_base_path()
            logo_path = os.path.join(base_dir, 'src', 'icons', 'FreshMath_V3', 'Black', 'FreshMath_Black_Secondary.png')

            if os.path.exists(logo_path):
                # Logo size (0.6 inches)
                logo_size = 0.6 * inch
                # Position in bottom right corner with some margin
                x_pos = width - 1.2 * inch
                y_pos = 0.4 * inch

                # Draw the logo
                c.drawImage(logo_path, x_pos, y_pos, width=logo_size, height=logo_size,
                           preserveAspectRatio=True, mask='auto')
        except Exception as e:
            # Silently fail if logo can't be loaded
            print(f"Note: Could not load Fresh Math logo: {e}")

    def _draw_answer_key_page(self, c: canvas.Canvas, equations: List[Union[Equation, SystemProblem, InequalityProblem, CompoundInequalityProblem, PropertyProblem, WordProblem, MultiStepEquation]],
                             title: str, width: float, height: float, start_problem_number: int = 1):
        """Draw the answer key page with same layout as worksheet, answers in red."""
        # Header with logo in top right (matching worksheet page)
        y_pos = height - 0.5 * inch

        # Draw QR code in top left corner
        try:
            base_dir = get_base_path()
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

        # Draw logo in top right (0.6 inches)
        try:
            base_dir = get_base_path()
            logo_path = os.path.join(base_dir, 'src', 'icons', 'FreshMath_V3',
                                     'Black', 'FreshMath_Black_Secondary.png')

            if os.path.exists(logo_path):
                logo_size = 0.6 * inch  # 0.6 x 0.6 inches
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

        # Use the full title as provided
        display_title = title

        c.drawCentredString(width / 2, y_pos, f"{display_title} - Answer Key")

        # Detect problem type and get configuration
        if equations and isinstance(equations[0], SystemProblem):
            problem_type = 'system_of_equations'
            is_system = True
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = False
            is_substitution = False
        elif equations and (isinstance(equations[0], InequalityProblem) or isinstance(equations[0], CompoundInequalityProblem)):
            problem_type = 'inequality'
            is_system = False
            is_inequality = True
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = False
            is_substitution = False
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
            is_graphing = False
        elif equations and isinstance(equations[0], WordProblem):
            problem_type = 'word_problems'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = True
            is_multistep = False
            is_graphing = False
        elif equations and isinstance(equations[0], MultiStepEquation):
            problem_type = 'multistep_equations'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = True
            is_graphing = False
            is_evaluating = False
            is_substitution = False
        elif equations and isinstance(equations[0], EvaluatingProblem):
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = True
            is_substitution = False
        elif equations and isinstance(equations[0], SubstitutionProblem):
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = False
            is_substitution = True
        elif equations and (isinstance(equations[0], GraphingPointsProblem) or
                           isinstance(equations[0], GraphingLineProblem) or
                           isinstance(equations[0], SlopeInterceptProblem) or
                           isinstance(equations[0], PointSlopeProblem) or
                           isinstance(equations[0], StandardFormProblem)):
            # Determine specific problem type
            if isinstance(equations[0], GraphingPointsProblem):
                problem_type = 'graphing_points'
            elif isinstance(equations[0], GraphingLineProblem):
                problem_type = 'graphing_lines'
            elif isinstance(equations[0], SlopeInterceptProblem):
                problem_type = 'slope_intercept'
            elif isinstance(equations[0], PointSlopeProblem):
                problem_type = 'point_slope'
            else:  # StandardFormProblem
                problem_type = 'standard_form'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
            is_evaluating = False
            is_substitution = False
        elif equations and isinstance(equations[0], GraphingSystemProblem):
            problem_type = 'graphing_systems'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
            is_evaluating = False
            is_substitution = False
        elif equations and isinstance(equations[0], ParabolaGraphingProblem):
            problem_type = 'graphing_parabolas'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = True
            is_evaluating = False
            is_substitution = False
        else:
            problem_type = 'linear_equation'
            is_system = False
            is_inequality = False
            is_property = False
            is_word_problem = False
            is_multistep = False
            is_graphing = False
            is_evaluating = False
            is_substitution = False

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
            # Calculate actual number of rows needed (2 columns)
            num_rows_answer = (problems_per_page + 1) // 2  # Ceiling division for 2-column layout
            problems_per_column = num_rows_answer  # Each column gets this many problems
        elif is_graphing:
            problems_per_column = 2  # 2 columns × 2 rows
            num_rows_answer = 2
        else:  # linear equations
            problems_per_column = 5  # First two columns have 5 problems
            num_rows_answer = 5

        # Calculate dynamic spacing for rows (same as worksheet)
        spacing = self._calculate_dynamic_spacing(
            problem_type,
            num_rows_answer,
            header_end,
            footer_start
        )

        x_start = 1 * inch
        y_start = y_pos

        if is_inequality:
            # For inequalities: show number lines with solutions in 2-column layout
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 2 columns x 4 rows (TOP-TO-BOTTOM: 1,3,5,7 in col 1, 2,4,6,8 in col 2)
                col = idx // problems_per_column
                row = idx % problems_per_column

                if col == 0:
                    x_start = 1 * inch
                else:
                    x_start = 4.25 * inch

                y_pos = y_start - (row * spacing)

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
                plain_text = equation.latex.replace('\\leq', '≤').replace('\\geq', '≥').replace('\\text{ or }', ' or ').replace('\\', '')
                c.drawString(x_start, y_pos, f"{start_problem_number + idx}. {plain_text}")

                # Render solved number line with solution
                try:
                    # Use answer image (number line with solution)
                    img = ImageReader(equation.answer_image)

                    # Draw number line (moved 0.25" closer to equation text)
                    numberline_width = 3.5 * inch
                    natural_height = (1.2 / 8.0) * numberline_width
                    image_bottom = y_pos - 0.10 * inch - natural_height
                    c.drawImage(
                        img,
                        x_start - 0.15 * inch,  # Moved 0.25" left from previous 0.1"
                        image_bottom,
                        width=numberline_width,
                        height=natural_height,
                        preserveAspectRatio=True
                    )

                    # Draw algebraic solution below the number line in RED (only for simple inequalities)
                    if hasattr(equation, 'solution'):
                        # Simple inequality - show algebraic solution
                        try:
                            c.setFont("Lexend", 12)
                        except:
                            c.setFont("Helvetica", 12)
                        ineq_symbol = symbol_map.get(equation.inequality_type, equation.inequality_type)
                        solution = self._get_problem_solution(equation)
                        if isinstance(solution, (int, float)):
                            if solution == int(solution):
                                solution_str = f"x {ineq_symbol} {int(solution)}"
                            else:
                                solution_str = f"x {ineq_symbol} {solution:.2f}"
                        else:
                            solution_str = str(solution)

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
                # Layout: 2 columns x 4 rows (LEFT-TO-RIGHT: 1,2 in row 1, 3,4 in row 2, etc.)
                row = idx // 2
                col = idx % 2

                # Calculate position based on row and column
                if col == 0:
                    x_start = 1 * inch
                else:
                    x_start = 4.25 * inch

                # y_pos is calculated from row position (same for both columns in the row)
                y_pos = y_start - (row * spacing)

                # Display problem number and both equations as plain text
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                eq1_plain = equation.equation1_latex.replace('\\', '')
                eq2_plain = equation.equation2_latex.replace('\\', '')
                c.drawString(x_start, y_pos, f"{start_problem_number + idx}. {eq1_plain}")
                c.drawString(x_start + 0.25 * inch, y_pos - 0.25 * inch, eq2_plain)

                # Display answer in RED below the equations
                c.setFillColorRGB(1, 0, 0)  # Red color
                solution = self._get_problem_solution(equation)
                c.drawString(x_start + 0.25 * inch, y_pos - 0.55 * inch, str(solution))
                c.setFillColorRGB(0, 0, 0)  # Reset to black

        elif is_property:
            # For properties: 2 columns x 5 rows layout with answers in red
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 2 columns x 5 rows (LEFT-TO-RIGHT: 1,2 in row 1, 3,4 in row 2, etc.)
                row = idx // 2
                col = idx % 2

                # Calculate position based on row and column
                if col == 0:
                    x_start = 1 * inch
                else:
                    x_start = 4.25 * inch

                # y_pos is calculated from row position (same for both columns in the row)
                y_pos = y_start - (row * spacing)

                # Display problem equation with proper fraction rendering
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")
                # Draw equation with fractions properly rendered
                width_used, height_used = self._draw_equation_with_fractions(c, equation.latex, x_start + 0.25 * inch, y_pos, 12, max_width=3.0 * inch)

                # Display property name and solution in RED
                c.setFillColorRGB(1, 0, 0)  # Red color
                property_type = getattr(equation, 'property_type', 'Unknown')
                # Abbreviate property types to fit in column
                property_abbrev = {
                    'addition': 'Add',
                    'subtraction': 'Sub',
                    'multiplication': 'Mult',
                    'division': 'Div',
                    'combined (subtraction then division)': 'Sub+Div',
                    'combined (addition then division)': 'Add+Div'
                }
                prop_text = property_abbrev.get(property_type.lower(), property_type)
                # Draw property name and solution on separate lines to avoid overflow
                c.drawString(x_start, y_pos - 0.35 * inch, f"{prop_text} Property")
                c.drawString(x_start, y_pos - 0.55 * inch, f"x = {equation.solution}")
                c.setFillColorRGB(0, 0, 0)  # Reset to black

        elif is_word_problem:
            # For word problems: single column layout with answers in red
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Display problem text with wrapping
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                # Draw problem number first
                c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")
                # Wrap and draw the problem text (full page width minus margins)
                problem_text = getattr(equation, 'problem_text', equation.latex)
                text_end_y = self._wrap_text(c, problem_text, x_start + 0.25 * inch, y_pos, 6.0, line_height=0.18)

                # Display equation and solution in RED
                c.setFillColorRGB(1, 0, 0)  # Red color
                c.drawString(x_start + 0.25 * inch, text_end_y - 0.15 * inch, f"Equation: {equation.equation}")
                c.drawString(x_start + 0.25 * inch, text_end_y - 0.4 * inch, f"Solution: x = {equation.solution}")
                c.setFillColorRGB(0, 0, 0)  # Reset to black

                # Update y_pos to be below the answer we just drew, with additional spacing
                y_pos = text_end_y - 0.6 * inch  # Position below solution with extra padding

        elif is_graphing:
            # For graphing problems: 2 columns x 2 rows layout with plotted points
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 2 columns x 2 rows (LEFT-TO-RIGHT: 1,2 in row 1, 3,4 in row 2)
                row = idx // 2
                col = idx % 2
                if col == 0:
                    x_start = 1 * inch
                    if row == 0:
                        y_pos = y_start
                    else:
                        y_pos = y_start - (row * spacing)
                else:
                    x_start = 4.25 * inch
                    # y_pos stays same as left column

                # Display problem number and points
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")

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
                    # For systems: display both equations as aligned LaTeX image
                    try:
                        system_img = self.render_system_to_image(equation.equation1_latex, equation.equation2_latex, 21)
                        c.drawImage(
                            system_img,
                            x_start + 0.25 * inch,
                            y_pos - 0.25 * inch,
                            width=2.5 * inch,
                            height=0.6 * inch,
                            preserveAspectRatio=True,
                            mask='auto'
                        )
                        text_y = y_pos - 0.85 * inch
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

                # Only decrement y_pos after finishing a row (when we're in the right column)
                if col == 1:
                    y_pos -= spacing

        else:
            # For linear equations: 2 columns layout with left-to-right ordering (matching worksheet)
            for idx, equation in enumerate(equations[:problems_per_page]):
                # Layout: 2 columns with left-to-right ordering (same as worksheet)
                # Problems fill left-to-right: 1,2 in row 1, 3,4 in row 2, etc.
                # After 10 problems (5 rows x 2 columns), continue at top of page below the first set
                if idx < 10:
                    # First 10 problems: 2 columns x 5 rows
                    row = idx // 2
                    col = idx % 2
                    if col == 0:
                        x_start = 1 * inch
                    else:
                        x_start = 4.5 * inch
                    y_pos = y_start - (row * spacing)
                else:
                    # Problems 11-15: continue below in left column
                    adjusted_idx = idx - 10
                    row = adjusted_idx
                    x_start = 1 * inch
                    y_pos = y_start - ((5 + row) * spacing)

                # Display problem number and equation as plain text
                try:
                    c.setFont("Lexend", 12)
                except:
                    c.setFont("Helvetica", 12)

                # First convert LaTeX symbols to Unicode BEFORE stripping backslashes
                plain_text = equation.latex
                # Convert math symbols to Unicode equivalents
                plain_text = re.sub(r'\\sqrt\[3\]\{([^}]+)\}', r'∛\1', plain_text)  # Cube root
                plain_text = re.sub(r'\\sqrt\{([^}]+)\}', r'√\1', plain_text)  # Square root
                plain_text = plain_text.replace('\\pi', 'π')  # Pi
                plain_text = plain_text.replace('\\approx', '≈')  # Approximately
                plain_text = plain_text.replace('\\cdot', '·')  # Middle dot
                plain_text = plain_text.replace('\\times', '×')  # Multiplication
                plain_text = plain_text.replace('\\lt', '<')  # Less than
                plain_text = plain_text.replace('\\gt', '>')  # Greater than
                plain_text = plain_text.replace('\\leq', '≤')  # Less than or equal
                plain_text = plain_text.replace('\\geq', '≥')  # Greater than or equal
                plain_text = plain_text.replace('\\left', '')  # Remove sizing commands
                plain_text = plain_text.replace('\\right', '')
                # Now remove remaining backslashes
                plain_text = plain_text.replace('\\', '')
                # Remove text{} wrappers: text{content} -> content
                plain_text = re.sub(r'text\{([^}]*)\}', r'\1', plain_text)

                # Check if this is a text-heavy problem that needs wrapping
                text_indicators = ['If ', 'Is ', 'Find ', 'Which ', 'Verify', 'Input:', 'Rule:', 'Output:', 'Evaluate', 'Between ', 'Approximate ', 'Order ']
                needs_wrapping = any(indicator in plain_text for indicator in text_indicators)

                if needs_wrapping:
                    # Text-heavy problem: draw number, then wrap text
                    # Convert fractions to slash notation for text-heavy problems
                    plain_text = re.sub(r'frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', plain_text)
                    c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")
                    # Wrap text to fit column width (3.0 inches for 3-column layout)
                    text_end_y = self._wrap_text(c, plain_text, x_start + 0.25 * inch, y_pos, 3.0, line_height=0.18)

                    # Display answer in RED below wrapped text
                    c.setFillColorRGB(1, 0, 0)  # Red color
                    # Check if solution is a string (for new generators)
                    if isinstance(equation.solution, str):
                        solution_str = equation.solution
                    # Check if this is Variables worksheet - handle all Variables problems first
                    elif "Variables" in title:
                        # For Variables, use steps[0] if available (text answers), otherwise show numeric value
                        if hasattr(equation, 'steps') and equation.steps and equation.solution == 0:
                            solution_str = equation.steps[0]  # Use text answer from steps
                        elif equation.solution == int(equation.solution):
                            solution_str = str(int(equation.solution))
                        else:
                            solution_str = f"{equation.solution:.2f}"
                    # Check if this is a "What Are Solutions?" worksheet
                    elif "What Are Solutions?" in title or "Solutions" in title:
                        # Format for solutions worksheet: just show the number
                        if equation.solution == 999:
                            solution_str = "infinite"
                        elif equation.solution == 0:
                            solution_str = "zero"
                        elif equation.solution == 1:
                            solution_str = "one"
                        else:
                            solution_str = str(int(equation.solution))
                    # Check if this is an expression problem (exponents, evaluating, etc.) - just show the value
                    elif "Exponent" in title or "Evaluating" in title or "Substitution" in title:
                        if equation.solution == int(equation.solution):
                            solution_str = str(int(equation.solution))
                        else:
                            solution_str = f"{equation.solution:.2f}"
                    # Check if this is a text-based problem (like combining like terms)
                    elif equation.solution == 0 and hasattr(equation, 'steps') and equation.steps:
                        solution_str = equation.steps[0]  # Use text answer from steps
                    elif equation.solution == int(equation.solution):
                        solution_str = f"x = {int(equation.solution)}"
                    else:
                        solution_str = f"x = {equation.solution:.2f}"

                    # Use text wrapping for long answers (especially variable problems)
                    if len(solution_str) > 30:
                        # Use smaller font for long variable answers
                        c.setFont('Lexend', 9)
                        self._wrap_text(c, solution_str, x_start + 0.25 * inch, text_end_y - 0.15 * inch, max_width=3.0, line_height=0.13)
                        c.setFont('Lexend', 12)  # Reset font
                    else:
                        c.drawString(x_start + 0.25 * inch, text_end_y - 0.15 * inch, solution_str)
                    c.setFillColorRGB(0, 0, 0)  # Reset to black
                else:
                    # Simple equation: draw with proper fraction rendering
                    # Note: Equations use same 12pt font as problem numbers (not 21pt)
                    c.setFont('Lexend', 12)
                    c.drawString(x_start, y_pos, f"{start_problem_number + idx}.")
                    # Draw equation with fractions (using 12pt to match other simple equations)
                    # Pass max_width of 3.0 inches to prevent overflow
                    width_used, height_used = self._draw_equation_with_fractions(c, equation.latex, x_start + 0.25 * inch, y_pos, 12, max_width=3.0 * inch)

                    # Display answer in RED below the equation
                    # Account for height used by equation if it wrapped
                    answer_y = y_pos - 0.25 * inch - height_used
                    c.setFillColorRGB(1, 0, 0)  # Red color
                    # Check if solution is a string (for new generators)
                    if isinstance(equation.solution, str):
                        solution_str = equation.solution
                    # Check if this is Variables worksheet - handle all Variables problems first
                    elif "Variables" in title:
                        # For Variables, use steps[0] if available (text answers), otherwise show numeric value
                        if hasattr(equation, 'steps') and equation.steps and equation.solution == 0:
                            solution_str = equation.steps[0]  # Use text answer from steps
                        elif equation.solution == int(equation.solution):
                            solution_str = str(int(equation.solution))
                        else:
                            solution_str = f"{equation.solution:.2f}"
                    # Check if this is a "What Are Solutions?" worksheet
                    elif "What Are Solutions?" in title or "Solutions" in title:
                        # Format for solutions worksheet: just show the number
                        if equation.solution == 999:
                            solution_str = "infinite"
                        elif equation.solution == 0:
                            solution_str = "zero"
                        elif equation.solution == 1:
                            solution_str = "one"
                        else:
                            solution_str = str(int(equation.solution))
                    # Check if this is an expression problem (exponents, evaluating, etc.) - just show the value
                    elif "Exponent" in title or "Evaluating" in title or "Substitution" in title:
                        if equation.solution == int(equation.solution):
                            solution_str = str(int(equation.solution))
                        else:
                            solution_str = f"{equation.solution:.2f}"
                    # Check if this is a text-based problem (like combining like terms)
                    elif equation.solution == 0 and hasattr(equation, 'steps') and equation.steps:
                        solution_str = equation.steps[0]  # Use text answer from steps
                    elif equation.solution == int(equation.solution):
                        solution_str = f"x = {int(equation.solution)}"
                    else:
                        solution_str = f"x = {equation.solution:.2f}"

                    # Use text wrapping for long answers (especially variable problems)
                    if len(solution_str) > 30:
                        # Use smaller font for long variable answers
                        c.setFont('Lexend', 9)
                        self._wrap_text(c, solution_str, x_start + 0.25 * inch, answer_y, max_width=3.0, line_height=0.13)
                        c.setFont('Lexend', 12)  # Reset font
                    else:
                        c.drawString(x_start + 0.25 * inch, answer_y, solution_str)
                    c.setFillColorRGB(0, 0, 0)  # Reset to black

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
