"""
Generator for x and y intercepts worksheets.
Chapter 4: Linear Equations (Two Variables) - X and Y Intercepts
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from fractions import Fraction

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from graphing_utils import CoordinatePlane
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt


@dataclass
class InterceptsProblem:
    """Represents an x and y intercepts problem."""
    equation_type: str  # 'slope-intercept', 'standard', 'point-slope'
    equation_latex: str  # LaTeX string for the equation
    x_intercept: tuple  # (x, 0) or None if no x-intercept
    y_intercept: tuple  # (0, y) or None if no y-intercept
    x_intercept_latex: str  # LaTeX representation of x-intercept
    y_intercept_latex: str  # LaTeX representation of y-intercept
    difficulty: str  # easy, medium, hard, challenge
    worksheet_image: object  # PIL Image for worksheet (blank grid with equation)
    answer_image: object  # PIL Image for answer key (grid with line and intercepts marked)
    problem_latex: str  # LaTeX string for the problem
    answer_latex: str  # LaTeX string for the answer
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class InterceptsGenerator:
    """Generator for x and y intercepts problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def _format_number(self, num):
        """Format a number for display, handling fractions."""
        if isinstance(num, int):
            return str(num)
        elif isinstance(num, float):
            # Check if it's close to an integer
            if abs(num - round(num)) < 0.0001:
                return str(int(round(num)))
            # Try to convert to fraction
            frac = Fraction(num).limit_denominator(100)
            if frac.denominator == 1:
                return str(frac.numerator)
            else:
                return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"
        return str(num)

    def _calculate_intercepts(self, equation_type, params):
        """
        Calculate x and y intercepts from equation parameters.

        Args:
            equation_type: Type of equation ('slope-intercept', 'standard', etc.)
            params: Dictionary of equation parameters

        Returns:
            Tuple of (x_intercept, y_intercept, x_latex, y_latex)
        """
        if equation_type == 'slope-intercept':
            # y = mx + b
            m = params['slope']
            b = params['y_intercept']

            # Y-intercept is simply b
            y_int = (0, b)
            y_latex = f"(0, {self._format_number(b)})"

            # X-intercept: set y = 0, solve for x
            # 0 = mx + b => x = -b/m
            if m == 0:
                # Horizontal line
                if b == 0:
                    x_int = "all points on x-axis"
                    x_latex = "\\text{all points on x-axis}"
                else:
                    x_int = None
                    x_latex = "\\text{none}"
            else:
                x_val = -b / m
                x_int = (x_val, 0)
                x_latex = f"({self._format_number(x_val)}, 0)"

        elif equation_type == 'standard':
            # Ax + By = C
            A = params['A']
            B = params['B']
            C = params['C']

            # X-intercept: set y = 0
            if A == 0:
                x_int = None
                x_latex = "\\text{none}"
            else:
                x_val = C / A
                x_int = (x_val, 0)
                x_latex = f"({self._format_number(x_val)}, 0)"

            # Y-intercept: set x = 0
            if B == 0:
                y_int = None
                y_latex = "\\text{none}"
            else:
                y_val = C / B
                y_int = (0, y_val)
                y_latex = f"(0, {self._format_number(y_val)})"

        else:  # vertical line x = a
            a = params['x_value']
            x_int = (a, 0)
            x_latex = f"({a}, 0)"
            y_int = None
            y_latex = "\\text{none}"

        return x_int, y_int, x_latex, y_latex

    def _create_graph(self, equation_type, params, show_intercepts=False):
        """
        Create a coordinate plane with the line and optionally intercepts marked.

        Args:
            equation_type: Type of equation
            params: Equation parameters
            show_intercepts: Whether to mark the intercepts

        Returns:
            PIL Image object
        """
        plane = CoordinatePlane()
        fig, ax = plane.create_figure()

        # Plot the line
        if equation_type == 'slope-intercept':
            m = params['slope']
            b = params['y_intercept']
            if m != 0:
                plane.plot_line_from_equation(ax, slope=m, y_intercept=b, color='blue', linewidth=2)
            else:
                # Horizontal line
                ax.axhline(y=b, color='blue', linewidth=2)

        elif equation_type == 'standard':
            A = params['A']
            B = params['B']
            C = params['C']
            plane.plot_line_from_equation(ax, standard_form=(A, B, C), color='blue', linewidth=2)

        else:  # vertical line
            x_val = params['x_value']
            ax.axvline(x=x_val, color='blue', linewidth=2)

        # Mark intercepts if requested
        if show_intercepts:
            x_int, y_int, _, _ = self._calculate_intercepts(equation_type, params)

            if x_int and isinstance(x_int, tuple):
                plane.plot_point(ax, x_int[0], x_int[1],
                               label=f"x-int: ({self._format_number(x_int[0])}, 0)",
                               color='red', size=100)

            if y_int and isinstance(y_int, tuple):
                plane.plot_point(ax, y_int[0], y_int[1],
                               label=f"y-int: (0, {self._format_number(y_int[1])})",
                               color='green', size=100)

        # Convert to PIL Image
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        plt.close(fig)
        buffer.seek(0)
        image = Image.open(buffer)

        return image

    def generate_problem(self, difficulty: str) -> InterceptsProblem:
        """
        Generate a single intercepts problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            InterceptsProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> InterceptsProblem:
        """Generate easy intercepts problem (integer intercepts, slope-intercept form)."""
        # Use slope-intercept form with integer values
        slope = random.randint(1, 3) * random.choice([-1, 1])
        y_intercept = random.randint(-6, 6)

        # Ensure x-intercept is also an integer
        while y_intercept % slope != 0:
            slope = random.randint(1, 3) * random.choice([-1, 1])
            y_intercept = random.randint(-6, 6)

        equation_type = 'slope-intercept'
        params = {'slope': slope, 'y_intercept': y_intercept}

        # Format equation
        if slope == 1:
            equation_latex = f"y = x + {y_intercept}" if y_intercept >= 0 else f"y = x - {abs(y_intercept)}"
        elif slope == -1:
            equation_latex = f"y = -x + {y_intercept}" if y_intercept >= 0 else f"y = -x - {abs(y_intercept)}"
        else:
            equation_latex = f"y = {slope}x + {y_intercept}" if y_intercept >= 0 else f"y = {slope}x - {abs(y_intercept)}"

        if y_intercept == 0:
            equation_latex = f"y = {slope}x" if slope != 1 else "y = x"
            if slope == -1:
                equation_latex = "y = -x"

        x_int, y_int, x_latex, y_latex = self._calculate_intercepts(equation_type, params)

        problem_latex = f"Find the x-intercept and y-intercept of the line: ${equation_latex}$"
        answer_latex = f"x-intercept: ${x_latex}$, y-intercept: ${y_latex}$"

        return InterceptsProblem(
            equation_type=equation_type,
            equation_latex=equation_latex,
            x_intercept=x_int,
            y_intercept=y_int,
            x_intercept_latex=x_latex,
            y_intercept_latex=y_latex,
            difficulty='easy',
            worksheet_image=self._create_graph(equation_type, params, show_intercepts=False),
            answer_image=self._create_graph(equation_type, params, show_intercepts=True),
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_medium(self) -> InterceptsProblem:
        """Generate medium intercepts problem (standard form, fractional intercepts)."""
        # Use standard form Ax + By = C
        A = random.randint(1, 5) * random.choice([-1, 1])
        B = random.randint(1, 5) * random.choice([-1, 1])
        C = random.randint(1, 12) * random.choice([-1, 1])

        equation_type = 'standard'
        params = {'A': A, 'B': B, 'C': C}

        # Format equation
        equation_latex = f"{A}x + {B}y = {C}"
        if B < 0:
            equation_latex = f"{A}x - {abs(B)}y = {C}"
        if A == 1:
            equation_latex = equation_latex.replace("1x", "x")
        if A == -1:
            equation_latex = equation_latex.replace("-1x", "-x")
        if B == 1:
            equation_latex = equation_latex.replace("1y", "y")
        if B == -1:
            equation_latex = equation_latex.replace("-1y", "-y")

        x_int, y_int, x_latex, y_latex = self._calculate_intercepts(equation_type, params)

        problem_latex = f"Find the x-intercept and y-intercept of the line: ${equation_latex}$"
        answer_latex = f"x-intercept: ${x_latex}$, y-intercept: ${y_latex}$"

        return InterceptsProblem(
            equation_type=equation_type,
            equation_latex=equation_latex,
            x_intercept=x_int,
            y_intercept=y_int,
            x_intercept_latex=x_latex,
            y_intercept_latex=y_latex,
            difficulty='medium',
            worksheet_image=self._create_graph(equation_type, params, show_intercepts=False),
            answer_image=self._create_graph(equation_type, params, show_intercepts=True),
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_hard(self) -> InterceptsProblem:
        """Generate hard intercepts problem (complex fractions, horizontal lines)."""
        problem_type = random.choice(['complex_standard', 'horizontal', 'steep_slope'])

        if problem_type == 'horizontal':
            # Horizontal line y = b
            y_val = random.randint(-6, 6)
            while y_val == 0:
                y_val = random.randint(-6, 6)

            equation_type = 'slope-intercept'
            params = {'slope': 0, 'y_intercept': y_val}
            equation_latex = f"y = {y_val}"

        elif problem_type == 'steep_slope':
            # Very steep slope with fractional intercepts
            slope = random.randint(4, 8) * random.choice([-1, 1])
            y_intercept = random.randint(1, 7)

            equation_type = 'slope-intercept'
            params = {'slope': slope, 'y_intercept': y_intercept}
            equation_latex = f"y = {slope}x + {y_intercept}" if y_intercept > 0 else f"y = {slope}x - {abs(y_intercept)}"

        else:  # complex_standard
            # Standard form with larger coefficients
            A = random.randint(3, 7) * random.choice([-1, 1])
            B = random.randint(3, 7) * random.choice([-1, 1])
            C = random.randint(10, 20) * random.choice([-1, 1])

            equation_type = 'standard'
            params = {'A': A, 'B': B, 'C': C}

            equation_latex = f"{A}x + {B}y = {C}"
            if B < 0:
                equation_latex = f"{A}x - {abs(B)}y = {C}"

        x_int, y_int, x_latex, y_latex = self._calculate_intercepts(equation_type, params)

        problem_latex = f"Find the x-intercept and y-intercept of the line: ${equation_latex}$"
        answer_latex = f"x-intercept: ${x_latex}$, y-intercept: ${y_latex}$"

        return InterceptsProblem(
            equation_type=equation_type,
            equation_latex=equation_latex,
            x_intercept=x_int,
            y_intercept=y_int,
            x_intercept_latex=x_latex,
            y_intercept_latex=y_latex,
            difficulty='hard',
            worksheet_image=self._create_graph(equation_type, params, show_intercepts=False),
            answer_image=self._create_graph(equation_type, params, show_intercepts=True),
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_challenge(self) -> InterceptsProblem:
        """Generate challenge intercepts problem (vertical lines, no intercepts)."""
        problem_type = random.choice(['vertical', 'through_origin', 'complex_fraction'])

        if problem_type == 'vertical':
            # Vertical line x = a
            x_val = random.randint(-6, 6)
            while x_val == 0:
                x_val = random.randint(-6, 6)

            equation_type = 'vertical'
            params = {'x_value': x_val}
            equation_latex = f"x = {x_val}"

        elif problem_type == 'through_origin':
            # Line through origin (y-intercept = 0)
            slope = Fraction(random.randint(1, 5), random.randint(2, 4)).limit_denominator()

            equation_type = 'slope-intercept'
            params = {'slope': float(slope), 'y_intercept': 0}
            equation_latex = f"y = \\frac{{{slope.numerator}}}{{{slope.denominator}}}x"

        else:  # complex_fraction
            # Both intercepts are complex fractions
            A = random.choice([3, 5, 7, 9])
            B = random.choice([4, 6, 8])
            C = random.choice([10, 12, 15, 18, 20])

            equation_type = 'standard'
            params = {'A': A, 'B': B, 'C': C}
            equation_latex = f"{A}x + {B}y = {C}"

        x_int, y_int, x_latex, y_latex = self._calculate_intercepts(equation_type, params)

        problem_latex = f"Find the x-intercept and y-intercept of the line: ${equation_latex}$"
        answer_latex = f"x-intercept: ${x_latex}$, y-intercept: ${y_latex}$"

        return InterceptsProblem(
            equation_type=equation_type,
            equation_latex=equation_latex,
            x_intercept=x_int,
            y_intercept=y_int,
            x_intercept_latex=x_latex,
            y_intercept_latex=y_latex,
            difficulty='challenge',
            worksheet_image=self._create_graph(equation_type, params, show_intercepts=False),
            answer_image=self._create_graph(equation_type, params, show_intercepts=True),
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple intercepts problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of InterceptsProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems