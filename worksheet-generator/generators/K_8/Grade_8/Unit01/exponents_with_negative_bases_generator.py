"""
Exponents with Negative Bases Generator - Grade 8 Unit 1
Generates problems evaluating expressions with negative bases
Example: (-2)³ = -8, (-3)² = 9
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ExponentsWithNegativeBasesGenerator:
    """Generates exponents with negative bases problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
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
        """Generate easy problems: (-a)² and (-a)³ with small bases."""
        base = random.choice([2, 3, 4, 5])
        exponent = random.choice([2, 3])

        result = (-base) ** exponent

        latex = f"(-{base})^{{{exponent}}}"
        solution = str(result)

        if exponent == 2:
            steps = [f"(-{base}) \\times (-{base}) = {result}"]
        else:
            steps = [f"(-{base}) \\times (-{base}) \\times (-{base}) = {result}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: higher exponents and comparing with/without parentheses."""
        problem_type = random.choice(['eval', 'compare'])

        if problem_type == 'eval':
            base = random.choice([2, 3, 4, 5, 6])
            exponent = random.choice([2, 3, 4])

            result = (-base) ** exponent

            latex = f"(-{base})^{{{exponent}}}"
            solution = str(result)
            steps = [f"\\text{{Negative base raised to }} {exponent}", f"(-{base})^{{{exponent}}} = {result}"]

        else:  # compare
            base = random.choice([2, 3, 4, 5])
            exponent = 2

            with_parens = (-base) ** exponent
            without_parens = -(base ** exponent)

            latex = f"\\text{{Compare: }} (-{base})^{{{exponent}}} \\text{{ and }} -{base}^{{{exponent}}}"
            solution = f"(-{base})^{{{exponent}}} = {with_parens}, -{base}^{{{exponent}}} = {without_parens}"
            steps = [
                f"(-{base})^{{{exponent}}} = {with_parens}",
                f"-{base}^{{{exponent}}} = -{base**exponent} = {without_parens}",
                f"\\text{{They are }} {'equal' if with_parens == without_parens else 'different'}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: expressions with multiple terms."""
        problem_type = random.choice(['sum', 'product', 'power'])

        if problem_type == 'sum':
            base1 = random.choice([2, 3, 4])
            base2 = random.choice([2, 3, 4])
            exp1 = random.choice([2, 3])
            exp2 = random.choice([2, 3])

            val1 = (-base1) ** exp1
            val2 = (-base2) ** exp2
            result = val1 + val2

            latex = f"(-{base1})^{{{exp1}}} + (-{base2})^{{{exp2}}}"
            solution = str(result)
            steps = [
                f"(-{base1})^{{{exp1}}} = {val1}",
                f"(-{base2})^{{{exp2}}} = {val2}",
                f"{val1} + {val2} = {result}"
            ]

        elif problem_type == 'product':
            base = random.choice([2, 3, 4])
            exp1 = 2
            exp2 = 3

            val1 = (-base) ** exp1
            val2 = (-base) ** exp2
            result = val1 * val2

            latex = f"(-{base})^{{{exp1}}} \\times (-{base})^{{{exp2}}}"
            solution = str(result)
            steps = [
                f"(-{base})^{{{exp1}}} = {val1}",
                f"(-{base})^{{{exp2}}} = {val2}",
                f"{val1} \\times {val2} = {result}"
            ]

        else:  # power
            base = random.choice([2, 3])
            inner_exp = 2
            outer_exp = 2

            inner_result = (-base) ** inner_exp
            result = inner_result ** outer_exp

            latex = f"\\left[(-{base})^{{{inner_exp}}}\\right]^{{{outer_exp}}}"
            solution = str(result)
            steps = [
                f"(-{base})^{{{inner_exp}}} = {inner_result}",
                f"({inner_result})^{{{outer_exp}}} = {result}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: patterns and reasoning."""
        problem_type = random.choice(['pattern', 'true_false', 'complex'])

        if problem_type == 'pattern':
            base = random.choice([2, 3])

            latex = f"\\text{{Is }} (-{base})^{{10}} \\text{{ positive or negative?}}"
            solution = "Positive"
            steps = [
                f"\\text{{Even exponent means even number of negative factors}}",
                f"\\text{{Negative × negative = positive}}",
                f"\\text{{Answer: Positive}}"
            ]

        elif problem_type == 'true_false':
            base = random.choice([2, 3, 4])

            latex = f"\\text{{True or False: }} (-{base})^{{{2}}} = -{base}^{{{2}}}"
            solution = "False"
            steps = [
                f"(-{base})^{{{2}}} = {(-base)**2}",
                f"-{base}^{{{2}}} = {-(base**2)}",
                f"{(-base)**2} \\neq {-(base**2)}",
                f"\\text{{False}}"
            ]

        else:  # complex
            base = random.choice([2, 3])

            val1 = (-base) ** 3
            val2 = (-base) ** 2
            result = val1 - val2

            latex = f"(-{base})^3 - (-{base})^2"
            solution = str(result)
            steps = [
                f"(-{base})^3 = {val1}",
                f"(-{base})^2 = {val2}",
                f"{val1} - {val2} = {result}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ExponentsWithNegativeBasesGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex} = {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
