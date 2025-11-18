"""
Generator for graphing standard form worksheets.
Chapter 4: Linear Equations (Two Variables) - Standard Form (Ax + By = C)
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
class StandardFormProblem:
    """Represents a standard form graphing problem."""
    a: int  # A in Ax + By = C
    b: int  # B in Ax + By = C
    c: int  # C in Ax + By = C
    equation_latex: str  # LaTeX string for the equation
    difficulty: str  # easy, medium, hard
    worksheet_image: object  # PIL Image for worksheet (blank grid)
    answer_image: object  # PIL Image for answer key (with line plotted)
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class StandardFormGenerator:
    """Generator for standard form graphing problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple graphing problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
            num_problems: Number of problems to generate

        Returns:
            List of StandardFormProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems

    def generate_problem(self, difficulty: str) -> StandardFormProblem:
        """
        Generate a single standard form graphing problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            StandardFormProblem object
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

    def _generate_easy(self) -> StandardFormProblem:
        """
        Generate easy problem: small positive coefficients, easy intercepts.
        """
        # Small coefficients
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(4, 20)

        # Format equation
        equation_latex = self._format_equation(a, b, c)

        # Create images
        worksheet_img, answer_img = self._create_images(a, b, c)

        return StandardFormProblem(
            a=a,
            b=b,
            c=c,
            equation_latex=equation_latex,
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_medium(self) -> StandardFormProblem:
        """
        Generate medium problem: mix of positive/negative coefficients, larger values.
        """
        # Mixed coefficients
        a = random.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        b = random.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        c = random.randint(-20, 20)

        # Avoid a=0 or b=0 (would be vertical/horizontal)
        while a == 0 or b == 0:
            a = random.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
            b = random.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])

        # Format equation
        equation_latex = self._format_equation(a, b, c)

        # Create images
        worksheet_img, answer_img = self._create_images(a, b, c)

        return StandardFormProblem(
            a=a,
            b=b,
            c=c,
            equation_latex=equation_latex,
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_hard(self) -> StandardFormProblem:
        """
        Generate hard problem: special cases (vertical/horizontal lines), larger coefficients.
        """
        problem_type = random.choice(['vertical', 'horizontal', 'negative_coeffs'])

        if problem_type == 'vertical':
            # Vertical line: Ax = C (B = 0)
            a = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            b = 0
            c = random.randint(-10, 10)

        elif problem_type == 'horizontal':
            # Horizontal line: By = C (A = 0)
            a = 0
            b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            c = random.randint(-10, 10)

        else:  # negative_coeffs
            # Both coefficients negative
            a = random.randint(-8, -2)
            b = random.randint(-8, -2)
            c = random.randint(-30, 30)

        # Format equation
        equation_latex = self._format_equation(a, b, c)

        # Create images
        worksheet_img, answer_img = self._create_images(a, b, c)

        return StandardFormProblem(
            a=a,
            b=b,
            c=c,
            equation_latex=equation_latex,
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_challenge(self) -> StandardFormProblem:
        """
        Generate challenge problem: large coefficients, complex negative values,
        fractional intercepts, and extreme slope combinations.
        """
        problem_type = random.choice(['large_coeffs', 'all_negative', 'coprime_large', 'extreme_ratio'])

        if problem_type == 'large_coeffs':
            # Large coefficients with complex relationships
            a = random.choice([-15, -12, -9, 9, 12, 15])
            b = random.choice([-11, -8, -7, 7, 8, 11])
            c = random.randint(-50, 50)

        elif problem_type == 'all_negative':
            # All negative coefficients with large magnitudes
            a = random.randint(-18, -8)
            b = random.randint(-15, -6)
            c = random.randint(-60, -10)

        elif problem_type == 'coprime_large':
            # Large coprime coefficients (creates fractional slope)
            a = random.choice([-13, -11, -7, 7, 11, 13])
            b = random.choice([-17, -13, -11, 11, 13, 17])
            c = random.randint(-40, 40)

        else:  # extreme_ratio
            # Extreme ratio between coefficients
            if random.choice([True, False]):
                # Very steep slope (large a, small b)
                a = random.choice([-20, -18, -15, 15, 18, 20])
                b = random.choice([-3, -2, -1, 1, 2, 3])
            else:
                # Very flat slope (small a, large b)
                a = random.choice([-3, -2, -1, 1, 2, 3])
                b = random.choice([-20, -18, -15, 15, 18, 20])
            c = random.randint(-50, 50)

        # Format equation
        equation_latex = self._format_equation(a, b, c)

        # Create images
        worksheet_img, answer_img = self._create_images(a, b, c)

        return StandardFormProblem(
            a=a,
            b=b,
            c=c,
            equation_latex=equation_latex,
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _format_equation(self, a, b, c):
        """Format the standard form equation as LaTeX."""
        parts = []

        # Format Ax term
        if a != 0:
            if a == 1:
                parts.append("x")
            elif a == -1:
                parts.append("-x")
            else:
                parts.append(f"{a}x")

        # Format By term
        if b != 0:
            if len(parts) > 0:  # Not first term
                if b == 1:
                    parts.append("+ y")
                elif b == -1:
                    parts.append("- y")
                elif b > 0:
                    parts.append(f"+ {b}y")
                else:
                    parts.append(f"- {abs(b)}y")
            else:  # First term
                if b == 1:
                    parts.append("y")
                elif b == -1:
                    parts.append("-y")
                else:
                    parts.append(f"{b}y")

        # Combine parts
        left_side = " ".join(parts) if parts else "0"
        equation_latex = f"{left_side} = {c}"

        return equation_latex

    def _create_images(self, a, b, c):
        """Create worksheet and answer key images."""
        # Create worksheet image (blank grid)
        plane = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig, ax = plane.create_figure(figsize=(6, 6))
        worksheet_img = self._fig_to_image(fig)

        # Create answer key image (with line plotted)
        plane_ans = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig_ans, ax_ans = plane_ans.create_figure(figsize=(6, 6))

        # Plot the line using standard form
        plane_ans.plot_line_from_equation(
            ax_ans,
            standard_form=(a, b, c),
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
    gen = StandardFormGenerator()

    print("Testing Standard Form Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. Graph: {problem.equation_latex}")
            print(f"   ({problem.a}x + {problem.b}y = {problem.c})\n")
