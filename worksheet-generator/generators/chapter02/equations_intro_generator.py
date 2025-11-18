"""
Equations Intro Generator - Introduction to the concept of equations
Generates problems about understanding what equations are and their properties
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class EquationsIntroGenerator:
    """Generates problems introducing the concept of equations."""

    def __init__(self, seed=None):
        """Initialize the equations intro generator."""
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
        """Generate a single equation intro problem."""

        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy equation concept problems."""
        problem_type = random.choice(['identify_equation', 'true_false', 'complete'])

        if problem_type == 'identify_equation':
            # Is this an equation?
            var = random.choice(['x', 'n', 'y'])
            num1 = random.randint(2, 9)
            num2 = random.randint(1, 10)

            if random.choice([True, False]):
                # True equation
                latex = f"Is {num1}{var} = {num2} an equation?"
                solution = 1
            else:
                # Expression (not equation)
                latex = f"Is {num1}{var} + {num2} an equation?"
                solution = 0

        elif problem_type == 'true_false':
            # Check if equation is true for given value
            x_val = random.randint(1, 8)
            result = random.randint(10, 30)
            coef = result // x_val if result % x_val == 0 else random.randint(2, 6)
            actual_result = coef * x_val

            latex = f"If x = {x_val}, is {coef}x = {actual_result} true?"
            solution = 1

        else:  # complete
            # Complete the equation
            x_val = random.randint(2, 9)
            coef = random.randint(2, 7)
            result = coef * x_val
            latex = f"If x = {x_val} and {coef}x = ?, what is ?"
            solution = result

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium equation concept problems."""
        problem_type = random.choice(['balance', 'find_value', 'verify'])

        if problem_type == 'balance':
            # Both sides equal
            x_val = random.randint(2, 8)
            left_coef = random.randint(2, 6)
            left_const = random.randint(1, 10)
            left_side = left_coef * x_val + left_const

            latex = f"If x = {x_val}, what equals {left_coef}x + {left_const}?"
            solution = left_side

        elif problem_type == 'find_value':
            # Find x that makes equation true
            solution = random.randint(2, 10)
            const = random.randint(5, 20)
            total = solution + const
            latex = f"Find x if x + {const} = {total}"

        else:  # verify
            # Verify solution
            x_val = random.randint(3, 12)
            coef = random.randint(2, 5)
            const = random.randint(1, 8)
            result = coef * x_val + const

            latex = f"Is x = {x_val} a solution to {coef}x + {const} = {result}?"
            solution = 1

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard equation concept problems."""
        problem_type = random.choice(['multiple_solutions', 'no_solution', 'identity'])

        if problem_type == 'multiple_solutions':
            # Which value satisfies the equation?
            solution = random.randint(4, 12)
            const = random.randint(10, 25)
            total = solution + const

            latex = f"Which value makes x + {const} = {total} true?"

        elif problem_type == 'no_solution':
            # Check if value is a solution
            x_test = random.randint(3, 10)
            coef = random.randint(2, 6)
            wrong_result = coef * x_test + random.randint(1, 5)  # Intentionally wrong

            latex = f"Is x = {x_test} a solution to {coef}x = {wrong_result}?"
            solution = 0

        else:  # identity
            # Find what makes both sides equal
            x_val = random.randint(3, 9)
            coef1 = random.randint(2, 5)
            coef2 = random.randint(2, 5)
            const = random.randint(2, 10)

            # Make equation true: coef1*x + const = coef2*x + ?
            # So ? = coef1*x + const - coef2*x = (coef1-coef2)*x + const
            result = (coef1 - coef2) * x_val + const

            latex = f"If x = {x_val}, find ? so {coef1}x + {const} = {coef2}x + ?"
            solution = result

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge equation concept problems."""
        problem_type = random.choice(['complex_conceptual', 'prove_property', 'multi_variable_reasoning'])

        if problem_type == 'complex_conceptual':
            # Complex multi-step conceptual problem
            # Find the value that makes a complex relationship work
            a = random.randint(2, 5)
            b = random.randint(3, 7)
            c = random.randint(2, 6)

            # If ax + b = cx + d, and we know x = k, find d
            x_val = random.randint(4, 12)
            solution = a * x_val + b - c * x_val

            latex = f"If x = {x_val} makes {a}x + {b} = {c}x + ? true, find ?"

        elif problem_type == 'prove_property':
            # Understand equation properties
            # Which transformation keeps equation balanced?
            x_val = random.randint(3, 10)
            coef = random.randint(2, 6)
            const1 = random.randint(5, 15)
            const2 = random.randint(3, 12)

            # If 2x + 5 = 17, what operation gives 2x = 12?
            # Answer is the constant to subtract
            solution = const1
            total = coef * x_val + const1

            latex = f"If {coef}x + {const1} = {total}, subtract what from both sides to get {coef}x = {total - const1}?"

        else:  # multi_variable_reasoning
            # Complex reasoning about equation structure
            # If 3a + 2b = 20 and a = 4, find b
            a_val = random.randint(2, 6)
            b_val = random.randint(2, 8)
            coef_a = random.randint(2, 5)
            coef_b = random.randint(2, 4)
            total = coef_a * a_val + coef_b * b_val

            # Solving for b: b = (total - coef_a * a_val) / coef_b
            solution = b_val

            latex = f"If {coef_a}a + {coef_b}b = {total} \\text{{ and }} a = {a_val}, \\text{{ find }} b"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = EquationsIntroGenerator()

    print("Testing Equations Intro Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")
