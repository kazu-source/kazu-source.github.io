"""
Order of Operations Generator - PEMDAS practice
Generates problems requiring proper order of operations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class OrderOfOperationsGenerator:
    """Generates problems for practicing order of operations."""

    def __init__(self, seed=None):
        """Initialize the order of operations generator."""
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
        """Generate a single order of operations problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple two-operation problem: a + b × c"""
        a = random.randint(2, 10)
        b = random.randint(2, 8)
        c = random.randint(2, 6)

        problem_type = random.choice(['add_mult', 'mult_add', 'sub_mult'])

        if problem_type == 'add_mult':
            latex = f"{a} + {b} \\times {c}"
            solution = a + (b * c)
        elif problem_type == 'mult_add':
            latex = f"{a} \\times {b} + {c}"
            solution = (a * b) + c
        else:  # sub_mult
            latex = f"{a} - {b} \\times {c}"
            solution = a - (b * c)

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate problem with parentheses: (a + b) × c"""
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        c = random.randint(2, 6)

        problem_type = random.choice(['paren_mult', 'mult_paren', 'div_paren'])

        if problem_type == 'paren_mult':
            latex = f"({a} + {b}) \\times {c}"
            solution = (a + b) * c
        elif problem_type == 'mult_paren':
            latex = f"{c} \\times ({a} + {b})"
            solution = c * (a + b)
        else:  # div_paren
            total = a + b
            result = random.randint(2, 5)
            divisor = total * result
            latex = f"{divisor} \\div ({a} + {b})"
            solution = result

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate problem with exponents: a^2 + b × c"""
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(2, 5)

        problem_type = random.choice(['exp_add', 'exp_mult', 'paren_exp'])

        if problem_type == 'exp_add':
            latex = f"{a}^2 + {b} \\times {c}"
            solution = (a ** 2) + (b * c)
        elif problem_type == 'exp_mult':
            latex = f"{a}^2 \\times {b} - {c}"
            solution = (a ** 2) * b - c
        else:  # paren_exp
            latex = f"({a} + {b})^2"
            solution = (a + b) ** 2

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate complex multi-operation problem"""
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        c = random.randint(2, 4)
        d = random.randint(2, 4)

        problem_type = random.choice(['nested', 'mixed_ops', 'fraction_ops'])

        if problem_type == 'nested':
            latex = f"{a} \\times ({b} + {c} \\times {d})"
            solution = a * (b + c * d)
        elif problem_type == 'mixed_ops':
            latex = f"{a}^2 + {b} \\times ({c} - {d})"
            solution = (a ** 2) + b * (c - d)
        else:  # fraction_ops
            numerator = a * b
            denominator = c + d
            if numerator % denominator == 0:
                latex = f"\\frac{{{a} \\times {b}}}{{{c} + {d}}}"
                solution = numerator // denominator
            else:
                # Adjust to ensure integer result
                denominator = c
                numerator = a * b
                if numerator % denominator == 0:
                    latex = f"\\frac{{{a} \\times {b}}}{{{c}}}"
                    solution = numerator // denominator
                else:
                    latex = f"{a} \\times {b} \\div {c}"
                    solution = (a * b) // c if (a * b) % c == 0 else a * b / c

        return Equation(latex=latex, solution=solution, steps=[str(solution)], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = OrderOfOperationsGenerator()

    print("Testing Order of Operations Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")