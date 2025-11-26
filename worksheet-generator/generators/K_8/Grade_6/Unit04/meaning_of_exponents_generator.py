"""
Meaning of Exponents Generator - Grade 6 Unit 4
Generates problems introducing exponent notation
Example: Write 3 × 3 × 3 × 3 using exponential notation
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MeaningOfExponentsGenerator:
    """Generates meaning of exponents problems."""

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
        """Generate easy problems: convert repeated multiplication to exponents."""
        base = random.randint(2, 9)
        exponent = random.randint(2, 4)

        multiplication = " \\times ".join([str(base)] * exponent)

        latex = f"\\text{{Write using exponents: }} {multiplication}"
        solution = f"{base}^{{{exponent}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{{base} is multiplied {exponent} times}}",
                f"\\text{{Answer: }} {base}^{{{exponent}}}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: expand exponential notation."""
        base = random.randint(2, 12)
        exponent = random.randint(2, 5)

        multiplication = " \\times ".join([str(base)] * exponent)

        latex = f"\\text{{Expand: }} {base}^{{{exponent}}}"
        solution = multiplication

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{base}^{{{exponent}}} = {multiplication}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: identify base and exponent."""
        base = random.randint(2, 15)
        exponent = random.randint(2, 6)

        if random.choice([True, False]):
            latex = f"\\text{{What is the base in }} {base}^{{{exponent}}}\\text{{?}}"
            solution = str(base)
        else:
            latex = f"\\text{{What is the exponent in }} {base}^{{{exponent}}}\\text{{?}}"
            solution = str(exponent)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{In }} {base}^{{{exponent}}}, \\text{{ base}} = {base}, \\text{{ exponent}} = {exponent}"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: comparing exponential expressions."""
        base1 = random.randint(2, 5)
        exp1 = random.randint(3, 5)
        val1 = base1 ** exp1

        base2 = random.randint(2, 5)
        exp2 = random.randint(3, 5)
        val2 = base2 ** exp2

        # Make sure they're different
        while val1 == val2:
            exp2 = random.randint(3, 5)
            val2 = base2 ** exp2

        if val1 > val2:
            solution = f"{base1}^{{{exp1}}} > {base2}^{{{exp2}}}"
            comparison = ">"
        elif val1 < val2:
            solution = f"{base1}^{{{exp1}}} < {base2}^{{{exp2}}}"
            comparison = "<"
        else:
            solution = f"{base1}^{{{exp1}}} = {base2}^{{{exp2}}}"
            comparison = "="

        latex = f"\\text{{Compare using }}<, >, \\text{{ or }} =: {base1}^{{{exp1}}} \\quad ? \\quad {base2}^{{{exp2}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{base1}^{{{exp1}}} = {val1}",
                f"{base2}^{{{exp2}}} = {val2}",
                f"{val1} {comparison} {val2}"
            ],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MeaningOfExponentsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
