"""
Simplified Quadratic Functions Generator
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation
from typing import List


class QuadraticFunctionsSimpleGenerator:
    """Generator for quadratic functions problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate a worksheet of quadratic functions problems."""
        problems = []
        for _ in range(num_problems):
            if difficulty == 'easy':
                problem = self._generate_easy()
            elif difficulty == 'medium':
                problem = self._generate_medium()
            elif difficulty == 'hard':
                problem = self._generate_hard()
            else:  # challenge
                problem = self._generate_challenge()
            problems.append(problem)
        return problems

    def _generate_easy(self) -> Equation:
        """Generate easy: Find vertex, axis of symmetry, or direction"""
        problem_type = random.choice(['vertex', 'axis', 'direction'])

        # Generate simple quadratic in vertex form
        h = random.randint(-5, 5)
        k = random.randint(-10, 10)
        a = random.choice([-2, -1, 1, 2])

        # Format function
        if a == 1:
            func = "f(x) = (x"
        elif a == -1:
            func = "f(x) = -(x"
        else:
            func = f"f(x) = {a}(x"

        if h > 0:
            func += f" - {h})^2"
        elif h < 0:
            func += f" + {abs(h)})^2"
        else:
            func += ")^2"

        if k > 0:
            func += f" + {k}"
        elif k < 0:
            func += f" - {abs(k)}"

        if problem_type == 'vertex':
            latex = f"\\text{{Find vertex of }} {func}"
            solution = h  # Return x-coordinate of vertex
        elif problem_type == 'axis':
            latex = f"\\text{{Find axis of symmetry of }} {func}"
            solution = h  # x = h
        else:  # direction
            latex = f"\\text{{Does }} {func} \\text{{ open up (1) or down (-1)?}}"
            solution = 1 if a > 0 else -1

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Identify vertex form: a(x-h)² + k"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Find x-intercepts or y-intercept"""
        problem_type = random.choice(['x_int', 'y_int'])

        if problem_type == 'x_int':
            # Use factored form
            root1 = random.randint(-8, 8)
            root2 = random.randint(-8, 8)

            latex = f"\\text{{Find x-intercepts of }} f(x) = (x - {root1})(x - {root2})"
            solution = min(root1, root2)  # Return smaller root

        else:  # y_int
            a = random.choice([1, -1, 2])
            b = random.randint(-10, 10)
            c = random.randint(-15, 15)

            if a == 1:
                func = "f(x) = x^2"
            elif a == -1:
                func = "f(x) = -x^2"
            else:
                func = f"f(x) = {a}x^2"

            if b > 0:
                func += f" + {b}x"
            elif b < 0:
                func += f" - {abs(b)}x"

            if c > 0:
                func += f" + {c}"
            elif c < 0:
                func += f" - {abs(c)}"

            latex = f"\\text{{Find y-intercept of }} {func}"
            solution = c

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Set x = 0 for y-intercept, or y = 0 for x-intercepts"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: Find maximum/minimum value"""
        a = random.choice([-2, -1, 1, 2])
        h = random.randint(-5, 5)
        k = random.randint(-10, 10)

        # Format function
        if a == 1:
            func = "f(x) = (x"
        elif a == -1:
            func = "f(x) = -(x"
        else:
            func = f"f(x) = {a}(x"

        if h > 0:
            func += f" - {h})^2"
        elif h < 0:
            func += f" + {abs(h)})^2"
        else:
            func += ")^2"

        if k > 0:
            func += f" + {k}"
        elif k < 0:
            func += f" - {abs(k)}"

        if a > 0:
            latex = f"\\text{{Find minimum value of }} {func}"
        else:
            latex = f"\\text{{Find maximum value of }} {func}"

        solution = k  # The min/max value is k

        return Equation(
            latex=latex,
            solution=solution,
            steps=["Vertex form: a(x-h)² + k", "Min/max occurs at vertex"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Word problem with projectile motion"""
        v0 = random.choice([32, 48, 64])  # Initial velocity
        h0 = random.choice([0, 10, 20])   # Initial height

        latex = f"\\text{{Ball thrown up at }} {v0} \\text{{ ft/s from }} {h0} \\text{{ ft. Max height?}}"

        # Height function: h(t) = -16t² + v0*t + h0
        # Maximum occurs at t = -b/(2a) = v0/32
        t_max = v0 / 32
        max_height = -16 * t_max**2 + v0 * t_max + h0

        solution = round(max_height)

        return Equation(
            latex=latex,
            solution=solution,
            steps=["h(t) = -16t² + v₀t + h₀", "Find vertex"],
            difficulty='challenge'
        )