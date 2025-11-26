"""
What Are Solutions? Generator - Understanding what makes a value a solution
Generates problems about identifying and verifying solutions to equations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class SolutionsGenerator:
    """Generates problems about understanding solutions to equations."""

    def __init__(self, seed=None):
        """Initialize the solutions generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
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
        """Generate a single solutions problem."""

        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy equations - always has one solution."""
        # Simple linear equations with one solution
        x_val = random.randint(2, 10)
        const = random.randint(1, 8)
        total = x_val + const

        latex = f"x + {const} = {total}"
        solution = 1  # Always has one solution

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium equations - always has one solution."""
        # Two-step equations with one solution
        coef = random.randint(2, 6)
        const = random.randint(3, 12)
        x_val = random.randint(2, 10)
        total = coef * x_val + const

        latex = f"{coef}x + {const} = {total}"
        solution = 1  # Always has one solution

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard equations - mix of one solution and no solution."""
        problem_type = random.choice(['one_solution', 'no_solution'])

        if problem_type == 'one_solution':
            # Verify solution to equation with variables on both sides
            x_val = random.randint(3, 10)
            left_coef = random.randint(3, 7)
            right_coef = random.randint(1, left_coef - 1)
            const = random.randint(2, 12)

            # left_coef * x = right_coef * x + const
            # (left_coef - right_coef) * x = const
            # x = const / (left_coef - right_coef)
            correct_x = const // (left_coef - right_coef) if const % (left_coef - right_coef) == 0 else None

            if correct_x and random.choice([True, False]):
                # Use correct solution
                latex = f"\\text{{Is }} x = {correct_x} \\text{{ a solution to }} {left_coef}x = {right_coef}x + {const}?"
                solution = 1
            else:
                # Use incorrect solution
                wrong_x = random.randint(5, 15)
                latex = f"\\text{{Is }} x = {wrong_x} \\text{{ a solution to }} {left_coef}x = {right_coef}x + {const}?"
                solution = 0

        elif problem_type == 'no_solution':
            # Identify if an equation has no solution (contradictory)
            coef = random.randint(2, 6)
            const1 = random.randint(5, 15)
            const2 = const1 + random.randint(1, 5)  # Different constants

            latex = f"\\text{{Does }} {coef}x + {const1} = {coef}x + {const2} \\text{{ have a solution?}}"
            solution = 0

        else:  # infinite_solutions
            # Find what makes equation true for all x
            x_val = random.randint(3, 8)
            coef1 = random.randint(2, 6)
            coef2 = random.randint(2, 6)
            const = random.randint(3, 12)

            # Find x such that coef1*x + const = coef2*x
            # coef1*x - coef2*x = -const
            # (coef1 - coef2)*x = -const
            if coef1 != coef2:
                solution = abs(const) // abs(coef1 - coef2) if const % (coef1 - coef2) == 0 else random.randint(2, 10)
                latex = f"\\text{{Find }} x \\text{{ where }} {coef1}x + {const} = {coef2}x"
            else:
                # Fallback to simpler problem
                solution = random.randint(4, 12)
                add_const = random.randint(10, 25)
                total = solution + add_const
                latex = f"\\text{{Find }} x \\text{{ if }} x + {add_const} = {total}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge solution problems - focus on no solution and infinite solutions."""
        problem_type = random.choice(['no_solution_verify', 'infinite_solutions_verify', 'determine_solution_type', 'find_value_for_condition'])

        if problem_type == 'no_solution_verify':
            # Create equation with no solution: ax + b = ax + c where b != c
            coef = random.randint(3, 8)
            const1 = random.randint(5, 20)
            const2 = const1 + random.randint(3, 10)  # Ensure different

            latex = f"{coef}x + {const1} = {coef}x + {const2}"
            solution = 0  # No solutions

        elif problem_type == 'infinite_solutions_verify':
            # Create equation with infinite solutions: ax + b = ax + b
            coef = random.randint(2, 7)
            const = random.randint(3, 15)

            latex = f"{coef}x + {const} = {coef}x + {const}"
            solution = 999  # Infinite solutions (using 999 as code for infinity)

        elif problem_type == 'determine_solution_type':
            # Given coefficients, determine if equation has 0, 1, or infinite solutions
            # Randomly choose between the three types
            eq_type = random.choice(['one', 'none', 'infinite'])

            if eq_type == 'one':
                # Different coefficients: normal equation
                left_coef = random.randint(4, 9)
                right_coef = random.randint(2, left_coef - 1)
                const1 = random.randint(2, 12)
                const2 = random.randint(5, 20)

                latex = f"{left_coef}x + {const1} = {right_coef}x + {const2}"
                solution = 1

            elif eq_type == 'none':
                # Same coefficients, different constants: no solution
                coef = random.randint(3, 7)
                const1 = random.randint(4, 15)
                const2 = const1 + random.randint(2, 8)

                latex = f"{coef}x + {const1} = {coef}x + {const2}"
                solution = 0

            else:  # infinite
                # Same everything: infinite solutions
                coef = random.randint(3, 8)
                const = random.randint(5, 18)

                latex = f"{coef}x + {const} = {coef}x + {const}"
                solution = 999

        else:  # find_value_for_condition
            # Find the value of k that makes equation have no solution or infinite solutions
            # If 3x + 5 = 3x + k has no solution, what is k? (any k != 5)
            # If 3x + k = 3x + k has infinite solutions, what is k? (any value works)

            condition_type = random.choice(['no_solution', 'infinite_solution'])
            coef = random.randint(2, 6)
            const = random.randint(4, 15)

            if condition_type == 'no_solution':
                # For no solution, need same coefficients but different constants
                # So k must NOT equal const
                wrong_const = const + random.randint(1, 10)
                latex = f"\\text{{If }} {coef}x + {const} = {coef}x + k \\text{{ has no solution, k could be:}}"
                solution = wrong_const

            else:  # infinite_solution
                # For infinite solutions, everything must be identical
                # So k must equal const
                latex = f"\\text{{If }} {coef}x + k = {coef}x + {const} \\text{{ has infinite solutions, find k}}"
                solution = const

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = SolutionsGenerator()

    print("Testing Solutions Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")
