"""
Generator for Quadratic Formula problems.
"""

import random
import math
from generators.base import Problem, BaseGenerator
from typing import List, Tuple


class QuadraticFormulaGenerator(BaseGenerator):
    """Generator for quadratic formula problems."""

    def __init__(self):
        """Initialize the generator."""
        super().__init__()

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Problem]:
        """
        Generate a worksheet of quadratic formula problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Problem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            if problem:
                problems.append(problem)
        return problems

    def generate_problem(self, difficulty: str) -> Problem:
        """
        Generate a single quadratic formula problem.

        Args:
            difficulty: Problem difficulty level

        Returns:
            Problem object
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

    def _format_solution(self, x1: float, x2: float) -> str:
        """Format the solution set nicely."""
        # Round to reasonable precision
        x1 = round(x1, 4)
        x2 = round(x2, 4)

        # Check if they're integers
        if x1 == int(x1):
            x1 = int(x1)
        if x2 == int(x2):
            x2 = int(x2)

        # Sort solutions
        if x1 > x2:
            x1, x2 = x2, x1

        return f"x = {x1} or x = {x2}"

    def _generate_easy(self) -> Problem:
        """
        Generate an easy quadratic formula problem.
        x² + bx + c = 0 with integer solutions
        """
        # Generate two integer roots
        root1 = random.randint(-10, 10)
        root2 = random.randint(-10, 10)

        # Calculate coefficients using (x - root1)(x - root2) = 0
        # x² - (root1 + root2)x + root1*root2 = 0
        a = 1
        b = -(root1 + root2)
        c = root1 * root2

        # Problem text
        problem_text = "x²"
        if b > 0:
            problem_text += f" + {b}x"
        elif b < 0:
            problem_text += f" - {abs(b)}x"

        if c > 0:
            problem_text += f" + {c}"
        elif c < 0:
            problem_text += f" - {abs(c)}"

        problem_text += " = 0"

        # Apply quadratic formula
        discriminant = b**2 - 4*a*c

        return Problem(
            problem_type="quadratic_formula",
            question=f"Solve using the quadratic formula: {problem_text}",
            answer=self._format_solution(root1, root2),
            difficulty=1
        )

    def _generate_medium(self) -> Problem:
        """
        Generate a medium quadratic formula problem.
        ax² + bx + c = 0 with a ≠ 1, rational solutions
        """
        # Generate coefficient a != 1
        a = random.choice([2, 3, 4, 5, -2, -3])

        # Generate two rational roots
        root1 = random.choice([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
        root2 = random.choice([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

        # Calculate b and c from roots
        # ax² + bx + c = a(x - root1)(x - root2)
        b = -a * (root1 + root2)
        c = a * root1 * root2

        # Problem text
        if a == 1:
            problem_text = "x²"
        elif a == -1:
            problem_text = "-x²"
        else:
            problem_text = f"{a}x²"

        if b > 0:
            problem_text += f" + {b}x"
        elif b < 0:
            problem_text += f" - {abs(b)}x"

        if c > 0:
            problem_text += f" + {c}"
        elif c < 0:
            problem_text += f" - {abs(c)}"

        problem_text += " = 0"

        return Problem(
            problem_type="quadratic_formula",
            question=f"Solve using the quadratic formula: {problem_text}",
            answer=self._format_solution(root1, root2),
            difficulty=2
        )

    def _generate_hard(self) -> Problem:
        """
        Generate a hard quadratic formula problem.
        ax² + bx + c = 0 with irrational solutions (square roots)
        """
        # Generate coefficients that give irrational roots
        a = random.choice([1, 2, 3])
        b = random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])

        # Choose c to make discriminant positive but not perfect square
        # We want b² - 4ac to be positive but not a perfect square
        max_c = int(b**2 / (4*a)) - 1
        if max_c > 10:
            max_c = 10
        if max_c < -10:
            c = random.randint(max_c, -1)
        else:
            c = random.randint(-10, max_c)

        discriminant = b**2 - 4*a*c

        # Make sure discriminant is positive and not a perfect square
        while discriminant <= 0 or math.sqrt(discriminant) == int(math.sqrt(discriminant)):
            c = random.randint(-10, max_c)
            discriminant = b**2 - 4*a*c

        # Problem text
        if a == 1:
            problem_text = "x²"
        else:
            problem_text = f"{a}x²"

        if b > 0:
            problem_text += f" + {b}x"
        elif b < 0:
            problem_text += f" - {abs(b)}x"

        if c > 0:
            problem_text += f" + {c}"
        elif c < 0:
            problem_text += f" - {abs(c)}"

        problem_text += " = 0"

        # Calculate solutions
        sqrt_disc = math.sqrt(discriminant)
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)

        # Format with square root notation
        if b > 0:
            solution_text = f"x = ({-b} ± √{discriminant}) / {2*a}"
        else:
            solution_text = f"x = ({-b} ± √{discriminant}) / {2*a}"

        return Problem(
            problem_type="quadratic_formula",
            question=f"Solve using the quadratic formula: {problem_text}",
            answer=solution_text,
            difficulty=3
        )

    def _generate_challenge(self) -> Problem:
        """
        Generate a challenge quadratic formula problem.
        Complex equation that needs rearranging first, or has no real solutions
        """
        problem_type = random.choice(['rearrange', 'no_real', 'fraction'])

        if problem_type == 'rearrange':
            # Generate equation like: 2x² + 3x = 5x - 7
            a = random.choice([2, 3, 4, -2, -3])
            b1 = random.randint(1, 10)
            b2 = random.randint(1, 10)
            c = random.randint(-15, 15)

            # Left side: ax² + b1x
            left_side = ""
            if a == 1:
                left_side = "x²"
            elif a == -1:
                left_side = "-x²"
            else:
                left_side = f"{a}x²"

            if b1 > 0:
                left_side += f" + {b1}x"
            else:
                left_side += f" - {abs(b1)}x"

            # Right side: b2x + c
            right_side = f"{b2}x"
            if c > 0:
                right_side += f" + {c}"
            elif c < 0:
                right_side += f" - {abs(c)}"

            problem_text = f"{left_side} = {right_side}"

            # Rearrange to standard form
            b = b1 - b2
            c = -c

            # Calculate discriminant
            discriminant = b**2 - 4*a*c

            if discriminant > 0:
                sqrt_disc = math.sqrt(discriminant)
                x1 = (-b + sqrt_disc) / (2*a)
                x2 = (-b - sqrt_disc) / (2*a)

                if sqrt_disc == int(sqrt_disc):
                    answer = self._format_solution(x1, x2)
                else:
                    answer = f"x = ({-b} ± √{discriminant}) / {2*a}"
            elif discriminant == 0:
                x = -b / (2*a)
                answer = f"x = {x}"
            else:
                answer = "No real solutions"

        elif problem_type == 'no_real':
            # Generate equation with negative discriminant
            a = random.choice([1, 2, 3])
            b = random.choice([1, 2, 3, -1, -2, -3])
            # Choose c to make discriminant negative
            min_c = int(b**2 / (4*a)) + 1
            c = random.randint(min_c, min_c + 10)

            # Problem text
            if a == 1:
                problem_text = "x²"
            else:
                problem_text = f"{a}x²"

            if b > 0:
                problem_text += f" + {b}x"
            elif b < 0:
                problem_text += f" - {abs(b)}x"

            problem_text += f" + {c} = 0"

            answer = "No real solutions (discriminant < 0)"

        else:  # fraction coefficients
            # Generate equation with fractional coefficients
            a = random.choice([1, 2])
            b = random.choice([1, 3, 5, 7])
            c = random.choice([1, 2, 3, 4])
            denom = random.choice([2, 3, 4])

            problem_text = f"{a}x²/{denom} + {b}x/{denom} + {c} = 0"

            # Multiply through by denominator
            a_new = a
            b_new = b
            c_new = c * denom

            discriminant = b_new**2 - 4*a_new*c_new

            if discriminant >= 0:
                answer = f"x = ({-b_new} ± √{discriminant}) / {2*a_new}"
            else:
                answer = "No real solutions"

        return Problem(
            problem_type="quadratic_formula",
            question=f"Solve using the quadratic formula: {problem_text}",
            answer=answer,
            difficulty=4
        )