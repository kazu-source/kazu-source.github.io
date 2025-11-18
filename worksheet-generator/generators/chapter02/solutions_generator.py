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
        """Generate easy solution verification problems."""
        problem_type = random.choice(['verify_simple', 'test_value', 'find_from_list'])

        if problem_type == 'verify_simple':
            # Is x = 5 a solution to x + 3 = 8?
            x_val = random.randint(2, 10)
            const = random.randint(1, 8)
            total = x_val + const

            # Randomly make it correct or incorrect
            if random.choice([True, False]):
                latex = f"\\text{{Is }} x = {x_val} \\text{{ a solution to }} x + {const} = {total}?"
                solution = 1
            else:
                wrong_total = total + random.randint(1, 3)
                latex = f"\\text{{Is }} x = {x_val} \\text{{ a solution to }} x + {const} = {wrong_total}?"
                solution = 0

        elif problem_type == 'test_value':
            # Test if a value satisfies the equation
            x_val = random.randint(3, 12)
            mult = random.randint(2, 6)
            result = mult * x_val

            latex = f"\\text{{Does }} x = {x_val} \\text{{ satisfy }} {mult}x = {result}?"
            solution = 1

        else:  # find_from_list
            # Which value from a short list is the solution?
            solution = random.randint(3, 9)
            const = random.randint(5, 15)
            total = solution + const

            latex = f"\\text{{Which is a solution to }} x + {const} = {total}? \\text{{Find }} x"
            # solution is already the answer

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium solution verification problems."""
        problem_type = random.choice(['two_step_verify', 'multiple_check', 'find_solution'])

        if problem_type == 'two_step_verify':
            # Is x = 4 a solution to 2x + 3 = 11?
            x_val = random.randint(2, 8)
            coef = random.randint(2, 5)
            const = random.randint(1, 10)
            total = coef * x_val + const

            if random.choice([True, False]):
                latex = f"\\text{{Is }} x = {x_val} \\text{{ a solution to }} {coef}x + {const} = {total}?"
                solution = 1
            else:
                wrong_total = total + random.randint(2, 5)
                latex = f"\\text{{Is }} x = {x_val} \\text{{ a solution to }} {coef}x + {const} = {wrong_total}?"
                solution = 0

        elif problem_type == 'multiple_check':
            # Check which of two values is the solution
            solution = random.randint(4, 10)
            coef = random.randint(2, 6)
            const = random.randint(3, 12)
            total = coef * solution + const

            latex = f"\\text{{Find the solution to }} {coef}x + {const} = {total}"
            # solution is already the answer

        else:  # find_solution
            # Solve simple equation to find the solution
            solution = random.randint(5, 15)
            const = random.randint(10, 30)
            total = solution + const

            latex = f"\\text{{Find }} x \\text{{ if }} x + {const} = {total}"
            # solution is already the answer

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard solution verification problems."""
        problem_type = random.choice(['verify_complex', 'no_solution', 'infinite_solutions'])

        if problem_type == 'verify_complex':
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

            latex = f"\\text{{How many solutions does }} {coef}x + {const1} = {coef}x + {const2} \\text{{ have?}}"
            solution = 0  # No solutions

        elif problem_type == 'infinite_solutions_verify':
            # Create equation with infinite solutions: ax + b = ax + b
            coef = random.randint(2, 7)
            const = random.randint(3, 15)

            latex = f"\\text{{How many solutions does }} {coef}x + {const} = {coef}x + {const} \\text{{ have? (0=none, 1=one, 999=infinite)}}"
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

                latex = f"\\text{{How many solutions: }} {left_coef}x + {const1} = {right_coef}x + {const2}? \\text{{(0, 1, or 999 for infinite)}}"
                solution = 1

            elif eq_type == 'none':
                # Same coefficients, different constants: no solution
                coef = random.randint(3, 7)
                const1 = random.randint(4, 15)
                const2 = const1 + random.randint(2, 8)

                latex = f"\\text{{How many solutions: }} {coef}x + {const1} = {coef}x + {const2}? \\text{{(0, 1, or 999 for infinite)}}"
                solution = 0

            else:  # infinite
                # Same everything: infinite solutions
                coef = random.randint(3, 8)
                const = random.randint(5, 18)

                latex = f"\\text{{How many solutions: }} {coef}x + {const} = {coef}x + {const}? \\text{{(0, 1, or 999 for infinite)}}"
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
