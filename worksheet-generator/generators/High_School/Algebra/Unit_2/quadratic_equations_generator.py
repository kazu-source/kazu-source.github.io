"""
Quadratic Equations Generator - Unit 10
Generates problems for solving quadratic equations using various methods
"""

import random
import math
from dataclasses import dataclass
from typing import List, Tuple, Optional, Union


@dataclass
class QuadraticProblem:
    """Represents a quadratic equation problem."""
    latex: str  # LaTeX formatted problem
    solution: str  # The solution(s)
    difficulty: str
    method: str  # Method used to solve (square_root, factoring, vertex, standard)
    graph_info: dict = None  # Optional graphing information


class QuadraticEquationsGenerator:
    """Generates quadratic equation problems."""

    def __init__(self, seed=None):
        """Initialize the quadratic equations generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[QuadraticProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of QuadraticProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> QuadraticProblem:
        """Generate a single quadratic problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _format_solutions(self, solutions: List[Union[int, float]]) -> str:
        """Format solutions nicely."""
        if not solutions:
            return "No real solutions"
        elif len(solutions) == 1:
            if isinstance(solutions[0], int) or solutions[0].is_integer():
                return f"x = {int(solutions[0])}"
            else:
                return f"x = {solutions[0]:.2f}"
        else:
            formatted = []
            for sol in sorted(solutions):
                if isinstance(sol, int) or (isinstance(sol, float) and sol.is_integer()):
                    formatted.append(f"x = {int(sol)}")
                else:
                    formatted.append(f"x = {sol:.2f}")
            return " or ".join(formatted)

    def _generate_easy(self) -> QuadraticProblem:
        """Generate easy quadratic problems (simple square roots, factoring with integers)."""
        problem_type = random.choice(['square_root_simple', 'factor_simple', 'vertex_form_simple'])

        if problem_type == 'square_root_simple':
            # Solve x^2 = c
            c = random.choice([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
            sqrt_c = int(math.sqrt(c))

            latex = f"\\text{{Solve: }} x^2 = {c}"
            solution = f"x = \\pm{sqrt_c}"
            method = 'square_root'

        elif problem_type == 'factor_simple':
            # Solve (x - p)(x - q) = 0
            p = random.randint(-5, 5)
            q = random.randint(-5, 5)

            # Expand to standard form
            a = 1
            b = -(p + q)
            c = p * q

            if b == 0:
                latex = f"\\text{{Solve by factoring: }} x^2 {c:+d} = 0"
            elif b == 1:
                latex = f"\\text{{Solve by factoring: }} x^2 + x {c:+d} = 0"
            elif b == -1:
                latex = f"\\text{{Solve by factoring: }} x^2 - x {c:+d} = 0"
            else:
                latex = f"\\text{{Solve by factoring: }} x^2 {b:+d}x {c:+d} = 0"

            latex = latex.replace("+-", "-")
            solution = self._format_solutions([p, q])
            method = 'factoring'

        else:  # vertex_form_simple
            # Solve from vertex form (x - h)^2 = k
            h = random.randint(-5, 5)
            k = random.choice([0, 1, 4, 9, 16, 25])

            if k == 0:
                latex = f"\\text{{Solve: }} (x {-h:+d})^2 = 0".replace("+-", "-")
                solution = f"x = {h}"
            else:
                sqrt_k = int(math.sqrt(k))
                latex = f"\\text{{Solve: }} (x {-h:+d})^2 = {k}".replace("+-", "-")
                solution = self._format_solutions([h - sqrt_k, h + sqrt_k])

            method = 'vertex_form'

        return QuadraticProblem(
            latex=latex,
            solution=solution,
            difficulty='easy',
            method=method
        )

    def _generate_medium(self) -> QuadraticProblem:
        """Generate medium quadratic problems (with coefficients, standard form)."""
        problem_type = random.choice(['square_root_coeff', 'standard_form', 'factor_with_coeff'])

        if problem_type == 'square_root_coeff':
            # Solve ax^2 = c
            a = random.randint(2, 5)
            c = random.choice([8, 18, 32, 50, 72, 98])

            latex = f"\\text{{Solve: }} {a}x^2 = {c}"

            # x^2 = c/a
            if c % a == 0:
                value = c // a
                if math.sqrt(value).is_integer():
                    sqrt_val = int(math.sqrt(value))
                    solution = f"x = \\pm{sqrt_val}"
                else:
                    solution = f"x = \\pm\\sqrt{{{value}}}"
            else:
                solution = f"x = \\pm\\sqrt{{\\frac{{{c}}}{{{a}}}}}"

            method = 'square_root'

        elif problem_type == 'standard_form':
            # Standard form with nice discriminant
            a = 1
            b = random.randint(-8, 8)
            # Ensure discriminant is a perfect square
            discriminant_sqrt = random.randint(0, 6)
            discriminant = discriminant_sqrt ** 2
            # b^2 - 4ac = discriminant
            # c = (b^2 - discriminant) / 4
            c = (b * b - discriminant) // 4

            latex = f"\\text{{Solve: }} x^2 {b:+d}x {c:+d} = 0".replace("+-", "-")

            # Using quadratic formula
            if discriminant == 0:
                x = -b / 2
                solution = self._format_solutions([x])
            else:
                x1 = (-b + discriminant_sqrt) / 2
                x2 = (-b - discriminant_sqrt) / 2
                solution = self._format_solutions([x1, x2])

            method = 'standard_form'

        else:  # factor_with_coeff
            # Factor ax^2 + bx + c where a > 1
            a = random.randint(2, 3)
            # Choose factors that work nicely
            p = random.randint(-3, 3)
            q = random.randint(-3, 3)

            # (ax - p)(x - q) = ax^2 - (aq + p)x + pq
            b = -(a * q + p)
            c = p * q

            latex = f"\\text{{Solve by factoring: }} {a}x^2 {b:+d}x {c:+d} = 0".replace("+-", "-")

            x1 = p / a
            x2 = q

            solution = self._format_solutions([x1, x2])
            method = 'factoring'

        return QuadraticProblem(
            latex=latex,
            solution=solution,
            difficulty='medium',
            method=method
        )

    def _generate_hard(self) -> QuadraticProblem:
        """Generate hard quadratic problems (completing the square, complex vertex form)."""
        problem_type = random.choice(['vertex_form_complex', 'complete_square_needed', 'word_problem'])

        if problem_type == 'vertex_form_complex':
            # Vertex form a(x - h)^2 + k = 0
            a = random.choice([-2, -1, 1, 2, 3])
            h = random.randint(-5, 5)
            k = random.randint(-20, 20)

            if a == 1:
                latex = f"\\text{{Solve: }} (x {-h:+d})^2 {k:+d} = 0".replace("+-", "-")
            else:
                latex = f"\\text{{Solve: }} {a}(x {-h:+d})^2 {k:+d} = 0".replace("+-", "-")

            # a(x - h)^2 = -k
            # (x - h)^2 = -k/a
            value = -k / a

            if value < 0:
                solution = "No real solutions"
            elif value == 0:
                solution = f"x = {h}"
            else:
                sqrt_val = math.sqrt(value)
                if sqrt_val.is_integer():
                    sqrt_val = int(sqrt_val)
                    solution = self._format_solutions([h - sqrt_val, h + sqrt_val])
                else:
                    solution = f"x = {h} \\pm \\sqrt{{{value:.2f}}}"

            method = 'vertex_form'
            graph_info = {'vertex': (h, k), 'a': a}

        elif problem_type == 'complete_square_needed':
            # Problem that benefits from completing the square
            a = 1
            b = 2 * random.randint(-5, 5)  # Even coefficient for easier completing
            c = random.randint(-10, 10)

            latex = f"\\text{{Solve by completing the square: }} x^2 {b:+d}x {c:+d} = 0".replace("+-", "-")

            # Complete the square
            # x^2 + bx + c = 0
            # (x + b/2)^2 - (b/2)^2 + c = 0
            # (x + b/2)^2 = (b/2)^2 - c

            value = (b / 2) ** 2 - c

            if value < 0:
                solution = "No real solutions"
            elif value == 0:
                solution = f"x = {-b // 2}"
            else:
                sqrt_val = math.sqrt(value)
                x1 = -b / 2 + sqrt_val
                x2 = -b / 2 - sqrt_val
                solution = self._format_solutions([x1, x2])

            method = 'completing_square'
            graph_info = {'vertex': (-b / 2, -value), 'a': 1}

        else:  # word_problem
            # Projectile motion problem
            v0 = random.choice([16, 32, 48, 64])  # Initial velocity
            h0 = random.choice([0, 10, 20, 30, 40])  # Initial height

            latex = f"\\text{{A ball is thrown upward at {v0} ft/s from {h0} ft height. "
            latex += f"When does it hit the ground? (h = -16t^2 + {v0}t + {h0})}}"

            # Solve -16t^2 + v0*t + h0 = 0
            # Using quadratic formula
            discriminant = v0 ** 2 + 64 * h0
            sqrt_disc = math.sqrt(discriminant)

            t1 = (v0 + sqrt_disc) / 32  # Positive solution
            t2 = (v0 - sqrt_disc) / 32  # May be negative

            if t2 > 0:
                solution = f"t = {t1:.2f} seconds"
            else:
                solution = f"t = {t1:.2f} seconds"

            method = 'word_problem'
            graph_info = None

        return QuadraticProblem(
            latex=latex,
            solution=solution,
            difficulty='hard',
            method=method,
            graph_info=graph_info
        )

    def _generate_challenge(self) -> QuadraticProblem:
        """Generate challenge quadratic problems (systems, complex applications)."""
        problem_type = random.choice(['discriminant_analysis', 'parameter_problem', 'optimization'])

        if problem_type == 'discriminant_analysis':
            # Find values of k for which equation has specific solution types
            a = 1
            b = random.randint(-6, 6)

            solution_type = random.choice(['two_real', 'one_real', 'no_real'])

            if solution_type == 'two_real':
                latex = f"\\text{{Find k so that }} x^2 {b:+d}x + k = 0 \\text{{ has two distinct real solutions}}".replace("+-", "-")
                # Need b^2 - 4k > 0
                # k < b^2/4
                solution = f"k < {b**2 / 4}"
            elif solution_type == 'one_real':
                latex = f"\\text{{Find k so that }} x^2 {b:+d}x + k = 0 \\text{{ has exactly one real solution}}".replace("+-", "-")
                # Need b^2 - 4k = 0
                # k = b^2/4
                solution = f"k = {b**2 / 4}"
            else:
                latex = f"\\text{{Find k so that }} x^2 {b:+d}x + k = 0 \\text{{ has no real solutions}}".replace("+-", "-")
                # Need b^2 - 4k < 0
                # k > b^2/4
                solution = f"k > {b**2 / 4}"

            method = 'discriminant'

        elif problem_type == 'parameter_problem':
            # Find parameter value given a root
            root = random.randint(-5, 5)
            other_root = random.randint(-5, 5)

            # If roots are r and s, then equation is x^2 - (r+s)x + rs = 0
            b = -(root + other_root)
            c = root * other_root

            latex = f"\\text{{If }} x = {root} \\text{{ is a solution to }} x^2 {b:+d}x + c = 0, \\text{{ find c}}".replace("+-", "-")
            solution = f"c = {c}"

            method = 'parameter'

        else:  # optimization
            # Maximum/minimum area or revenue problem
            perimeter = random.choice([20, 24, 30, 40])

            latex = f"\\text{{A rectangle has perimeter {perimeter} ft. Find dimensions for maximum area.}}"

            # If length is x, width is (perimeter - 2x)/2 = perimeter/2 - x
            # Area = x * (perimeter/2 - x) = -x^2 + (perimeter/2)x
            # Maximum at x = perimeter/4

            length = perimeter / 4
            width = perimeter / 4
            max_area = length * width

            solution = f"Square with side {length:.0f} ft, area = {max_area:.0f} sq ft"

            method = 'optimization'

        return QuadraticProblem(
            latex=latex,
            solution=solution,
            difficulty='challenge',
            method=method
        )


if __name__ == "__main__":
    # Test the generator
    gen = QuadraticEquationsGenerator()

    print("Testing Quadratic Equations Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Method: {problem.method}")
            if problem.graph_info:
                print(f"   Graph info: {problem.graph_info}")