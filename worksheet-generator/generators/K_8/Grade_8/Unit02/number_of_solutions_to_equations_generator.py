"""
Number of Solutions to Equations Generator - Grade 8 Unit 2
Generates problems about identifying if equations have no solution, one solution, or infinitely many solutions
Example: Determine if 2x + 3 = 2x + 5 has no solution, one solution, or infinitely many solutions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class NumberOfSolutionsToEquationsGenerator:
    """Generates problems about number of solutions to equations."""

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
        """Generate easy problems: obvious one solution cases."""
        x = random.randint(1, 10)

        # Simple equation with one solution
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        c = a * x + b

        latex = f"\\text{{How many solutions does }} {a}x + {b} = {c} \\text{{ have?}}"
        solution = "\\text{One solution: } x = " + str(x)
        steps = [
            f"{a}x + {b} = {c}",
            f"{a}x = {c - b}",
            f"x = {x}",
            "\\text{One solution}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: mix of no solution, one solution, and infinite solutions."""
        solution_type = random.choice(['none', 'one', 'infinite'])

        if solution_type == 'none':
            # Same coefficients, different constants: ax + b = ax + c where b ≠ c
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            c = b + random.randint(1, 5)

            latex = f"\\text{{How many solutions does }} {a}x + {b} = {a}x + {c} \\text{{ have?}}"
            solution = "\\text{No solution}"
            steps = [
                f"{a}x + {b} = {a}x + {c}",
                f"{b} = {c}",
                f"\\text{{False statement, so no solution}}"
            ]
        elif solution_type == 'one':
            # One solution
            x = random.randint(1, 10)
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            c = random.randint(1, a - 1) if a > 1 else a + 1
            d = a * x + b - c * x

            latex = f"\\text{{How many solutions does }} {a}x + {b} = {c}x + {d} \\text{{ have?}}"
            solution = f"\\text{{One solution: }} x = {x}"
            steps = [
                f"{a}x + {b} = {c}x + {d}",
                f"{a - c}x = {d - b}",
                f"x = {x}",
                "\\text{One solution}"
            ]
        else:  # infinite
            # Same on both sides: ax + b = ax + b
            a = random.randint(2, 6)
            b = random.randint(1, 10)

            latex = f"\\text{{How many solutions does }} {a}x + {b} = {a}x + {b} \\text{{ have?}}"
            solution = "\\text{Infinitely many solutions}"
            steps = [
                f"{a}x + {b} = {a}x + {b}",
                f"0 = 0",
                "\\text{True for all x, so infinitely many solutions}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: equations with parentheses requiring distribution first."""
        solution_type = random.choice(['none', 'one', 'infinite'])

        if solution_type == 'none':
            # a(x + b) = ax + c where ab ≠ c
            a = random.randint(2, 5)
            b = random.randint(2, 6)
            c = a * b + random.randint(1, 4)

            latex = f"\\text{{How many solutions does }} {a}(x + {b}) = {a}x + {c} \\text{{ have?}}"
            solution = "\\text{No solution}"
            steps = [
                f"{a}(x + {b}) = {a}x + {c}",
                f"{a}x + {a * b} = {a}x + {c}",
                f"{a * b} = {c}",
                f"\\text{{False statement, so no solution}}"
            ]
        elif solution_type == 'one':
            x = random.randint(1, 8)
            a = random.randint(2, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 4)
            d = a * x + a * b - c * x

            latex = f"\\text{{How many solutions does }} {a}(x + {b}) = {c}x + {d} \\text{{ have?}}"
            solution = f"\\text{{One solution: }} x = {x}"
            steps = [
                f"{a}(x + {b}) = {c}x + {d}",
                f"{a}x + {a * b} = {c}x + {d}",
                f"{a - c}x = {d - a * b}",
                f"x = {x}",
                "\\text{One solution}"
            ]
        else:  # infinite
            a = random.randint(2, 5)
            b = random.randint(2, 6)
            c = a * b

            latex = f"\\text{{How many solutions does }} {a}(x + {b}) = {a}x + {c} \\text{{ have?}}"
            solution = "\\text{Infinitely many solutions}"
            steps = [
                f"{a}(x + {b}) = {a}x + {c}",
                f"{a}x + {a * b} = {a}x + {c}",
                f"{a}x + {c} = {a}x + {c}",
                f"0 = 0",
                "\\text{True for all x, so infinitely many solutions}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex equations with multiple parentheses."""
        solution_type = random.choice(['none', 'one', 'infinite'])

        if solution_type == 'none':
            # a(x + b) + c = a(x + d) + c where b ≠ d
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(1, 8)
            d = b + random.randint(1, 4)

            latex = f"\\text{{How many solutions does }} {a}(x + {b}) + {c} = {a}(x + {d}) + {c} \\text{{ have?}}"
            solution = "\\text{No solution}"
            steps = [
                f"{a}(x + {b}) + {c} = {a}(x + {d}) + {c}",
                f"{a}x + {a * b} + {c} = {a}x + {a * d} + {c}",
                f"{a * b} = {a * d}",
                f"\\text{{False statement, so no solution}}"
            ]
        elif solution_type == 'one':
            x = random.randint(1, 8)
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(2, 4)
            d = random.randint(1, 5)
            e = a * x + a * b - c * x - c * d

            latex = f"\\text{{How many solutions does }} {a}(x + {b}) = {c}(x + {d}) + {e} \\text{{ have?}}"
            solution = f"\\text{{One solution: }} x = {x}"
            steps = [
                f"{a}(x + {b}) = {c}(x + {d}) + {e}",
                f"{a}x + {a * b} = {c}x + {c * d} + {e}",
                f"{a - c}x = {c * d + e - a * b}",
                f"x = {x}",
                "\\text{One solution}"
            ]
        else:  # infinite
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(1, 8)

            latex = f"\\text{{How many solutions does }} {a}(x + {b}) + {c} = {a}x + {a * b + c} \\text{{ have?}}"
            solution = "\\text{Infinitely many solutions}"
            steps = [
                f"{a}(x + {b}) + {c} = {a}x + {a * b + c}",
                f"{a}x + {a * b} + {c} = {a}x + {a * b + c}",
                f"{a}x + {a * b + c} = {a}x + {a * b + c}",
                f"0 = 0",
                "\\text{True for all x, so infinitely many solutions}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = NumberOfSolutionsToEquationsGenerator()

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
