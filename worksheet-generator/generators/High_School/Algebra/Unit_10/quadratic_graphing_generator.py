"""
Quadratic Graphing Generator - Unit 10
Generates problems for graphing quadratic functions using vertex form, standard form, and factored form
"""

import random
import math
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional


@dataclass
class QuadraticGraphProblem:
    """Represents a quadratic graphing problem."""
    latex: str  # LaTeX formatted problem
    vertex: Tuple[float, float]  # Vertex coordinates (h, k)
    x_intercepts: List[float]  # X-intercepts (roots)
    y_intercept: float  # Y-intercept
    axis_of_symmetry: float  # x = h
    form: str  # 'vertex', 'standard', or 'factored'
    difficulty: str
    a_value: float  # Coefficient affecting direction and width
    key_points: List[Tuple[float, float]]  # Additional points for graphing


class QuadraticGraphingGenerator:
    """Generates quadratic graphing problems."""

    def __init__(self, seed=None):
        """Initialize the quadratic graphing generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[QuadraticGraphProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of QuadraticGraphProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> QuadraticGraphProblem:
        """Generate a single quadratic graphing problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _calculate_quadratic_properties(self, a: float, b: float, c: float) -> Dict:
        """
        Calculate properties of quadratic ax^2 + bx + c.
        Returns dict with vertex, intercepts, axis of symmetry.
        """
        # Vertex x-coordinate: -b/(2a)
        h = -b / (2 * a)
        # Vertex y-coordinate: f(h)
        k = a * h * h + b * h + c

        # Y-intercept is c (when x = 0)
        y_intercept = c

        # X-intercepts using quadratic formula
        discriminant = b * b - 4 * a * c
        if discriminant > 0:
            sqrt_disc = math.sqrt(discriminant)
            x1 = (-b + sqrt_disc) / (2 * a)
            x2 = (-b - sqrt_disc) / (2 * a)
            x_intercepts = sorted([x1, x2])
        elif discriminant == 0:
            x_intercepts = [-b / (2 * a)]
        else:
            x_intercepts = []

        return {
            'vertex': (h, k),
            'x_intercepts': x_intercepts,
            'y_intercept': y_intercept,
            'axis_of_symmetry': h
        }

    def _generate_key_points(self, a: float, h: float, k: float) -> List[Tuple[float, float]]:
        """Generate additional points on the parabola for graphing."""
        points = []
        # Generate points 1 and 2 units away from vertex
        for dx in [-2, -1, 1, 2]:
            x = h + dx
            y = a * (x - h) ** 2 + k
            points.append((x, y))
        return points

    def _generate_easy(self) -> QuadraticGraphProblem:
        """Generate easy graphing problems (vertex form with integer coordinates)."""
        form_type = random.choice(['vertex_simple', 'standard_simple', 'factored_simple'])

        if form_type == 'vertex_simple':
            # Vertex form: a(x - h)^2 + k
            a = random.choice([-2, -1, 1, 2])
            h = random.randint(-3, 3)
            k = random.randint(-4, 4)

            if a == 1:
                if h == 0 and k == 0:
                    latex = f"\\text{{Graph: }} y = x^2"
                elif h == 0:
                    latex = f"\\text{{Graph: }} y = x^2 {k:+d}".replace("+-", "-")
                elif k == 0:
                    latex = f"\\text{{Graph: }} y = (x {-h:+d})^2".replace("+-", "-")
                else:
                    latex = f"\\text{{Graph: }} y = (x {-h:+d})^2 {k:+d}".replace("+-", "-")
            elif a == -1:
                latex = f"\\text{{Graph: }} y = -(x {-h:+d})^2 {k:+d}".replace("+-", "-")
            else:
                latex = f"\\text{{Graph: }} y = {a}(x {-h:+d})^2 {k:+d}".replace("+-", "-")

            # Calculate properties
            # Expand to standard form: a(x-h)^2 + k = ax^2 - 2ahx + ah^2 + k
            b = -2 * a * h
            c = a * h * h + k

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'vertex'

        elif form_type == 'standard_simple':
            # Standard form: ax^2 + bx + c
            a = random.choice([-1, 1])
            b = random.randint(-4, 4)
            c = random.randint(-5, 5)

            if a == 1:
                if b == 0:
                    latex = f"\\text{{Graph: }} y = x^2 {c:+d}".replace("+-", "-")
                else:
                    latex = f"\\text{{Graph: }} y = x^2 {b:+d}x {c:+d}".replace("+-", "-")
            else:
                latex = f"\\text{{Graph: }} y = -x^2 {b:+d}x {c:+d}".replace("+-", "-")

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'standard'

        else:  # factored_simple
            # Factored form: a(x - r1)(x - r2)
            a = random.choice([-1, 1])
            r1 = random.randint(-3, 3)
            r2 = random.randint(-3, 3)

            if a == 1:
                latex = f"\\text{{Graph: }} y = (x {-r1:+d})(x {-r2:+d})".replace("+-", "-")
            else:
                latex = f"\\text{{Graph: }} y = -(x {-r1:+d})(x {-r2:+d})".replace("+-", "-")

            # Expand to standard form
            b = -a * (r1 + r2)
            c = a * r1 * r2

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'factored'

        return QuadraticGraphProblem(
            latex=latex,
            vertex=props['vertex'],
            x_intercepts=props['x_intercepts'],
            y_intercept=props['y_intercept'],
            axis_of_symmetry=props['axis_of_symmetry'],
            form=form,
            difficulty='easy',
            a_value=a,
            key_points=self._generate_key_points(a, props['vertex'][0], props['vertex'][1])
        )

    def _generate_medium(self) -> QuadraticGraphProblem:
        """Generate medium graphing problems (with coefficients, transformations)."""
        form_type = random.choice(['vertex_transform', 'standard_complete', 'factored_stretch'])

        if form_type == 'vertex_transform':
            # Vertex form with stretching/compression
            a = random.choice([-3, -2, -0.5, 0.5, 2, 3])
            h = random.randint(-4, 4)
            k = random.randint(-6, 6)

            if abs(a) < 1:
                a_str = f"\\frac{{1}}{{{int(1/abs(a))}}}"
                if a < 0:
                    a_str = "-" + a_str
            else:
                a_str = str(a) if a != 1 else ""
                if a == -1:
                    a_str = "-"

            latex = f"\\text{{Graph: }} y = {a_str}(x {-h:+d})^2 {k:+d}".replace("+-", "-")

            # Calculate standard form coefficients
            b = -2 * a * h
            c = a * h * h + k

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'vertex'

        elif form_type == 'standard_complete':
            # Standard form that requires completing the square
            a = random.choice([-2, -1, 1, 2])
            # Make b even for easier completing the square
            b = 2 * random.randint(-3, 3)
            c = random.randint(-8, 8)

            if a == 1:
                latex = f"\\text{{Graph: }} y = x^2 {b:+d}x {c:+d}".replace("+-", "-")
            else:
                latex = f"\\text{{Graph: }} y = {a}x^2 {b:+d}x {c:+d}".replace("+-", "-")

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'standard'

        else:  # factored_stretch
            # Factored form with coefficient
            a = random.choice([-2, 2, 3])
            r1 = random.randint(-4, 4)
            r2 = random.randint(-4, 4)

            latex = f"\\text{{Graph: }} y = {a}(x {-r1:+d})(x {-r2:+d})".replace("+-", "-")

            # Expand to standard form
            b = -a * (r1 + r2)
            c = a * r1 * r2

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'factored'

        return QuadraticGraphProblem(
            latex=latex,
            vertex=props['vertex'],
            x_intercepts=props['x_intercepts'],
            y_intercept=props['y_intercept'],
            axis_of_symmetry=props['axis_of_symmetry'],
            form=form,
            difficulty='medium',
            a_value=a,
            key_points=self._generate_key_points(a, props['vertex'][0], props['vertex'][1])
        )

    def _generate_hard(self) -> QuadraticGraphProblem:
        """Generate hard graphing problems (multiple forms, word problems)."""
        form_type = random.choice(['convert_forms', 'from_description', 'application'])

        if form_type == 'convert_forms':
            # Give equation in one form, ask to graph and convert
            a = random.choice([-2, -1, 1, 2])
            h = random.randint(-3, 3)
            k = random.randint(-5, 5)

            # Start with vertex form
            vertex_form = f"y = {a if a != 1 else ''}(x {-h:+d})^2 {k:+d}".replace("+-", "-")
            if a == -1:
                vertex_form = f"y = -(x {-h:+d})^2 {k:+d}".replace("+-", "-")

            # Expand to standard form
            b = -2 * a * h
            c = a * h * h + k

            latex = f"\\text{{Graph }} {vertex_form} \\text{{ and write in standard form}}"

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'vertex'

        elif form_type == 'from_description':
            # Create parabola from description
            vertex_h = random.randint(-3, 3)
            vertex_k = random.randint(-4, 4)
            opens = random.choice(['upward', 'downward'])
            a = random.choice([1, 2]) if opens == 'upward' else random.choice([-1, -2])

            latex = f"\\text{{Graph parabola with vertex ({vertex_h}, {vertex_k}) opening {opens}}}"

            # Calculate properties
            b = -2 * a * vertex_h
            c = a * vertex_h * vertex_h + vertex_k

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'description'

        else:  # application
            # Application problem (projectile motion)
            v0 = random.choice([32, 48, 64])  # Initial velocity
            h0 = random.choice([0, 16, 32])  # Initial height

            latex = f"\\text{{Graph height of projectile: }} h(t) = -16t^2 + {v0}t + {h0}"

            # This is in form at^2 + bt + c where a = -16, b = v0, c = h0
            props = self._calculate_quadratic_properties(-16, v0, h0)
            form = 'application'
            a = -16

        return QuadraticGraphProblem(
            latex=latex,
            vertex=props['vertex'],
            x_intercepts=props['x_intercepts'],
            y_intercept=props['y_intercept'],
            axis_of_symmetry=props['axis_of_symmetry'],
            form=form,
            difficulty='hard',
            a_value=a,
            key_points=self._generate_key_points(a, props['vertex'][0], props['vertex'][1])
        )

    def _generate_challenge(self) -> QuadraticGraphProblem:
        """Generate challenge graphing problems (transformations, systems)."""
        form_type = random.choice(['transformation_sequence', 'find_equation', 'system_quadratic'])

        if form_type == 'transformation_sequence':
            # Apply sequence of transformations
            # Start with y = x^2, apply transformations
            shifts = {
                'right': random.randint(1, 3),
                'up': random.randint(-4, 4),
                'stretch': random.choice([0.5, 2, 3])
            }

            h = shifts['right']
            k = shifts['up']
            a = shifts['stretch']

            latex = f"\\text{{Graph: Start with }} y = x^2, "
            latex += f"\\text{{shift right {h}, "
            if k > 0:
                latex += f"up {k}, "
            else:
                latex += f"down {-k}, "
            if a > 1:
                latex += f"stretch vertically by {a}}}"
            else:
                latex += f"compress vertically by {a}}}"

            # Result is y = a(x - h)^2 + k
            b = -2 * a * h
            c = a * h * h + k

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'transformation'

        elif form_type == 'find_equation':
            # Find equation from given points
            vertex = (random.randint(-3, 3), random.randint(-4, 4))
            # Another point on the parabola
            other_x = vertex[0] + random.randint(1, 3)
            a = random.choice([-2, -1, 1, 2])
            other_y = a * (other_x - vertex[0]) ** 2 + vertex[1]

            latex = f"\\text{{Find and graph parabola with vertex {vertex} passing through ({other_x}, {other_y})}}"

            # Calculate properties
            h, k = vertex
            b = -2 * a * h
            c = a * h * h + k

            props = self._calculate_quadratic_properties(a, b, c)
            form = 'find_equation'

        else:  # system_quadratic
            # System with quadratic and linear
            # Parabola y = x^2 + bx + c
            b = random.randint(-4, 4)
            c = random.randint(-3, 3)
            # Line y = mx + n
            m = random.randint(-2, 2)
            n = random.randint(-3, 3)

            latex = f"\\text{{Graph system: }} y = x^2 {b:+d}x {c:+d} \\text{{ and }} y = {m}x {n:+d}".replace("+-", "-")

            props = self._calculate_quadratic_properties(1, b, c)
            form = 'system'
            a = 1

        return QuadraticGraphProblem(
            latex=latex,
            vertex=props['vertex'],
            x_intercepts=props['x_intercepts'],
            y_intercept=props['y_intercept'],
            axis_of_symmetry=props['axis_of_symmetry'],
            form=form,
            difficulty='challenge',
            a_value=a,
            key_points=self._generate_key_points(a, props['vertex'][0], props['vertex'][1])
        )


if __name__ == "__main__":
    # Test the generator
    gen = QuadraticGraphingGenerator()

    print("Testing Quadratic Graphing Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Vertex: {problem.vertex}")
            print(f"   X-intercepts: {problem.x_intercepts}")
            print(f"   Y-intercept: {problem.y_intercept}")
            print(f"   Axis of symmetry: x = {problem.axis_of_symmetry}")
            print(f"   Opens: {'upward' if problem.a_value > 0 else 'downward'}")
            print(f"   Form: {problem.form}")
            print(f"   Key points: {problem.key_points[:2]}...")