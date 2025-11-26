"""
More on Order of Operations Generator - Grade 6 Unit 4
Generates advanced order of operations problems with exponents
Example: Evaluate 2^3 + 4 × 5
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MoreOnOrderOfOperationsGenerator:
    """Generates advanced order of operations problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy problems: exponents with addition/subtraction."""
        base = random.randint(2, 5)
        exp = 2
        power_val = base ** exp
        addend = random.randint(3, 10)

        if random.choice([True, False]):
            result = power_val + addend
            latex = f"{base}^{{{exp}}} + {addend}"
            steps = [
                f"\\text{{Exponent first: }} {base}^{{{exp}}} = {power_val}",
                f"\\text{{Then add: }} {power_val} + {addend} = {result}"
            ]
        else:
            result = power_val - addend
            latex = f"{base}^{{{exp}}} - {addend}"
            steps = [
                f"\\text{{Exponent first: }} {base}^{{{exp}}} = {power_val}",
                f"\\text{{Then subtract: }} {power_val} - {addend} = {result}"
            ]

        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: exponents with multiplication/division."""
        base = random.randint(2, 4)
        exp = 2
        power_val = base ** exp
        multiplier = random.randint(2, 5)

        if random.choice([True, False]):
            result = power_val * multiplier
            latex = f"{base}^{{{exp}}} \\times {multiplier}"
            steps = [
                f"\\text{{Exponent first: }} {base}^{{{exp}}} = {power_val}",
                f"\\text{{Then multiply: }} {power_val} \\times {multiplier} = {result}"
            ]
        else:
            result = power_val + multiplier * random.randint(2, 4)
            mult = random.randint(2, 4)
            mult_val = multiplier * mult
            latex = f"{base}^{{{exp}}} + {multiplier} \\times {mult}"
            steps = [
                f"\\text{{Exponent: }} {base}^{{{exp}}} = {power_val}",
                f"\\text{{Multiply: }} {multiplier} \\times {mult} = {mult_val}",
                f"\\text{{Add: }} {power_val} + {mult_val} = {power_val + mult_val}"
            ]
            result = power_val + mult_val

        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: parentheses with exponents."""
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        exp = 2

        # (a + b)^2
        sum_val = a + b
        result = sum_val ** exp

        latex = f"({a} + {b})^{{{exp}}}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Parentheses first: }} {a} + {b} = {sum_val}",
                f"\\text{{Then exponent: }} {sum_val}^{{{exp}}} = {result}"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex expressions with all operations."""
        a = random.randint(2, 4)
        b = random.randint(2, 3)
        c = random.randint(2, 4)
        d = random.randint(2, 5)

        # a^2 + (b × c) - d
        power_val = a ** 2
        product = b * c
        result = power_val + product - d

        latex = f"{a}^{{2}} + ({b} \\times {c}) - {d}"
        solution = str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Exponent: }} {a}^{{2}} = {power_val}",
                f"\\text{{Parentheses: }} {b} \\times {c} = {product}",
                f"\\text{{Left to right: }} {power_val} + {product} - {d} = {result}"
            ],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MoreOnOrderOfOperationsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex} = {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex} = {problem.solution}\n")


if __name__ == '__main__':
    main()
