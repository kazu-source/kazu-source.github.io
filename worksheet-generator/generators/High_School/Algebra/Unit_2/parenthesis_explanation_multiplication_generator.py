"""
Parenthesis Explanation (Multiplication) Generator
Generates problems focused on understanding and applying the distributive property
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class ParenthesisExplanationMultiplicationGenerator:
    """Generates distributive property and parenthesis multiplication problems."""

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
        """Generate easy: Basic distribution with positive numbers."""
        problem_type = random.choice(['numeric', 'single_var', 'explain'])

        if problem_type == 'numeric':
            # a(b + c) with numbers only
            a = random.randint(2, 5)
            b = random.randint(2, 10)
            c = random.randint(1, 10)
            result = a * (b + c)

            latex = f"\\text{{Expand: }} {a}({b} + {c})"
            solution = f"{a * b} + {a * c} = {result}"

            steps = [
                f"\\text{{Distribute }} {a} \\text{{ to each term inside}}",
                f"{a} \\times {b} + {a} \\times {c}",
                f"= {a * b} + {a * c}",
                f"= {result}"
            ]

        elif problem_type == 'single_var':
            # a(x + b)
            a = random.randint(2, 5)
            b = random.randint(1, 10)

            latex = f"\\text{{Expand: }} {a}(x + {b})"
            solution = f"{a}x + {a * b}"

            steps = [
                f"\\text{{Distribute }} {a} \\text{{ to each term}}",
                f"{a} \\times x + {a} \\times {b}",
                f"= {a}x + {a * b}"
            ]

        else:  # explain
            a = random.randint(2, 4)
            b = random.randint(3, 8)
            c = random.randint(2, 7)

            latex = f"\\text{{Why does }} {a}({b} + {c}) = {a} \\times {b} + {a} \\times {c}?"
            solution = "Distributive Property"

            steps = [
                f"\\text{{The distributive property states:}}",
                f"a(b + c) = ab + ac",
                f"\\text{{We multiply }} {a} \\text{{ by each term inside the parentheses}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium: Distribution with subtraction and negative numbers."""
        problem_type = random.choice(['subtraction', 'negative_outside', 'coefficient_var'])

        if problem_type == 'subtraction':
            # a(x - b)
            a = random.randint(2, 6)
            b = random.randint(1, 10)

            latex = f"\\text{{Expand: }} {a}(x - {b})"
            solution = f"{a}x - {a * b}"

            steps = [
                f"\\text{{Distribute }} {a} \\text{{ to each term}}",
                f"{a} \\times x - {a} \\times {b}",
                f"= {a}x - {a * b}"
            ]

        elif problem_type == 'negative_outside':
            # -a(x + b)
            a = random.randint(2, 5)
            b = random.randint(1, 8)

            latex = f"\\text{{Expand: }} -{a}(x + {b})"
            solution = f"-{a}x - {a * b}"

            steps = [
                f"\\text{{Distribute }} -{a} \\text{{ to each term}}",
                f"-{a} \\times x + (-{a}) \\times {b}",
                f"= -{a}x - {a * b}"
            ]

        else:  # coefficient_var
            # a(bx + c)
            a = random.randint(2, 4)
            b = random.randint(2, 5)
            c = random.randint(1, 8)

            latex = f"\\text{{Expand: }} {a}({b}x + {c})"
            solution = f"{a * b}x + {a * c}"

            steps = [
                f"\\text{{Distribute }} {a} \\text{{ to each term}}",
                f"{a} \\times {b}x + {a} \\times {c}",
                f"= {a * b}x + {a * c}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard: Multiple terms or multiple variables."""
        problem_type = random.choice(['three_terms', 'two_variables', 'negative_both'])

        if problem_type == 'three_terms':
            # a(x + b + c)
            a = random.randint(2, 5)
            b = random.randint(1, 6)
            c = random.randint(1, 6)

            latex = f"\\text{{Expand: }} {a}(x + {b} + {c})"
            solution = f"{a}x + {a * b} + {a * c}"
            simplified = f"{a}x + {a * (b + c)}"

            steps = [
                f"\\text{{Distribute }} {a} \\text{{ to all terms}}",
                f"{a}x + {a * b} + {a * c}",
                f"\\text{{Combine constants: }} {a}x + {a * (b + c)}"
            ]

        elif problem_type == 'two_variables':
            # a(x + y)
            a = random.randint(2, 6)

            latex = f"\\text{{Expand: }} {a}(x + y)"
            solution = f"{a}x + {a}y"

            steps = [
                f"\\text{{Distribute }} {a} \\text{{ to each variable}}",
                f"{a} \\times x + {a} \\times y",
                f"= {a}x + {a}y"
            ]

        else:  # negative_both
            # -a(x - b) or -a(-x + b)
            a = random.randint(2, 5)
            b = random.randint(1, 8)

            latex = f"\\text{{Expand: }} -{a}(x - {b})"
            solution = f"-{a}x + {a * b}"

            steps = [
                f"\\text{{Distribute }} -{a} \\text{{ to each term}}",
                f"-{a} \\times x - (-{a}) \\times {b}",
                f"= -{a}x + {a * b}",
                f"\\text{{Note: negative times negative = positive}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex distribution or combining after distribution."""
        problem_type = random.choice(['double_distribute', 'combine_after', 'nested'])

        if problem_type == 'double_distribute':
            # a(x + b) + c(x + d)
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(2, 4)
            d = random.randint(1, 5)

            latex = f"\\text{{Expand and simplify: }} {a}(x + {b}) + {c}(x + {d})"
            combined_x = a + c
            combined_const = a * b + c * d
            solution = f"{combined_x}x + {combined_const}"

            steps = [
                f"\\text{{Distribute each term:}}",
                f"{a}x + {a * b} + {c}x + {c * d}",
                f"\\text{{Combine like terms:}}",
                f"({a} + {c})x + ({a * b} + {c * d})",
                f"= {combined_x}x + {combined_const}"
            ]

        elif problem_type == 'combine_after':
            # a(x + b) - c(x + d)
            a = random.randint(3, 6)
            b = random.randint(1, 5)
            c = random.randint(2, a - 1)
            d = random.randint(1, 5)

            latex = f"\\text{{Expand and simplify: }} {a}(x + {b}) - {c}(x + {d})"
            combined_x = a - c
            combined_const = a * b - c * d

            if combined_const >= 0:
                solution = f"{combined_x}x + {combined_const}"
            else:
                solution = f"{combined_x}x - {abs(combined_const)}"

            steps = [
                f"\\text{{Distribute (watch the negative):}}",
                f"{a}x + {a * b} - {c}x - {c * d}",
                f"\\text{{Combine like terms:}}",
                f"({a} - {c})x + ({a * b} - {c * d})",
                f"= {solution}"
            ]

        else:  # nested
            # a(b(x + c))
            a = random.randint(2, 3)
            b = random.randint(2, 4)
            c = random.randint(1, 5)

            latex = f"\\text{{Expand: }} {a}({b}(x + {c}))"
            solution = f"{a * b}x + {a * b * c}"

            steps = [
                f"\\text{{Work from inside out:}}",
                f"\\text{{Inner: }} {b}(x + {c}) = {b}x + {b * c}",
                f"\\text{{Then: }} {a}({b}x + {b * c})",
                f"= {a * b}x + {a * b * c}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = ParenthesisExplanationMultiplicationGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
