"""
Equations with Parentheses Generator - Grade 8 Unit 2
Generates equations that require distributing and solving
Example: 3(x + 2) = 15, solve for x
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EquationsWithParenthesesGenerator:
    """Generates equations with parentheses."""

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
        """Generate easy problems: simple distribution on one side."""
        x = random.randint(1, 10)

        # a(x + b) = c
        a = random.randint(2, 5)
        b = random.randint(1, 8)
        c = a * (x + b)

        latex = f"{a}(x + {b}) = {c}"
        solution = f"x = {x}"
        steps = [
            f"{a}(x + {b}) = {c}",
            f"{a}x + {a * b} = {c}",
            f"{a}x = {c - a * b}",
            f"x = {x}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: distribution with subtraction or on both sides."""
        problem_type = random.choice(['subtract', 'both_sides'])

        if problem_type == 'subtract':
            x = random.randint(1, 10)

            # a(x - b) = c
            a = random.randint(2, 6)
            b = random.randint(1, 8)
            c = a * (x - b)

            latex = f"{a}(x - {b}) = {c}"
            solution = f"x = {x}"
            steps = [
                f"{a}(x - {b}) = {c}",
                f"{a}x - {a * b} = {c}",
                f"{a}x = {c + a * b}",
                f"x = {x}"
            ]
        else:  # both_sides
            x = random.randint(1, 10)

            # a(x + b) = c(x + d)
            a = random.randint(2, 5)
            b = random.randint(1, 6)
            c = random.randint(1, a - 1) if a > 1 else a + 1
            d = ((a * x + a * b) - c * x) // c if c != 0 else 1

            latex = f"{a}(x + {b}) = {c}(x + {d})"
            solution = f"x = {x}"
            steps = [
                f"{a}(x + {b}) = {c}(x + {d})",
                f"{a}x + {a * b} = {c}x + {c * d}",
                f"{a - c}x = {c * d - a * b}",
                f"x = {x}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: multiple sets of parentheses or negative coefficients."""
        problem_type = random.choice(['multiple', 'negative'])

        if problem_type == 'multiple':
            x = random.randint(1, 8)

            # a(x + b) + c(x + d) = e
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(2, 4)
            d = random.randint(1, 5)
            e = a * x + a * b + c * x + c * d

            latex = f"{a}(x + {b}) + {c}(x + {d}) = {e}"
            solution = f"x = {x}"
            steps = [
                f"{a}(x + {b}) + {c}(x + {d}) = {e}",
                f"{a}x + {a * b} + {c}x + {c * d} = {e}",
                f"{a + c}x + {a * b + c * d} = {e}",
                f"{a + c}x = {e - (a * b + c * d)}",
                f"x = {x}"
            ]
        else:  # negative
            x = random.randint(1, 10)

            # -a(x - b) = c
            a = random.randint(2, 5)
            b = random.randint(1, 8)
            c = -a * (x - b)

            latex = f"-{a}(x - {b}) = {c}"
            solution = f"x = {x}"
            steps = [
                f"-{a}(x - {b}) = {c}",
                f"-{a}x + {a * b} = {c}",
                f"-{a}x = {c - a * b}",
                f"x = {x}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: nested parentheses or complex distributions."""
        problem_type = random.choice(['nested', 'complex'])

        if problem_type == 'nested':
            x = random.randint(2, 6)

            # a(b(x + c) + d) = e
            a = random.randint(2, 3)
            b = random.randint(2, 3)
            c = random.randint(1, 4)
            d = random.randint(1, 4)
            e = a * (b * (x + c) + d)

            latex = f"{a}({b}(x + {c}) + {d}) = {e}"
            solution = f"x = {x}"
            steps = [
                f"{a}({b}(x + {c}) + {d}) = {e}",
                f"{a}({b}x + {b * c} + {d}) = {e}",
                f"{a}({b}x + {b * c + d}) = {e}",
                f"{a * b}x + {a * (b * c + d)} = {e}",
                f"{a * b}x = {e - a * (b * c + d)}",
                f"x = {x}"
            ]
        else:  # complex
            x = random.randint(1, 8)

            # a(x + b) - c(x - d) = e
            a = random.randint(2, 5)
            b = random.randint(1, 6)
            c = random.randint(2, 4)
            d = random.randint(1, 6)
            e = a * x + a * b - c * x + c * d

            latex = f"{a}(x + {b}) - {c}(x - {d}) = {e}"
            solution = f"x = {x}"
            steps = [
                f"{a}(x + {b}) - {c}(x - {d}) = {e}",
                f"{a}x + {a * b} - {c}x + {c * d} = {e}",
                f"{a - c}x + {a * b + c * d} = {e}",
                f"{a - c}x = {e - (a * b + c * d)}",
                f"x = {x}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = EquationsWithParenthesesGenerator()

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
