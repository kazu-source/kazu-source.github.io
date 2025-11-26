"""
Generator for graphing point-slope form worksheets.
Chapter 4: Linear Equations (Two Variables) - Point-Slope Form (y - y₁ = m(x - x₁))
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from graphing_utils import CoordinatePlane
from PIL import Image


@dataclass
class PointSlopeProblem:
    """Represents a point-slope form graphing problem."""
    slope: float  # m in y - y₁ = m(x - x₁)
    point: Tuple[int, int]  # (x₁, y₁) in y - y₁ = m(x - x₁)
    equation_latex: str  # LaTeX string for the equation
    difficulty: str  # easy, medium, hard
    worksheet_image: object  # PIL Image for worksheet (blank grid)
    answer_image: object  # PIL Image for answer key (with line plotted)
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class PointSlopeGenerator:
    """Generator for point-slope form graphing problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def _format_slope(self, numerator: int, denominator: int) -> str:
        """
        Format a slope as a fraction, simplifying to whole number if possible.

        Args:
            numerator: Numerator of the slope fraction
            denominator: Denominator of the slope fraction

        Returns:
            Formatted slope string (LaTeX)
        """
        # If divisible, simplify to whole number
        if numerator % denominator == 0:
            result = numerator // denominator
            if result == 1:
                return ""
            elif result == -1:
                return "-"
            else:
                return str(result)
        else:
            # Keep as fraction
            return f"\\frac{{{numerator}}}{{{denominator}}}"

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple graphing problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
            num_problems: Number of problems to generate

        Returns:
            List of PointSlopeProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems

    def generate_problem(self, difficulty: str) -> PointSlopeProblem:
        """
        Generate a single point-slope form graphing problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            PointSlopeProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        elif difficulty == 'challenge':
            return self._generate_challenge()
        else:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    def _generate_easy(self) -> PointSlopeProblem:
        """
        Generate easy problem: integer slope, point in first quadrant or near origin.
        """
        # Small positive integer slopes
        slope = random.choice([1, 2, 3])

        # Point near origin or in first quadrant
        x1 = random.randint(0, 5)
        y1 = random.randint(0, 5)
        point = (x1, y1)

        # Format equation: y - y1 = m(x - x1)
        slope_str = str(slope) if slope != 1 else ""

        if y1 >= 0:
            y_part = f"y - {y1}" if y1 != 0 else "y"
        else:
            y_part = f"y + {abs(y1)}"

        if x1 >= 0:
            x_part = f"x - {x1}" if x1 != 0 else "x"
        else:
            x_part = f"x + {abs(x1)}"

        equation_latex = f"{y_part} = {slope_str}({x_part})"

        # Create images
        worksheet_img, answer_img = self._create_images(slope, point)

        return PointSlopeProblem(
            slope=slope,
            point=point,
            equation_latex=equation_latex,
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_medium(self) -> PointSlopeProblem:
        """
        Generate medium problem: fractional slopes, points in any quadrant.
        """
        # Fractional slopes
        numerator = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        denominator = random.choice([2, 3])
        slope = numerator / denominator

        # Point anywhere
        x1 = random.randint(-6, 6)
        y1 = random.randint(-6, 6)
        point = (x1, y1)

        # Format equation with fraction
        if denominator == 1:
            slope_str = str(numerator)
        else:
            slope_str = f"\\frac{{{numerator}}}{{{denominator}}}"

        if y1 >= 0:
            y_part = f"y - {y1}" if y1 != 0 else "y"
        else:
            y_part = f"y + {abs(y1)}"

        if x1 >= 0:
            x_part = f"x - {x1}" if x1 != 0 else "x"
        else:
            x_part = f"x + {abs(x1)}"

        equation_latex = f"{y_part} = {slope_str}({x_part})"

        # Create images
        worksheet_img, answer_img = self._create_images(slope, point)

        return PointSlopeProblem(
            slope=slope,
            point=point,
            equation_latex=equation_latex,
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_hard(self) -> PointSlopeProblem:
        """
        Generate hard problem: negative slopes, larger coordinates, special cases.
        """
        problem_type = random.choice(['negative_slope', 'zero_slope', 'steep'])

        if problem_type == 'negative_slope':
            # Negative fractional slope
            numerator = random.choice([-5, -4, -3, -2])
            denominator = random.choice([2, 3, 4])
            slope = numerator / denominator

            x1 = random.randint(-8, 8)
            y1 = random.randint(-8, 8)

            slope_str = f"\\frac{{{numerator}}}{{{denominator}}}"

        elif problem_type == 'zero_slope':
            # Horizontal line (slope = 0)
            slope = 0
            slope_str = "0"

            x1 = random.randint(-8, 8)
            y1 = random.randint(-8, 8)

        else:  # steep
            # Steep slope
            slope = random.choice([-6, -5, 5, 6])
            slope_str = str(slope)

            x1 = random.randint(-6, 6)
            y1 = random.randint(-6, 6)

        point = (x1, y1)

        # Format equation
        if y1 >= 0:
            y_part = f"y - {y1}" if y1 != 0 else "y"
        else:
            y_part = f"y + {abs(y1)}"

        if x1 >= 0:
            x_part = f"x - {x1}" if x1 != 0 else "x"
        else:
            x_part = f"x + {abs(x1)}"

        equation_latex = f"{y_part} = {slope_str}({x_part})"

        # Create images
        worksheet_img, answer_img = self._create_images(slope, point)

        return PointSlopeProblem(
            slope=slope,
            point=point,
            equation_latex=equation_latex,
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_challenge(self) -> PointSlopeProblem:
        """
        Generate challenge problem: very steep/flat fractional slopes, large negative coordinates,
        complex fractions with extreme points.
        """
        problem_type = random.choice(['very_steep_fraction', 'very_flat_fraction', 'negative_extremes', 'complex_fraction'])

        if problem_type == 'very_steep_fraction':
            # Very steep fractional slope with extreme coordinates
            numerator = random.choice([-11, -9, -7, 7, 9, 11])
            denominator = random.choice([2, 3])
            slope = numerator / denominator
            slope_str = f"\\frac{{{numerator}}}{{{denominator}}}"

            x1 = random.randint(-10, 10)
            y1 = random.randint(-10, 10)

        elif problem_type == 'very_flat_fraction':
            # Very flat fractional slope
            numerator = random.choice([-3, -2, -1, 1, 2, 3])
            denominator = random.choice([5, 6, 7, 8])
            slope = numerator / denominator
            slope_str = f"\\frac{{{numerator}}}{{{denominator}}}"

            x1 = random.randint(-9, 9)
            y1 = random.randint(-9, 9)

        elif problem_type == 'negative_extremes':
            # Both slope and point with large negative values
            numerator = random.choice([-13, -11, -9, -7])
            denominator = random.choice([3, 4, 5])
            slope = numerator / denominator
            slope_str = f"\\frac{{{numerator}}}{{{denominator}}}"

            x1 = random.randint(-10, -5)
            y1 = random.randint(-10, -5)

        else:  # complex_fraction
            # Complex fractional slope with large coordinates
            numerator = random.choice([-17, -13, -11, 11, 13, 17])
            denominator = random.choice([4, 5, 6, 7])
            slope = numerator / denominator
            slope_str = f"\\frac{{{numerator}}}{{{denominator}}}"

            x1 = random.randint(-10, 10)
            y1 = random.randint(-10, 10)

        point = (x1, y1)

        # Format equation
        if y1 >= 0:
            y_part = f"y - {y1}" if y1 != 0 else "y"
        else:
            y_part = f"y + {abs(y1)}"

        if x1 >= 0:
            x_part = f"x - {x1}" if x1 != 0 else "x"
        else:
            x_part = f"x + {abs(x1)}"

        equation_latex = f"{y_part} = {slope_str}({x_part})"

        # Create images
        worksheet_img, answer_img = self._create_images(slope, point)

        return PointSlopeProblem(
            slope=slope,
            point=point,
            equation_latex=equation_latex,
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _create_images(self, slope, point):
        """Create worksheet and answer key images."""
        # Create worksheet image (blank grid)
        plane = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig, ax = plane.create_figure(figsize=(6, 6))
        worksheet_img = self._fig_to_image(fig)

        # Create answer key image (with line plotted)
        plane_ans = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig_ans, ax_ans = plane_ans.create_figure(figsize=(6, 6))

        # Plot the point
        x1, y1 = point
        plane_ans.plot_point(ax_ans, x1, y1, label=f"({x1},{y1})", color='blue')

        # Plot the line using point-slope form
        plane_ans.plot_line_from_equation(
            ax_ans,
            slope=slope,
            point=point,
            color='red',
            linewidth=2
        )

        answer_img = self._fig_to_image(fig_ans)

        return worksheet_img, answer_img

    def _fig_to_image(self, fig):
        """Convert matplotlib figure to PIL Image."""
        import io
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=150)
        buf.seek(0)
        img = Image.open(buf)
        import matplotlib.pyplot as plt
        plt.close(fig)
        return img


if __name__ == "__main__":
    # Test the generator
    gen = PointSlopeGenerator()

    print("Testing Point-Slope Form Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. Graph: {problem.equation_latex}")
            print(f"   (slope={problem.slope}, point={problem.point})\n")
