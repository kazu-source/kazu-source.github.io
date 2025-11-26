"""
Generator for graphing slope-intercept form worksheets.
Chapter 4: Linear Equations (Two Variables) - Slope-Intercept Form (y = mx + b)
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from graphing_utils import CoordinatePlane
from PIL import Image


@dataclass
class SlopeInterceptProblem:
    """Represents a slope-intercept form graphing problem."""
    slope: float  # m in y = mx + b
    y_intercept: int  # b in y = mx + b
    equation_latex: str  # LaTeX string for the equation
    difficulty: str  # easy, medium, hard
    worksheet_image: object  # PIL Image for worksheet (blank grid)
    answer_image: object  # PIL Image for answer key (with line plotted)
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class SlopeInterceptGenerator:
    """Generator for slope-intercept form graphing problems."""

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
            List of SlopeInterceptProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems

    def generate_problem(self, difficulty: str) -> SlopeInterceptProblem:
        """
        Generate a single slope-intercept form graphing problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            SlopeInterceptProblem object
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

    def _generate_easy(self) -> SlopeInterceptProblem:
        """
        Generate easy problem: integer slope, small y-intercept.
        """
        # Small positive or negative integer slopes
        slope = random.choice([-3, -2, -1, 1, 2, 3])
        y_intercept = random.randint(-5, 5)

        # Format equation
        if slope == 1:
            slope_str = ""
        elif slope == -1:
            slope_str = "-"
        else:
            slope_str = str(slope)

        if y_intercept >= 0:
            equation_latex = f"y = {slope_str}x + {y_intercept}"
        else:
            equation_latex = f"y = {slope_str}x - {abs(y_intercept)}"

        # Create images
        worksheet_img, answer_img = self._create_images(slope, y_intercept)

        return SlopeInterceptProblem(
            slope=slope,
            y_intercept=y_intercept,
            equation_latex=equation_latex,
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_medium(self) -> SlopeInterceptProblem:
        """
        Generate medium problem: fractional slopes, larger intercepts.
        """
        # Fractional slopes (simple fractions)
        numerator = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        denominator = random.choice([2, 3, 4])
        slope = numerator / denominator

        y_intercept = random.randint(-8, 8)

        # Format equation with fraction (simplify if possible)
        slope_str = self._format_slope(numerator, denominator)

        if y_intercept >= 0:
            equation_latex = f"y = {slope_str}x + {y_intercept}"
        else:
            equation_latex = f"y = {slope_str}x - {abs(y_intercept)}"

        # Create images
        worksheet_img, answer_img = self._create_images(slope, y_intercept)

        return SlopeInterceptProblem(
            slope=slope,
            y_intercept=y_intercept,
            equation_latex=equation_latex,
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_hard(self) -> SlopeInterceptProblem:
        """
        Generate hard problem: special cases (zero slope, steep slopes, negative fractions).
        """
        problem_type = random.choice(['zero_slope', 'steep', 'negative_fraction'])

        if problem_type == 'zero_slope':
            # Horizontal line (slope = 0)
            slope = 0
            y_intercept = random.randint(-8, 8)
            equation_latex = f"y = {y_intercept}"

        elif problem_type == 'steep':
            # Steep slope
            slope = random.choice([-7, -6, -5, 5, 6, 7])
            y_intercept = random.randint(-5, 5)

            if slope == 1:
                slope_str = ""
            elif slope == -1:
                slope_str = "-"
            else:
                slope_str = str(slope)

            if y_intercept >= 0:
                equation_latex = f"y = {slope_str}x + {y_intercept}"
            else:
                equation_latex = f"y = {slope_str}x - {abs(y_intercept)}"

        else:  # negative_fraction
            # Negative fractional slope
            numerator = random.choice([-7, -5, -4, -3, -2])
            denominator = random.choice([2, 3, 4, 5])
            slope = numerator / denominator
            y_intercept = random.randint(-6, 6)

            slope_str = self._format_slope(numerator, denominator)

            if y_intercept >= 0:
                equation_latex = f"y = {slope_str}x + {y_intercept}"
            else:
                equation_latex = f"y = {slope_str}x - {abs(y_intercept)}"

        # Create images
        worksheet_img, answer_img = self._create_images(slope, y_intercept)

        return SlopeInterceptProblem(
            slope=slope,
            y_intercept=y_intercept,
            equation_latex=equation_latex,
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_challenge(self) -> SlopeInterceptProblem:
        """
        Generate challenge problem: very steep/flat slopes with complex fractions,
        large negative intercepts, and unusual fractional slopes.
        """
        problem_type = random.choice(['very_steep_fraction', 'very_flat_fraction', 'complex_negative', 'large_fraction'])

        if problem_type == 'very_steep_fraction':
            # Very steep fractional slope with large intercept
            numerator = random.choice([-11, -9, -8, 8, 9, 11])
            denominator = random.choice([2, 3])
            slope = numerator / denominator
            y_intercept = random.randint(-10, 10)

            slope_str = self._format_slope(numerator, denominator)

            if y_intercept >= 0:
                equation_latex = f"y = {slope_str}x + {y_intercept}"
            else:
                equation_latex = f"y = {slope_str}x - {abs(y_intercept)}"

        elif problem_type == 'very_flat_fraction':
            # Very flat fractional slope (small rise over large run)
            numerator = random.choice([-2, -1, 1, 2])
            denominator = random.choice([5, 6, 7, 8])
            slope = numerator / denominator
            y_intercept = random.randint(-8, 8)

            slope_str = self._format_slope(numerator, denominator)

            if y_intercept >= 0:
                equation_latex = f"y = {slope_str}x + {y_intercept}"
            else:
                equation_latex = f"y = {slope_str}x - {abs(y_intercept)}"

        elif problem_type == 'complex_negative':
            # Complex negative fractional slope with negative intercept
            numerator = random.choice([-13, -11, -9, -7])
            denominator = random.choice([4, 5, 6])
            slope = numerator / denominator
            y_intercept = random.randint(-12, -5)

            slope_str = self._format_slope(numerator, denominator)
            equation_latex = f"y = {slope_str}x - {abs(y_intercept)}"

        else:  # large_fraction
            # Larger fraction slope with mixed values
            numerator = random.choice([-17, -13, -11, 11, 13, 17])
            denominator = random.choice([3, 4, 5])
            slope = numerator / denominator
            y_intercept = random.randint(-10, 10)

            slope_str = self._format_slope(numerator, denominator)

            if y_intercept >= 0:
                equation_latex = f"y = {slope_str}x + {y_intercept}"
            else:
                equation_latex = f"y = {slope_str}x - {abs(y_intercept)}"

        # Create images
        worksheet_img, answer_img = self._create_images(slope, y_intercept)

        return SlopeInterceptProblem(
            slope=slope,
            y_intercept=y_intercept,
            equation_latex=equation_latex,
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _create_images(self, slope, y_intercept):
        """Create worksheet and answer key images."""
        # Create worksheet image (blank grid)
        plane = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig, ax = plane.create_figure(figsize=(6, 6))
        worksheet_img = self._fig_to_image(fig)

        # Create answer key image (with line plotted)
        plane_ans = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig_ans, ax_ans = plane_ans.create_figure(figsize=(6, 6))

        # Plot the line using slope-intercept form
        plane_ans.plot_line_from_equation(
            ax_ans,
            slope=slope,
            y_intercept=y_intercept,
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
    gen = SlopeInterceptGenerator()

    print("Testing Slope-Intercept Form Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. Graph: {problem.equation_latex}")
            print(f"   (slope={problem.slope}, y-intercept={problem.y_intercept})\n")
