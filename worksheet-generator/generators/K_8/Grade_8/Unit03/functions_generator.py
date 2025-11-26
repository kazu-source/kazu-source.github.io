"""
Functions Generator - Grade 8 Unit 3
Generates problems about understanding functions and function notation
Example: If f(x) = 2x + 3, find f(5)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class FunctionsGenerator:
    """Generates functions problems."""

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
        """Generate easy problems: evaluate simple function."""
        m = random.randint(2, 6)
        b = random.randint(1, 8)
        x = random.randint(1, 6)
        result = m * x + b

        latex = f"\\text{{If }} f(x) = {m}x + {b}, \\text{{ find }} f({x})"
        solution = f"f({x}) = {result}"
        steps = [
            f"f({x}) = {m}({x}) + {b}",
            f"f({x}) = {m * x} + {b}",
            f"f({x}) = {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: evaluate with negative values or find input."""
        problem_type = random.choice(['negative', 'find_input'])

        if problem_type == 'negative':
            m = random.randint(2, 5)
            b = random.randint(-5, 5)
            x = random.randint(-4, -1)
            result = m * x + b

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            latex = f"\\text{{If }} f(x) = {m}x {b_str}, \\text{{ find }} f({x})"
            solution = f"f({x}) = {result}"
            steps = [
                f"f({x}) = {m}({x}) {b_str}",
                f"f({x}) = {m * x} {b_str}",
                f"f({x}) = {result}"
            ]
        else:  # find_input
            m = random.randint(2, 6)
            b = random.randint(1, 8)
            x = random.randint(2, 8)
            result = m * x + b

            latex = f"\\text{{If }} f(x) = {m}x + {b} \\text{{ and }} f(x) = {result}, \\text{{ find }} x"
            solution = f"x = {x}"
            steps = [
                f"{result} = {m}x + {b}",
                f"{result - b} = {m}x",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: composite operations or function composition."""
        problem_type = random.choice(['operations', 'composition'])

        if problem_type == 'operations':
            m = random.randint(2, 5)
            b = random.randint(1, 6)
            x = random.randint(1, 5)
            fx = m * x + b

            latex = f"\\text{{If }} f(x) = {m}x + {b}, \\text{{ find }} 2f({x}) + 3"
            result = 2 * fx + 3
            solution = f"{result}"
            steps = [
                f"f({x}) = {m}({x}) + {b} = {fx}",
                f"2f({x}) + 3 = 2({fx}) + 3",
                f"= {2 * fx} + 3 = {result}"
            ]
        else:  # composition
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(1, 3)
            x = random.randint(1, 4)

            gx = c * x
            fgx = a * gx + b

            latex = f"\\text{{If }} f(x) = {a}x + {b} \\text{{ and }} g(x) = {c}x, \\text{{ find }} f(g({x}))"
            solution = f"f(g({x})) = {fgx}"
            steps = [
                f"g({x}) = {c}({x}) = {gx}",
                f"f(g({x})) = f({gx}) = {a}({gx}) + {b}",
                f"= {a * gx} + {b} = {fgx}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: solve for function definition."""
        x1, x2 = random.randint(1, 4), random.randint(5, 8)
        m = random.randint(2, 5)
        b = random.randint(1, 8)
        y1, y2 = m * x1 + b, m * x2 + b

        latex = f"\\text{{If }} f({x1}) = {y1} \\text{{ and }} f({x2}) = {y2}, \\text{{ find }} f(x)"
        solution = f"f(x) = {m}x + {b}"
        steps = [
            f"\\text{{Find slope: }} m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = {m}",
            f"\\text{{Use }} f({x1}) = {y1}: {y1} = {m}({x1}) + b",
            f"b = {b}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = FunctionsGenerator()

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
