"""
Linear Equations Generator
Generates general linear equation problems (one variable, first degree)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class LinearEquationsGenerator:
    """Generates linear equation problems."""

    def __init__(self, seed=None):
        """Initialize the linear equations generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single linear equation problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple linear: ax + b = c"""
        x = random.randint(1, 12)
        a = random.randint(2, 6)
        b = random.randint(1, 10)
        c = a * x + b

        latex = f"{a}x + {b} = {c}"
        solution = x

        steps = [
            f"Subtract {b} from both sides: {a}x = {c - b}",
            f"Divide by {a}: x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate with distribution or combining like terms"""
        equation_type = random.choice(['distribution', 'combine_terms', 'subtract_form'])

        if equation_type == 'distribution':
            # a(x + b) = c
            x = random.randint(2, 10)
            a = random.randint(2, 5)
            b = random.randint(1, 8)
            c = a * (x + b)

            latex = f"{a}(x + {b}) = {c}"
            solution = x

            expanded = a * b
            steps = [
                f"Distribute: {a}x + {expanded} = {c}",
                f"Subtract {expanded}: {a}x = {c - expanded}",
                f"Divide by {a}: x = {x}"
            ]

        elif equation_type == 'combine_terms':
            # ax + bx = c
            x = random.randint(2, 10)
            a = random.randint(2, 5)
            b = random.randint(1, 4)
            c = (a + b) * x

            latex = f"{a}x + {b}x = {c}"
            solution = x

            total = a + b
            steps = [
                f"Combine like terms: {total}x = {c}",
                f"Divide by {total}: x = {x}"
            ]

        else:  # subtract_form
            # ax - b = c
            x = random.randint(3, 12)
            a = random.randint(2, 6)
            b = random.randint(1, 15)
            c = a * x - b

            latex = f"{a}x - {b} = {c}"
            solution = x

            steps = [
                f"Add {b} to both sides: {a}x = {c + b}",
                f"Divide by {a}: x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate with variables on both sides"""
        equation_type = random.choice(['vars_both_sides', 'distribution_both', 'negative_coef'])

        if equation_type == 'vars_both_sides':
            # ax + b = cx + d
            x = random.randint(3, 15)
            a = random.randint(3, 8)
            c = random.randint(1, a - 1)
            b = random.randint(2, 12)
            d = (a - c) * x + b

            latex = f"{a}x + {b} = {c}x + {d}"
            solution = x

            diff_coef = a - c
            diff_const = d - b
            steps = [
                f"Subtract {c}x from both sides: {diff_coef}x + {b} = {d}",
                f"Subtract {b} from both sides: {diff_coef}x = {diff_const}",
                f"Divide by {diff_coef}: x = {x}"
            ]

        elif equation_type == 'distribution_both':
            # a(x + b) = c(x + d)
            x = random.randint(2, 8)
            a = random.randint(2, 5)
            c = random.randint(1, a - 1) if a > 1 else random.randint(1, 3)
            b = random.randint(1, 6)
            # Solve for d: a(x + b) = c(x + d)
            # ax + ab = cx + cd
            # ax - cx = cd - ab
            # x(a - c) = cd - ab
            # cd = x(a - c) + ab
            # d = (x(a - c) + ab) / c
            d = (x * (a - c) + a * b) // c if (x * (a - c) + a * b) % c == 0 else random.randint(1, 8)

            latex = f"{a}(x + {b}) = {c}(x + {d})"
            solution = x

            left_expanded = a * b
            right_expanded = c * d
            steps = [
                f"Distribute: {a}x + {left_expanded} = {c}x + {right_expanded}",
                f"Rearrange and solve for x",
                f"x = {x}"
            ]

        else:  # negative_coef
            # -ax + b = c
            x = random.randint(2, 10)
            a = random.randint(2, 6)
            b = random.randint(5, 20)
            c = -a * x + b

            latex = f"-{a}x + {b} = {c}"
            solution = x

            steps = [
                f"Subtract {b} from both sides: -{a}x = {c - b}",
                f"Divide by -{a}: x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate complex linear with fractions or multiple operations"""
        challenge_type = random.choice(['fraction_coef', 'nested_parens', 'complex_both_sides'])

        if challenge_type == 'fraction_coef':
            # (a/b)x + c = d
            x = random.randint(4, 20)
            numerator = random.randint(2, 5)
            denominator = random.choice([2, 3, 4])
            # Make x divisible by denominator
            x = random.randint(2, 8) * denominator
            c = random.randint(3, 12)
            d = (numerator * x) // denominator + c

            latex = f"\\frac{{{numerator}}}{{{denominator}}}x + {c} = {d}"
            solution = x

            steps = [
                f"Subtract {c}: \\frac{{{numerator}}}{{{denominator}}}x = {d - c}",
                f"Multiply by \\frac{{{denominator}}}{{{numerator}}}",
                f"x = {x}"
            ]

        elif challenge_type == 'nested_parens':
            # a(b(x + c) + d) = e
            x = random.randint(2, 8)
            a = random.randint(2, 4)
            b = random.randint(2, 3)
            c = random.randint(1, 5)
            d = random.randint(1, 6)
            e = a * (b * (x + c) + d)

            latex = f"{a}({b}(x + {c}) + {d}) = {e}"
            solution = x

            steps = [
                f"Distribute inner: {a}({b}x + {b * c} + {d}) = {e}",
                f"Simplify: {a}({b}x + {b * c + d}) = {e}",
                f"Distribute outer and solve",
                f"x = {x}"
            ]

        else:  # complex_both_sides
            # ax + b - cx = dx + e
            x = random.randint(3, 12)
            a = random.randint(4, 8)
            c = random.randint(1, 3)
            d = random.randint(1, 4)
            b = random.randint(5, 15)
            e = (a - c - d) * x + b

            latex = f"{a}x + {b} - {c}x = {d}x + {e}"
            solution = x

            left_coef = a - c
            steps = [
                f"Combine like terms: {left_coef}x + {b} = {d}x + {e}",
                f"Rearrange and solve",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

