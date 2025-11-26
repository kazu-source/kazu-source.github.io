"""
Generator for slope worksheets.
Chapter 4: Linear Equations (Two Variables) - Slope
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from fractions import Fraction
from io import BytesIO
import matplotlib.pyplot as plt

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from graphing_utils import CoordinatePlane
from PIL import Image


@dataclass
class SlopeProblem:
    """Represents a slope calculation problem."""
    point1: tuple  # (x1, y1)
    point2: tuple  # (x2, y2)
    slope: float  # Calculated slope
    slope_fraction: str  # Slope as a fraction string
    slope_latex: str  # LaTeX representation of slope
    difficulty: str  # easy, medium, hard, challenge
    worksheet_image: object  # PIL Image for worksheet (grid with points)
    answer_image: object  # PIL Image for answer key (grid with points and line)
    problem_latex: str  # LaTeX string for the problem
    answer_latex: str  # LaTeX string for the answer
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class SlopeGenerator:
    """Generator for slope calculation problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def _calculate_slope(self, x1, y1, x2, y2):
        """
        Calculate the slope between two points.

        Args:
            x1, y1: Coordinates of first point
            x2, y2: Coordinates of second point

        Returns:
            Tuple of (slope_value, slope_fraction_string, slope_latex)
        """
        if x2 == x1:
            return float('inf'), 'undefined', '\\text{undefined}'

        rise = y2 - y1
        run = x2 - x1
        slope = rise / run

        # Create fraction representation
        frac = Fraction(rise, run).limit_denominator()

        # Format for display
        if frac.denominator == 1:
            slope_str = str(frac.numerator)
            slope_latex = str(frac.numerator)
        else:
            slope_str = f"{frac.numerator}/{frac.denominator}"
            slope_latex = f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"

        return slope, slope_str, slope_latex

    def _create_graph(self, point1, point2, show_line=False, show_slope_triangle=False):
        """
        Create a coordinate plane with two points plotted.

        Args:
            point1: First point (x1, y1)
            point2: Second point (x2, y2)
            show_line: Whether to draw the line through the points
            show_slope_triangle: Whether to show the rise/run triangle

        Returns:
            PIL Image object
        """
        plane = CoordinatePlane()
        fig, ax = plane.create_figure()

        x1, y1 = point1
        x2, y2 = point2

        # Plot the points
        plane.plot_point(ax, x1, y1, label=f"({x1}, {y1})", color='blue', size=80)
        plane.plot_point(ax, x2, y2, label=f"({x2}, {y2})", color='blue', size=80)

        if show_line:
            # Draw line through points
            x_vals = [plane.x_min, plane.x_max]
            if x2 != x1:
                slope = (y2 - y1) / (x2 - x1)
                y_intercept = y1 - slope * x1
                y_vals = [slope * x + y_intercept for x in x_vals]
                ax.plot(x_vals, y_vals, 'r-', linewidth=2, alpha=0.7)
            else:
                # Vertical line
                ax.axvline(x=x1, color='red', linewidth=2, alpha=0.7)

        if show_slope_triangle and x2 != x1:
            # Draw rise and run
            rise = y2 - y1
            run = x2 - x1

            # Draw horizontal line (run)
            ax.plot([x1, x2], [y1, y1], 'g--', linewidth=1.5, alpha=0.7)
            # Draw vertical line (rise)
            ax.plot([x2, x2], [y1, y2], 'b--', linewidth=1.5, alpha=0.7)

            # Add labels
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            ax.text(mid_x, y1 - 0.5, f'run = {run}', fontsize=10, ha='center', color='green')
            ax.text(x2 + 0.5, mid_y, f'rise = {rise}', fontsize=10, ha='left', color='blue')

        # Convert to PIL Image
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        plt.close(fig)
        buffer.seek(0)
        image = Image.open(buffer)

        return image

    def generate_problem(self, difficulty: str) -> SlopeProblem:
        """
        Generate a single slope calculation problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            SlopeProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> SlopeProblem:
        """Generate easy slope problem (positive integer slopes)."""
        # Generate two points with positive integer slope
        x1 = random.randint(-5, 0)
        y1 = random.randint(-5, 5)

        # Ensure different x-coordinates
        x2 = random.randint(1, 5)
        while x2 == x1:
            x2 = random.randint(1, 5)

        # Create a positive integer slope
        slope = random.randint(1, 3)
        y2 = y1 + slope * (x2 - x1)

        # Keep y2 in bounds
        while y2 < -8 or y2 > 8:
            slope = random.randint(1, 3)
            y2 = y1 + slope * (x2 - x1)

        point1 = (x1, y1)
        point2 = (x2, y2)

        slope_val, slope_str, slope_latex = self._calculate_slope(x1, y1, x2, y2)

        problem_latex = f"Find the slope between the points $({x1}, {y1})$ and $({x2}, {y2})$"
        answer_latex = f"$m = {slope_latex}$"

        return SlopeProblem(
            point1=point1,
            point2=point2,
            slope=slope_val,
            slope_fraction=slope_str,
            slope_latex=slope_latex,
            difficulty='easy',
            worksheet_image=self._create_graph(point1, point2, show_line=False),
            answer_image=self._create_graph(point1, point2, show_line=True, show_slope_triangle=True),
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_medium(self) -> SlopeProblem:
        """Generate medium slope problem (negative and fractional slopes)."""
        x1 = random.randint(-6, 2)
        y1 = random.randint(-6, 6)

        x2 = random.randint(-6, 6)
        while x2 == x1:
            x2 = random.randint(-6, 6)

        # Create fractional or negative slopes
        rise = random.randint(-6, 6)
        while rise == 0:
            rise = random.randint(-6, 6)

        run = x2 - x1
        y2 = y1 + rise

        # Keep y2 in bounds
        while y2 < -8 or y2 > 8:
            rise = random.randint(-4, 4)
            while rise == 0:
                rise = random.randint(-4, 4)
            y2 = y1 + rise

        point1 = (x1, y1)
        point2 = (x2, y2)

        slope_val, slope_str, slope_latex = self._calculate_slope(x1, y1, x2, y2)

        problem_latex = f"Find the slope between the points $({x1}, {y1})$ and $({x2}, {y2})$"
        answer_latex = f"$m = {slope_latex}$"

        return SlopeProblem(
            point1=point1,
            point2=point2,
            slope=slope_val,
            slope_fraction=slope_str,
            slope_latex=slope_latex,
            difficulty='medium',
            worksheet_image=self._create_graph(point1, point2, show_line=False),
            answer_image=self._create_graph(point1, point2, show_line=True, show_slope_triangle=True),
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_hard(self) -> SlopeProblem:
        """Generate hard slope problem (more complex fractions, zero slopes)."""
        problem_type = random.choice(['fraction', 'zero', 'negative_fraction'])

        if problem_type == 'zero':
            # Horizontal line (slope = 0)
            y1 = random.randint(-6, 6)
            x1 = random.randint(-6, 0)
            x2 = random.randint(1, 6)
            y2 = y1
        elif problem_type == 'fraction':
            # Non-simple fractions
            x1 = random.randint(-6, 2)
            y1 = random.randint(-6, 6)

            # Create a run that doesn't divide evenly
            run = random.choice([3, 5, 7])
            x2 = x1 + run

            # Create a rise that makes a non-simple fraction
            rise = random.choice([2, 4, 5]) * random.choice([-1, 1])
            y2 = y1 + rise

            # Keep in bounds
            while x2 < -8 or x2 > 8 or y2 < -8 or y2 > 8:
                run = random.choice([3, 4, 5])
                x2 = x1 + run
                rise = random.choice([2, 3, 4]) * random.choice([-1, 1])
                y2 = y1 + rise
        else:
            # Negative fractions
            x1 = random.randint(-6, 2)
            y1 = random.randint(-2, 6)

            run = random.randint(2, 5)
            x2 = x1 + run

            rise = -random.randint(1, 6)
            y2 = y1 + rise

            # Keep in bounds
            while x2 > 8 or y2 < -8:
                run = random.randint(2, 4)
                x2 = x1 + run
                rise = -random.randint(1, 4)
                y2 = y1 + rise

        point1 = (x1, y1)
        point2 = (x2, y2)

        slope_val, slope_str, slope_latex = self._calculate_slope(x1, y1, x2, y2)

        problem_latex = f"Find the slope between the points $({x1}, {y1})$ and $({x2}, {y2})$"
        answer_latex = f"$m = {slope_latex}$"

        return SlopeProblem(
            point1=point1,
            point2=point2,
            slope=slope_val,
            slope_fraction=slope_str,
            slope_latex=slope_latex,
            difficulty='hard',
            worksheet_image=self._create_graph(point1, point2, show_line=False),
            answer_image=self._create_graph(point1, point2, show_line=True, show_slope_triangle=True),
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_challenge(self) -> SlopeProblem:
        """Generate challenge slope problem (undefined slopes, complex coordinates)."""
        problem_type = random.choice(['undefined', 'complex_fraction', 'negative_both'])

        if problem_type == 'undefined':
            # Vertical line (undefined slope)
            x1 = random.randint(-6, 6)
            x2 = x1
            y1 = random.randint(-6, 2)
            y2 = random.randint(3, 6)
        elif problem_type == 'complex_fraction':
            # Both coordinates negative with fractional slope
            x1 = random.randint(-8, -3)
            y1 = random.randint(-8, -3)

            # Create complex fractions
            run = random.choice([3, 5, 7])
            rise = random.choice([4, 5, 7, 8])

            x2 = x1 + run
            y2 = y1 + rise

            # Keep in bounds
            while x2 > 8 or y2 > 8:
                run = random.choice([3, 4, 5])
                rise = random.choice([3, 4, 5])
                x2 = x1 + run
                y2 = y1 + rise
        else:
            # Both coordinates negative
            x1 = random.randint(-8, -4)
            y1 = random.randint(-8, -4)
            x2 = random.randint(-3, 3)
            y2 = random.randint(-3, 3)

        point1 = (x1, y1)
        point2 = (x2, y2)

        slope_val, slope_str, slope_latex = self._calculate_slope(x1, y1, x2, y2)

        problem_latex = f"Find the slope between the points $({x1}, {y1})$ and $({x2}, {y2})$"

        if slope_val == float('inf'):
            answer_latex = "The slope is undefined (vertical line)"
        else:
            answer_latex = f"$m = {slope_latex}$"

        return SlopeProblem(
            point1=point1,
            point2=point2,
            slope=slope_val,
            slope_fraction=slope_str,
            slope_latex=slope_latex,
            difficulty='challenge',
            worksheet_image=self._create_graph(point1, point2, show_line=False),
            answer_image=self._create_graph(point1, point2,
                                           show_line=(slope_val != float('inf')),
                                           show_slope_triangle=(slope_val != float('inf'))),
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple slope problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of SlopeProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems