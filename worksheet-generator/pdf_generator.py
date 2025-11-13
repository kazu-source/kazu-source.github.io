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
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from equation_generator import Equation
from systems_generator import SystemProblem
from inequalities_generator import InequalityProblem
from worksheet_config import get_config, ProblemTypeConfig
from typing import Union


class PDFWorksheetGenerator:
    """Generates PDF worksheets with LaTeX-rendered equations."""

    def __init__(self):
        """Initialize the PDF generator."""
        # Configure matplotlib for LaTeX rendering
        plt.rcParams['mathtext.fontset'] = 'cm'  # Computer Modern font
        plt.rcParams['font.size'] = 14

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
        Render a system of equations as two lines with a brace.

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
        ax.text(0.12, 0.70, f'${eq1}$', fontsize=fontsize, verticalalignment='center')
        ax.text(0.12, 0.30, f'${eq2}$', fontsize=fontsize, verticalalignment='center')

        # Add a simple brace using text (not LaTeX)
        ax.text(0.02, 0.50, '{', fontsize=fontsize*3, verticalalignment='center', family='monospace')

        # Save to bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.1,
                    transparent=False, facecolor='white')
        buf.seek(0)
        plt.close(fig)

        return ImageReader(buf)

    def render_inequality_with_numberline(self, latex_str: str, min_val: int, max_val: int,
                                         solution: float, is_solution_left: bool,
                                         inequality_type: str, fontsize: int = 18) -> ImageReader:
        """
        Render an inequality with a number line showing the solution.

        Args:
            latex_str: Inequality in LaTeX format
            min_val: Minimum value on number line
            max_val: Maximum value on number line
            solution: The boundary value
            is_solution_left: True if solution is to the left (x < value)
            inequality_type: '<', '>', '<=', '>='
            fontsize: Font size for inequality

        Returns:
            ImageReader object for reportlab
        """
        # Create figure with inequality and number line
        fig = plt.figure(figsize=(4, 1.2))
        fig.patch.set_visible(False)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')

        # Render inequality at top
        ax.text(0.05, 0.75, f'${latex_str}$', fontsize=fontsize, verticalalignment='center')

        # Draw number line
        line_y = 0.35
        line_start_x = 0.1
        line_end_x = 0.9

        # Main line
        ax.plot([line_start_x, line_end_x], [line_y, line_y], 'k-', linewidth=2)

        # Calculate tick positions
        num_values = max_val - min_val + 1
        tick_spacing = (line_end_x - line_start_x) / (num_values - 1)

        # Draw ticks and labels
        for i, val in enumerate(range(min_val, max_val + 1)):
            x_pos = line_start_x + i * tick_spacing
            # Draw tick mark
            ax.plot([x_pos, x_pos], [line_y - 0.03, line_y + 0.03], 'k-', linewidth=2)
            # Draw label
            ax.text(x_pos, line_y - 0.12, str(val), fontsize=12,
                   ha='center', va='top', fontweight='bold')

        # Highlight the solution on number line
        solution_idx = solution - min_val
        solution_x = line_start_x + solution_idx * tick_spacing

        # Draw solution point (open or closed circle)
        is_equal = inequality_type in ['\\leq', '\\geq']
        if is_equal:
            # Closed circle (larger and more visible)
            circle = plt.Circle((solution_x, line_y), 0.025, color='blue', fill=True)
        else:
            # Open circle (larger and thicker line)
            circle = plt.Circle((solution_x, line_y), 0.025, color='blue', fill=False, linewidth=3)
        ax.add_patch(circle)

        # Draw arrow showing solution region (thicker)
        arrow_start = solution_x
        if is_solution_left:
            # Arrow pointing left
            arrow_end = line_start_x
            ax.annotate('', xy=(arrow_end, line_y), xytext=(arrow_start - 0.03, line_y),
                       arrowprops=dict(arrowstyle='->', color='blue', lw=4))
        else:
            # Arrow pointing right
            arrow_end = line_end_x
            ax.annotate('', xy=(arrow_end, line_y), xytext=(arrow_start + 0.03, line_y),
                       arrowprops=dict(arrowstyle='->', color='blue', lw=4))

        # Save to bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.1,
                    transparent=False, facecolor='white')
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
        # Title
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width / 2, height - 0.75 * inch, title)

        # Header fields
        c.setFont("Helvetica", 11)
        y_pos = height - 1.25 * inch
        c.drawString(1 * inch, y_pos, "Name: _________________________")
        c.drawString(4 * inch, y_pos, "Date: _____________")

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

        # Instructions
        y_pos -= 0.5 * inch
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(1 * inch, y_pos, config.instructions)

        # Draw problems
        y_pos -= 0.5 * inch
        c.setFont("Helvetica", 12)

        # Use configuration for layout
        problems_per_page = min(len(equations), config.problems_per_page)
        spacing = config.vertical_spacing * inch

        x_start = 1 * inch
        y_start = y_pos

        for idx, equation in enumerate(equations[:problems_per_page]):
            # Layout for systems vs equations
            if is_system:
                # Systems: single column or 2 columns depending on space
                if idx > 0 and idx % 4 == 0 and idx < 8:
                    x_start = 4.25 * inch
                    y_pos = y_start
            else:
                # Regular equations: 3 columns of 5
                if idx > 0 and idx % 5 == 0:
                    if idx == 5:
                        x_start = 4.5 * inch
                        y_pos = y_start
                    elif idx == 10:
                        x_start = 1 * inch
                        y_pos = y_start - 3.5 * inch

            # Problem number
            c.setFont("Helvetica", 11)
            c.drawString(x_start, y_pos, f"{idx + 1}.")

            # Render equation/system/inequality as image using configuration
            try:
                if is_inequality:
                    # Inequality: render with number line
                    img = self.render_inequality_with_numberline(
                        equation.latex,
                        equation.number_line_min,
                        equation.number_line_max,
                        equation.solution,
                        equation.is_solution_left,
                        equation.inequality_type,
                        fontsize=config.latex_fontsize
                    )
                elif is_system:
                    # Systems: render two equations with brace
                    img = self.render_system_to_image(
                        equation.equation1_latex,
                        equation.equation2_latex,
                        fontsize=config.latex_fontsize
                    )
                else:
                    # Single equation
                    img = self.render_latex_to_image(
                        equation.latex,
                        fontsize=config.latex_fontsize
                    )

                # Draw image with configured dimensions
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
                c.setFont("Courier", 9)
                if is_system:
                    c.drawString(x_start + 0.25 * inch, y_pos, equation.equation1_latex)
                    c.drawString(x_start + 0.25 * inch, y_pos - 0.2 * inch, equation.equation2_latex)
                else:
                    c.drawString(x_start + 0.25 * inch, y_pos, equation.latex)
                print(f"Warning: LaTeX rendering failed: {e}")

            y_pos -= spacing

        # Footer
        c.setFont("Helvetica-Oblique", 8)
        c.drawCentredString(width / 2, 0.5 * inch,
                           f"Generated on {datetime.now().strftime('%B %d, %Y')}")

    def _draw_answer_key_page(self, c: canvas.Canvas, equations: List[Union[Equation, SystemProblem, InequalityProblem]],
                             title: str, width: float, height: float):
        """Draw the answer key page."""
        # Title
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width / 2, height - 0.75 * inch, f"{title} - Answer Key")

        # Answers
        y_pos = height - 1.5 * inch
        c.setFont("Helvetica", 11)

        # Check problem type
        is_system = equations and isinstance(equations[0], SystemProblem)
        is_inequality = equations and isinstance(equations[0], InequalityProblem)

        # Organize answers in columns
        col1_x = 1 * inch
        col2_x = 4 * inch
        col3_x = 6.5 * inch

        for idx, equation in enumerate(equations):
            # Determine column
            if idx % 3 == 0:
                x_pos = col1_x
            elif idx % 3 == 1:
                x_pos = col2_x
            else:
                x_pos = col3_x

            # Format solution based on type
            if is_inequality:
                # InequalityProblem - format with inequality symbol
                ineq_symbol = equation.inequality_type.replace('\\', '')  # Remove LaTeX escapes
                if equation.solution == int(equation.solution):
                    solution_str = f"x {ineq_symbol} {int(equation.solution)}"
                else:
                    solution_str = f"x {ineq_symbol} {equation.solution:.2f}"
            elif is_system:
                # SystemProblem has solution string already formatted
                solution_str = equation.solution
            else:
                # Equation object - format x value
                if equation.solution == int(equation.solution):
                    solution_str = f"x = {int(equation.solution)}"
                else:
                    solution_str = f"x = {equation.solution:.2f}"

            c.drawString(x_pos, y_pos, f"{idx + 1}. {solution_str}")

            # Move to next row after every 3 answers
            if idx % 3 == 2:
                y_pos -= 0.35 * inch

        # Footer
        c.setFont("Helvetica-Oblique", 8)
        c.drawCentredString(width / 2, 0.5 * inch,
                           f"Generated on {datetime.now().strftime('%B %d, %Y')}")


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
