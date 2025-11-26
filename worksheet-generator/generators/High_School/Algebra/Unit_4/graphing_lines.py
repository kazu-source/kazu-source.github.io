"""
Generator for graphing lines on a coordinate plane worksheets.
Chapter 4: Linear Equations (Two Variables) - Graphing Lines
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from graphing_utils import CoordinatePlane
from PIL import Image


@dataclass
class GraphingLineProblem:
    """Represents a line graphing problem."""
    points: List[Tuple[int, int]]  # Two points defining the line
    equation_latex: str  # LaTeX representation of the points
    difficulty: str  # easy, medium, hard
    worksheet_image: object  # PIL Image for worksheet (blank grid)
    answer_image: object  # PIL Image for answer key (with line plotted)
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class GraphingLinesGenerator:
    """Generator for line graphing problems using two points."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> List[GraphingLineProblem]:
        """
        Generate multiple graphing problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
            num_problems: Number of problems to generate

        Returns:
            List of GraphingLineProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems

    def generate_problem(self, difficulty: str) -> GraphingLineProblem:
        """
        Generate a single line graphing problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            GraphingLineProblem object
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

    def _generate_easy(self) -> GraphingLineProblem:
        """
        Generate easy problem: two points with positive coordinates, small values.
        """
        # Generate two distinct points with small positive coordinates
        x1 = random.randint(1, 5)
        y1 = random.randint(1, 5)
        x2 = random.randint(6, 10)
        y2 = random.randint(1, 10)

        # Ensure points are different
        while x2 == x1 and y2 == y1:
            y2 = random.randint(1, 10)

        points = [(x1, y1), (x2, y2)]

        # Create worksheet image (blank grid)
        plane = CoordinatePlane(x_min=-1, x_max=10, y_min=-1, y_max=10, first_quadrant_only=False)
        fig, ax = plane.create_figure(figsize=(6, 6))
        worksheet_img = self._fig_to_image(fig)

        # Create answer key image (with line plotted)
        plane_ans = CoordinatePlane(x_min=-1, x_max=10, y_min=-1, y_max=10, first_quadrant_only=False)
        fig_ans, ax_ans = plane_ans.create_figure(figsize=(6, 6))

        # Plot the two points
        for i, (x, y) in enumerate(points):
            plane_ans.plot_point(ax_ans, x, y, label=f"({x},{y})", color='blue')

        # Plot the line through the two points
        self._plot_line_through_points(ax_ans, points[0], points[1])

        answer_img = self._fig_to_image(fig_ans)

        # Create equation latex representation
        equation_latex = f"({x1}, {y1}), ({x2}, {y2})"

        return GraphingLineProblem(
            points=points,
            equation_latex=equation_latex,
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img,
            x_min=-1,
            x_max=10,
            y_min=-1,
            y_max=10
        )

    def _generate_medium(self) -> GraphingLineProblem:
        """
        Generate medium problem: two points across all four quadrants.
        """
        # Generate two distinct points with mixed positive/negative coordinates
        x1 = random.randint(-8, 8)
        y1 = random.randint(-8, 8)
        x2 = random.randint(-8, 8)
        y2 = random.randint(-8, 8)

        # Ensure points are different and not too close
        while (x2 == x1 and y2 == y1) or (abs(x2 - x1) < 3 and abs(y2 - y1) < 3):
            x2 = random.randint(-8, 8)
            y2 = random.randint(-8, 8)

        points = [(x1, y1), (x2, y2)]

        # Create worksheet image (blank grid)
        plane = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig, ax = plane.create_figure(figsize=(6, 6))
        worksheet_img = self._fig_to_image(fig)

        # Create answer key image (with line plotted)
        plane_ans = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig_ans, ax_ans = plane_ans.create_figure(figsize=(6, 6))

        # Plot the two points
        for i, (x, y) in enumerate(points):
            plane_ans.plot_point(ax_ans, x, y, label=f"({x},{y})", color='blue')

        # Plot the line through the two points
        self._plot_line_through_points(ax_ans, points[0], points[1])

        answer_img = self._fig_to_image(fig_ans)

        # Create equation latex representation
        equation_latex = f"({x1}, {y1}), ({x2}, {y2})"

        return GraphingLineProblem(
            points=points,
            equation_latex=equation_latex,
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img,
            x_min=-10,
            x_max=10,
            y_min=-10,
            y_max=10
        )

    def _generate_hard(self) -> GraphingLineProblem:
        """
        Generate hard problem: two points with larger coordinates or fractional slopes.
        """
        # Generate two points that create interesting slopes (including vertical/horizontal)
        problem_type = random.choice(['steep', 'horizontal', 'vertical'])

        if problem_type == 'steep':
            # Steep slope
            x1 = random.randint(-8, 8)
            y1 = random.randint(-8, 8)
            x2 = x1 + random.choice([-2, -1, 1, 2])
            y2 = y1 + random.choice([-8, -7, 7, 8])
        elif problem_type == 'horizontal':
            # Horizontal line (slope = 0)
            y_val = random.randint(-8, 8)
            x1 = random.randint(-8, -2)
            x2 = random.randint(2, 8)
            y1 = y2 = y_val
        else:  # vertical
            # Vertical line (undefined slope)
            x_val = random.randint(-8, 8)
            x1 = x2 = x_val
            y1 = random.randint(-8, -2)
            y2 = random.randint(2, 8)

        points = [(x1, y1), (x2, y2)]

        # Create worksheet image (blank grid)
        plane = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig, ax = plane.create_figure(figsize=(6, 6))
        worksheet_img = self._fig_to_image(fig)

        # Create answer key image (with line plotted)
        plane_ans = CoordinatePlane(x_min=-10, x_max=10, y_min=-10, y_max=10)
        fig_ans, ax_ans = plane_ans.create_figure(figsize=(6, 6))

        # Plot the two points
        for i, (x, y) in enumerate(points):
            plane_ans.plot_point(ax_ans, x, y, label=f"({x},{y})", color='blue')

        # Plot the line through the two points
        self._plot_line_through_points(ax_ans, points[0], points[1])

        answer_img = self._fig_to_image(fig_ans)

        # Create equation latex representation
        equation_latex = f"({x1}, {y1}), ({x2}, {y2})"

        return GraphingLineProblem(
            points=points,
            equation_latex=equation_latex,
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img,
            x_min=-10,
            x_max=10,
            y_min=-10,
            y_max=10
        )

    def _generate_challenge(self) -> GraphingLineProblem:
        """
        Generate challenge problem: very steep/flat slopes, larger negative coordinates,
        fractional slopes with distant points.
        """
        # Generate two points that create very challenging slopes
        problem_type = random.choice(['very_steep', 'very_flat', 'complex_fractional', 'negative_extremes'])

        if problem_type == 'very_steep':
            # Very steep slope with large negative values
            x1 = random.randint(-10, 10)
            y1 = random.randint(-10, 10)
            x2 = x1 + random.choice([-1, 1])
            y2 = y1 + random.choice([-12, -11, -10, 10, 11, 12])
        elif problem_type == 'very_flat':
            # Very flat slope with distant points
            x1 = random.randint(-10, -5)
            y1 = random.randint(-10, 10)
            x2 = random.randint(5, 10)
            y2 = y1 + random.choice([-2, -1, 1, 2])
        elif problem_type == 'complex_fractional':
            # Create fractional slope with challenging coordinates
            x1 = random.randint(-9, 9)
            y1 = random.randint(-9, 9)
            # Create points that result in fractional slopes like 5/7, -8/3, etc.
            dx = random.choice([-7, -5, -3, 3, 5, 7])
            dy = random.choice([-9, -8, -6, 6, 8, 9])
            x2 = x1 + dx
            y2 = y1 + dy
            # Keep within bounds
            x2 = max(-10, min(10, x2))
            y2 = max(-10, min(10, y2))
        else:  # negative_extremes
            # Both points in negative regions with complex relationships
            x1 = random.randint(-10, -5)
            y1 = random.randint(-10, -5)
            x2 = random.randint(-10, 5)
            y2 = random.randint(-10, 5)
            # Ensure points are different and not too close
            while (x2 == x1 and y2 == y1) or (abs(x2 - x1) < 4 and abs(y2 - y1) < 4):
                x2 = random.randint(-10, 5)
                y2 = random.randint(-10, 5)

        points = [(x1, y1), (x2, y2)]

        # Create worksheet image (blank grid)
        plane = CoordinatePlane(x_min=-12, x_max=12, y_min=-12, y_max=12)
        fig, ax = plane.create_figure(figsize=(6, 6))
        worksheet_img = self._fig_to_image(fig)

        # Create answer key image (with line plotted)
        plane_ans = CoordinatePlane(x_min=-12, x_max=12, y_min=-12, y_max=12)
        fig_ans, ax_ans = plane_ans.create_figure(figsize=(6, 6))

        # Plot the two points
        for i, (x, y) in enumerate(points):
            plane_ans.plot_point(ax_ans, x, y, label=f"({x},{y})", color='blue')

        # Plot the line through the two points
        self._plot_line_through_points(ax_ans, points[0], points[1])

        answer_img = self._fig_to_image(fig_ans)

        # Create equation latex representation
        equation_latex = f"({x1}, {y1}), ({x2}, {y2})"

        return GraphingLineProblem(
            points=points,
            equation_latex=equation_latex,
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img,
            x_min=-12,
            x_max=12,
            y_min=-12,
            y_max=12
        )

    def _plot_line_through_points(self, ax, point1, point2):
        """Plot a line through two points."""
        x1, y1 = point1
        x2, y2 = point2

        # Get axis limits
        x_lim = ax.get_xlim()
        y_lim = ax.get_ylim()

        # Handle vertical line
        if x2 == x1:
            ax.axvline(x=x1, color='red', linewidth=2, zorder=2)
        # Handle horizontal line
        elif y2 == y1:
            ax.axhline(y=y1, color='red', linewidth=2, zorder=2)
        # Regular line
        else:
            # Calculate slope and intercept
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1

            # Create x values across the visible range
            x_vals = [x_lim[0], x_lim[1]]
            y_vals = [slope * x + intercept for x in x_vals]

            ax.plot(x_vals, y_vals, color='red', linewidth=2, zorder=2)

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
    gen = GraphingLinesGenerator()

    print("Testing Graphing Lines Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. Graph the line through points: {problem.points}")
