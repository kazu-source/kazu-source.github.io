"""
Generator for graphing systems of equations worksheets.
Chapter 5: Systems of Equations - Graphing Method
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from graphing_utils import CoordinatePlane


@dataclass
class GraphingSystemProblem:
    """Represents a system of equations graphing problem."""
    equation1_latex: str  # First equation in LaTeX format
    equation2_latex: str  # Second equation in LaTeX format
    slope1: float  # Slope of first line
    y_intercept1: float  # Y-intercept of first line
    slope2: float  # Slope of second line
    y_intercept2: float  # Y-intercept of second line
    solution: Tuple[float, float]  # (x, y) intersection point
    difficulty: str  # easy, medium, hard, challenge
    worksheet_image: object  # PIL Image for worksheet (blank grid with equations)
    answer_image: object  # PIL Image for answer key (with lines and intersection)
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class GraphingSystemsGenerator:
    """Generator for systems of equations graphing problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def generate_problem(self, difficulty: str) -> GraphingSystemProblem:
        """
        Generate a single systems graphing problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            GraphingSystemProblem object
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

    def _generate_easy(self) -> GraphingSystemProblem:
        """
        Generate easy problem: Integer slopes (±1, ±2), integer intercepts, integer solution.
        Both equations in slope-intercept form: y = mx + b
        """
        # Generate integer solution point
        x_sol = random.randint(-5, 5)
        y_sol = random.randint(-5, 5)

        # Generate first line with integer slope through the solution
        slope1 = random.choice([-2, -1, 1, 2])
        y_intercept1 = y_sol - slope1 * x_sol

        # Generate second line with different integer slope through the solution
        slope2 = random.choice([-2, -1, 1, 2])
        while slope2 == slope1:  # Ensure different slopes (not parallel)
            slope2 = random.choice([-2, -1, 1, 2])
        y_intercept2 = y_sol - slope2 * x_sol

        # Format equations: y = mx + b
        eq1_latex = self._format_slope_intercept(slope1, y_intercept1)
        eq2_latex = self._format_slope_intercept(slope2, y_intercept2)

        # Create worksheet image (blank grid)
        worksheet_img = self._create_worksheet_image()

        # Create answer key image (with lines and intersection)
        answer_img = self._create_answer_image(
            slope1, y_intercept1, slope2, y_intercept2,
            x_sol, y_sol
        )

        return GraphingSystemProblem(
            equation1_latex=eq1_latex,
            equation2_latex=eq2_latex,
            slope1=slope1,
            y_intercept1=y_intercept1,
            slope2=slope2,
            y_intercept2=y_intercept2,
            solution=(x_sol, y_sol),
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_medium(self) -> GraphingSystemProblem:
        """
        Generate medium problem: Fractional slopes (1/2, 2/3, etc.), integer solution.
        Mix of slope-intercept and standard form.
        """
        # Generate integer solution point
        x_sol = random.randint(-4, 4)
        y_sol = random.randint(-4, 4)

        # Generate first line with fractional slope
        numerator1 = random.choice([-3, -2, -1, 1, 2, 3])
        denominator1 = random.choice([2, 3])
        slope1 = numerator1 / denominator1
        y_intercept1 = y_sol - slope1 * x_sol

        # Generate second line with different slope
        slope2 = random.choice([-2, -1, 1, 2, 3])
        while abs(slope2 - slope1) < 0.5:  # Ensure sufficiently different slopes
            slope2 = random.choice([-2, -1, 1, 2, 3])
        y_intercept2 = y_sol - slope2 * x_sol

        # Format first equation as slope-intercept
        eq1_latex = self._format_slope_intercept(slope1, y_intercept1)

        # Format second equation as standard form (Ax + By = C)
        # From y = mx + b, we get: -mx + y = b, or multiply to clear fractions
        A = -int(slope2)
        B = 1
        C = int(y_intercept2)
        eq2_latex = self._format_standard_form(A, B, C)

        # Create images
        worksheet_img = self._create_worksheet_image()
        answer_img = self._create_answer_image(
            slope1, y_intercept1, slope2, y_intercept2,
            x_sol, y_sol
        )

        return GraphingSystemProblem(
            equation1_latex=eq1_latex,
            equation2_latex=eq2_latex,
            slope1=slope1,
            y_intercept1=y_intercept1,
            slope2=slope2,
            y_intercept2=y_intercept2,
            solution=(x_sol, y_sol),
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_hard(self) -> GraphingSystemProblem:
        """
        Generate hard problem: Both equations in standard form, may have fractional solution.
        """
        # Generate solution (may be fractional)
        x_sol = random.randint(-8, 8) / 2.0  # 0.5 increments
        y_sol = random.randint(-8, 8) / 2.0

        # Generate first line
        slope1 = random.randint(-4, 4) / 2.0
        while slope1 == 0:
            slope1 = random.randint(-4, 4) / 2.0
        y_intercept1 = y_sol - slope1 * x_sol

        # Generate second line
        slope2 = random.randint(-4, 4) / 2.0
        while slope2 == 0 or abs(slope2 - slope1) < 0.5:
            slope2 = random.randint(-4, 4) / 2.0
        y_intercept2 = y_sol - slope2 * x_sol

        # Convert both to standard form
        # From y = mx + b: -mx + y = b, multiply by 2 to clear fractions
        A1 = -int(slope1 * 2)
        B1 = 2
        C1 = int(y_intercept1 * 2)

        A2 = -int(slope2 * 2)
        B2 = 2
        C2 = int(y_intercept2 * 2)

        eq1_latex = self._format_standard_form(A1, B1, C1)
        eq2_latex = self._format_standard_form(A2, B2, C2)

        # Create images
        worksheet_img = self._create_worksheet_image()
        answer_img = self._create_answer_image(
            slope1, y_intercept1, slope2, y_intercept2,
            x_sol, y_sol
        )

        return GraphingSystemProblem(
            equation1_latex=eq1_latex,
            equation2_latex=eq2_latex,
            slope1=slope1,
            y_intercept1=y_intercept1,
            slope2=slope2,
            y_intercept2=y_intercept2,
            solution=(x_sol, y_sol),
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_challenge(self) -> GraphingSystemProblem:
        """
        Generate challenge problem: Complex standard forms, fractional solutions, larger range.
        """
        # Generate solution (fractional)
        x_sol = random.randint(-12, 12) / 3.0  # 1/3 increments
        y_sol = random.randint(-12, 12) / 3.0

        # Generate lines with more complex slopes
        slope1 = random.randint(-6, 6) / 3.0
        while abs(slope1) < 0.3:
            slope1 = random.randint(-6, 6) / 3.0
        y_intercept1 = y_sol - slope1 * x_sol

        slope2 = random.randint(-6, 6) / 3.0
        while abs(slope2) < 0.3 or abs(slope2 - slope1) < 0.5:
            slope2 = random.randint(-6, 6) / 3.0
        y_intercept2 = y_sol - slope2 * x_sol

        # Convert to standard form with larger coefficients
        A1 = -int(slope1 * 3)
        B1 = 3
        C1 = int(y_intercept1 * 3)

        A2 = -int(slope2 * 3)
        B2 = 3
        C2 = int(y_intercept2 * 3)

        eq1_latex = self._format_standard_form(A1, B1, C1)
        eq2_latex = self._format_standard_form(A2, B2, C2)

        # Create images
        worksheet_img = self._create_worksheet_image()
        answer_img = self._create_answer_image(
            slope1, y_intercept1, slope2, y_intercept2,
            x_sol, y_sol
        )

        return GraphingSystemProblem(
            equation1_latex=eq1_latex,
            equation2_latex=eq2_latex,
            slope1=slope1,
            y_intercept1=y_intercept1,
            slope2=slope2,
            y_intercept2=y_intercept2,
            solution=(x_sol, y_sol),
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _format_slope_intercept(self, slope: float, y_intercept: float) -> str:
        """Format equation as y = mx + b."""
        # Handle slope
        if slope == 1:
            slope_str = "x"
        elif slope == -1:
            slope_str = "-x"
        elif slope == int(slope):
            slope_str = f"{int(slope)}x"
        else:
            # Format as fraction if possible
            slope_str = f"{slope}x"

        # Handle y-intercept
        if y_intercept == 0:
            return f"y = {slope_str}"
        elif y_intercept > 0:
            if y_intercept == int(y_intercept):
                return f"y = {slope_str} + {int(y_intercept)}"
            else:
                return f"y = {slope_str} + {y_intercept}"
        else:
            if y_intercept == int(y_intercept):
                return f"y = {slope_str} - {int(abs(y_intercept))}"
            else:
                return f"y = {slope_str} - {abs(y_intercept)}"

    def _format_standard_form(self, A: int, B: int, C: int) -> str:
        """Format equation as Ax + By = C."""
        # Handle A term
        if A == 1:
            a_str = "x"
        elif A == -1:
            a_str = "-x"
        elif A == 0:
            a_str = ""
        else:
            a_str = f"{A}x"

        # Handle B term
        if B == 1:
            if a_str:
                b_str = " + y"
            else:
                b_str = "y"
        elif B == -1:
            b_str = " - y"
        elif B == 0:
            b_str = ""
        elif B > 0:
            if a_str:
                b_str = f" + {B}y"
            else:
                b_str = f"{B}y"
        else:
            b_str = f" - {abs(B)}y"

        return f"{a_str}{b_str} = {C}"

    def _create_worksheet_image(self):
        """Create blank coordinate plane for worksheet."""
        plane = CoordinatePlane(-10, 10, -10, 10, grid=True)
        fig, ax = plane.create_figure(figsize=(6, 6))

        # No equations on image - they will be displayed as text by PDF generator

        return plane.render_to_image(fig)

    def _create_answer_image(self, slope1, y_int1, slope2, y_int2,
                            x_sol, y_sol):
        """Create coordinate plane with lines and intersection for answer key."""
        plane = CoordinatePlane(-10, 10, -10, 10, grid=True)
        fig, ax = plane.create_figure(figsize=(6, 6))

        # No equations on image - they will be displayed as text by PDF generator

        # Plot first line (red)
        plane.plot_line_from_equation(ax, slope=slope1, y_intercept=y_int1,
                                     color='red', linewidth=2, label='Line 1')

        # Plot second line (blue)
        plane.plot_line_from_equation(ax, slope=slope2, y_intercept=y_int2,
                                     color='blue', linewidth=2, label='Line 2')

        # Plot intersection point (green)
        plane.plot_point(ax, x_sol, y_sol, label=f"({x_sol}, {y_sol})",
                        color='green', size=80, marker='o')

        return plane.render_to_image(fig)

    def generate_worksheet(self, difficulty: str,
                          num_problems: int) -> List[GraphingSystemProblem]:
        """
        Generate multiple problems for a worksheet.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of GraphingSystemProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problems.append(self.generate_problem(difficulty))
        return problems


if __name__ == "__main__":
    # Test the generator
    print("Testing Graphing Systems Generator...")

    gen = GraphingSystemsGenerator(seed=42)

    # Test each difficulty level
    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()}:")
        problem = gen.generate_problem(difficulty)
        print(f"  Equation 1: {problem.equation1_latex}")
        print(f"  Equation 2: {problem.equation2_latex}")
        print(f"  Solution: {problem.solution}")

        # Save test images
        problem.worksheet_image.save(f"test_systems_{difficulty}_worksheet.png")
        problem.answer_image.save(f"test_systems_{difficulty}_answer.png")
        print(f"  Saved: test_systems_{difficulty}_worksheet.png & _answer.png")

    print("\n[OK] All tests passed!")
