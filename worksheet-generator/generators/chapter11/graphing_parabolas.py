"""
Generator for graphing parabola worksheets.
Chapter 11: Quadratic Functions and Parabolas
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from graphing_utils import CoordinatePlane


@dataclass
class ParabolaGraphingProblem:
    """Represents a parabola graphing problem."""
    equation_latex: str  # Equation in LaTeX format
    a: float  # Vertical stretch/compression factor (negative = upside down)
    h: float  # X-coordinate of vertex
    k: float  # Y-coordinate of vertex
    vertex: Tuple[float, float]  # (h, k)
    opens_upward: bool  # True if a > 0
    difficulty: str  # easy, medium, hard, challenge
    worksheet_image: object  # PIL Image for worksheet (blank grid with equation)
    answer_image: object  # PIL Image for answer key (with parabola and vertex)
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class ParabolaGraphingGenerator:
    """Generator for parabola graphing problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def generate_problem(self, difficulty: str) -> ParabolaGraphingProblem:
        """
        Generate a single parabola graphing problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            ParabolaGraphingProblem object
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

    def _generate_easy(self) -> ParabolaGraphingProblem:
        """
        Generate easy problem: y = x² or y = -x² (vertex at origin, a = ±1)
        """
        # Simple parabola with vertex at origin
        a = random.choice([-1, 1])
        h = 0
        k = 0

        # Format equation
        if a == 1:
            eq_latex = "y = x^2"
        else:
            eq_latex = "y = -x^2"

        # Create images
        worksheet_img = self._create_worksheet_image()
        answer_img = self._create_answer_image(a, h, k)

        return ParabolaGraphingProblem(
            equation_latex=eq_latex,
            a=a,
            h=h,
            k=k,
            vertex=(h, k),
            opens_upward=(a > 0),
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_medium(self) -> ParabolaGraphingProblem:
        """
        Generate medium problem: y = (x - h)² + k with integer h, k
        Vertex form, a = 1, vertex not at origin
        """
        a = 1
        h = random.randint(-4, 4)
        k = random.randint(-4, 4)

        # Format equation: y = (x - h)² + k
        eq_latex = self._format_vertex_form(a, h, k)

        # Create images
        worksheet_img = self._create_worksheet_image()
        answer_img = self._create_answer_image(a, h, k)

        return ParabolaGraphingProblem(
            equation_latex=eq_latex,
            a=a,
            h=h,
            k=k,
            vertex=(h, k),
            opens_upward=(a > 0),
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_hard(self) -> ParabolaGraphingProblem:
        """
        Generate hard problem: y = a(x - h)² + k with a ≠ 1, integer h, k
        Includes vertical stretch/compression and flips
        """
        # Choose a from {-2, -1, -0.5, 0.5, 2}
        a = random.choice([-2, -1, -0.5, 0.5, 2])
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)

        # Format equation
        eq_latex = self._format_vertex_form(a, h, k)

        # Create images
        worksheet_img = self._create_worksheet_image()
        answer_img = self._create_answer_image(a, h, k)

        return ParabolaGraphingProblem(
            equation_latex=eq_latex,
            a=a,
            h=h,
            k=k,
            vertex=(h, k),
            opens_upward=(a > 0),
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_challenge(self) -> ParabolaGraphingProblem:
        """
        Generate challenge problem: y = a(x - h)² + k with fractional a, h, or k
        More complex vertex positions and stretch factors
        """
        # Choose a from fractional values
        a_choices = [-3, -2, -1.5, -1, -0.5, -0.25, 0.25, 0.5, 1, 1.5, 2, 3]
        a = random.choice(a_choices)

        # Allow fractional vertex coordinates
        h = random.randint(-8, 8) / 2.0  # 0.5 increments
        k = random.randint(-8, 8) / 2.0

        # Format equation
        eq_latex = self._format_vertex_form(a, h, k)

        # Create images
        worksheet_img = self._create_worksheet_image()
        answer_img = self._create_answer_image(a, h, k)

        return ParabolaGraphingProblem(
            equation_latex=eq_latex,
            a=a,
            h=h,
            k=k,
            vertex=(h, k),
            opens_upward=(a > 0),
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _format_vertex_form(self, a: float, h: float, k: float) -> str:
        """Format parabola equation in vertex form: y = a(x - h)² + k"""
        # Handle a coefficient
        if a == 1:
            a_str = ""
        elif a == -1:
            a_str = "-"
        elif a == int(a):
            a_str = f"{int(a)}"
        else:
            a_str = f"{a}"

        # Handle h (x - h)
        if h == 0:
            h_str = "x"
        elif h > 0:
            if h == int(h):
                h_str = f"(x - {int(h)})"
            else:
                h_str = f"(x - {h})"
        else:  # h < 0
            if h == int(h):
                h_str = f"(x + {int(abs(h))})"
            else:
                h_str = f"(x + {abs(h)})"

        # Handle k
        if k == 0:
            k_str = ""
        elif k > 0:
            if k == int(k):
                k_str = f" + {int(k)}"
            else:
                k_str = f" + {k}"
        else:  # k < 0
            if k == int(k):
                k_str = f" - {int(abs(k))}"
            else:
                k_str = f" - {abs(k)}"

        return f"y = {a_str}{h_str}^2{k_str}"

    def _create_worksheet_image(self):
        """Create blank coordinate plane for worksheet."""
        plane = CoordinatePlane(-10, 10, -10, 10, grid=True)
        fig, ax = plane.create_figure(figsize=(6, 6))

        # No equation on image - it will be displayed as text by PDF generator

        return plane.render_to_image(fig)

    def _create_answer_image(self, a, h, k):
        """Create coordinate plane with parabola and vertex for answer key."""
        plane = CoordinatePlane(-10, 10, -10, 10, grid=True)
        fig, ax = plane.create_figure(figsize=(6, 6))

        # No equation on image - it will be displayed as text by PDF generator

        # Plot parabola (purple)
        plane.plot_parabola(ax, a=a, h=h, k=k, color='purple', linewidth=2)

        # Vertex is already plotted by plot_parabola, but let's add label
        # The plot_parabola method plots the vertex, we just ensure it's labeled
        vertex_label = f"Vertex: ({h}, {k})"
        fig.text(0.5, 0.05, vertex_label, ha='center', va='bottom',
                fontsize=10, bbox=dict(boxstyle='round,pad=0.5',
                facecolor='yellow', alpha=0.7))

        return plane.render_to_image(fig)

    def generate_worksheet(self, difficulty: str,
                          num_problems: int) -> list:
        """
        Generate multiple problems for a worksheet.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of ParabolaGraphingProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problems.append(self.generate_problem(difficulty))
        return problems


if __name__ == "__main__":
    # Test the generator
    print("Testing Parabola Graphing Generator...")

    gen = ParabolaGraphingGenerator(seed=42)

    # Test each difficulty level
    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()}:")
        problem = gen.generate_problem(difficulty)
        print(f"  Equation: {problem.equation_latex}")
        print(f"  Vertex: {problem.vertex}")
        print(f"  Opens: {'upward' if problem.opens_upward else 'downward'}")
        print(f"  a = {problem.a}")

        # Save test images
        problem.worksheet_image.save(f"test_parabola_{difficulty}_worksheet.png")
        problem.answer_image.save(f"test_parabola_{difficulty}_answer.png")
        print(f"  Saved: test_parabola_{difficulty}_worksheet.png & _answer.png")

    print("\n[OK] All tests passed!")
