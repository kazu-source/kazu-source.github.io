"""
Evaluating Expressions Generator - Evaluates expressions with given variable values
Generates problems where students substitute values and evaluate
"""

import random
from dataclasses import dataclass
from typing import List


@dataclass
class EvaluatingProblem:
    """Represents an expression evaluation problem."""
    latex: str  # LaTeX formatted problem
    solution: int  # The answer
    difficulty: str


class EvaluatingExpressionsGenerator:
    """Generates expression evaluation problems."""

    def __init__(self, seed=None):
        """Initialize the evaluating expressions generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[EvaluatingProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
            num_problems: Number of problems to generate

        Returns:
            List of EvaluatingProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> EvaluatingProblem:
        """Generate a single evaluation problem."""

        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> EvaluatingProblem:
        """Generate easy evaluation problems (one variable, simple operations)."""
        var = random.choice(['x', 'n', 'y'])
        value = random.randint(1, 10)

        problem_type = random.choice(['add', 'subtract', 'multiply'])

        if problem_type == 'add':
            num = random.randint(1, 10)
            solution = value + num
            latex = f"{var} + {num}; {var} = {value}"

        elif problem_type == 'subtract':
            num = random.randint(1, value)  # Keep positive
            solution = value - num
            latex = f"{var} - {num}; {var} = {value}"

        else:  # multiply
            num = random.randint(2, 5)
            solution = num * value
            latex = f"{num}{var}; {var} = {value}"

        return EvaluatingProblem(latex=latex, solution=solution, difficulty='easy')

    def _generate_medium(self) -> EvaluatingProblem:
        """Generate medium evaluation problems (one variable, two operations)."""
        var = random.choice(['x', 'n', 'y', 'a'])
        value = random.randint(2, 10)

        problem_type = random.choice(['two_ops', 'with_exponent'])

        if problem_type == 'two_ops':
            # ax + b format
            coef = random.randint(2, 8)
            const = random.randint(1, 12)
            solution = coef * value + const
            latex = f"{coef}{var} + {const}; {var} = {value}"

        else:  # with_exponent
            # x^2 + b format
            const = random.randint(1, 10)
            solution = value ** 2 + const
            latex = f"{var}^2 + {const}; {var} = {value}"

        return EvaluatingProblem(latex=latex, solution=solution, difficulty='medium')

    def _generate_hard(self) -> EvaluatingProblem:
        """Generate hard evaluation problems (multiple variables or complex expressions)."""
        problem_type = random.choice(['two_vars', 'complex_exp', 'with_division'])

        if problem_type == 'two_vars':
            # ax + by format
            x_val = random.randint(2, 8)
            y_val = random.randint(2, 8)
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            solution = a * x_val + b * y_val
            latex = f"{a}x + {b}y; x = {x_val}, y = {y_val}"

        elif problem_type == 'complex_exp':
            # ax^2 + bx + c format
            x_val = random.randint(2, 6)
            a = random.randint(1, 4)
            b = random.randint(2, 8)
            c = random.randint(1, 10)
            solution = a * (x_val ** 2) + b * x_val + c
            latex = f"{a}x^2 + {b}x + {c}; x = {x_val}"

        else:  # with_division
            # (ax + b) / c format - ensure divisible
            x_val = random.randint(2, 6)
            c = random.randint(2, 4)
            # Make sure ax + b is divisible by c
            quotient = random.randint(3, 10)
            ax_plus_b = quotient * c
            a = random.randint(2, 5)
            b = ax_plus_b - (a * x_val)

            if b > 0:
                solution = quotient
                latex = f"\\frac{{{a}x + {b}}}{{{c}}}; x = {x_val}"
            else:
                # Fallback to simpler problem
                a = 3
                b = 6
                x_val = 2
                solution = (a * x_val + b) // c
                latex = f"\\frac{{{a}x + {b}}}{{{c}}}; x = {x_val}"

        return EvaluatingProblem(latex=latex, solution=solution, difficulty='hard')

    def _generate_challenge(self) -> EvaluatingProblem:
        """Generate challenge evaluation problems (multiple substitutions, nested expressions, complex operations)."""
        problem_type = random.choice(['three_vars', 'nested_exp', 'complex_fraction', 'mixed_exponents'])

        if problem_type == 'three_vars':
            # Three variables with complex expression
            x_val = random.randint(2, 8)
            y_val = random.randint(2, 8)
            z_val = random.randint(2, 8)
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            c = random.randint(2, 5)
            solution = a * x_val + b * y_val - c * z_val
            latex = f"{a}x + {b}y - {c}z; x = {x_val}, y = {y_val}, z = {z_val}"

        elif problem_type == 'nested_exp':
            # Nested expression with multiple operations
            x_val = random.randint(2, 5)
            a = random.randint(2, 4)
            b = random.randint(2, 6)
            c = random.randint(3, 8)
            solution = a * (x_val ** 2) + b * x_val - c
            latex = f"{a}x^2 + {b}x - {c}; x = {x_val}"

        elif problem_type == 'complex_fraction':
            # Complex fraction with two variables
            x_val = random.randint(3, 8)
            y_val = random.randint(2, 6)
            divisor = random.randint(2, 4)
            # Ensure divisible result
            numerator_val = divisor * random.randint(5, 15)
            a = random.randint(2, 5)
            b = numerator_val - (a * x_val + y_val)
            if b > 0:
                solution = (a * x_val + y_val + b) // divisor
                latex = f"\\frac{{{a}x + y + {b}}}{{{divisor}}}; x = {x_val}, y = {y_val}"
            else:
                # Fallback
                solution = (2 * x_val + 3 * y_val) // 2
                latex = f"\\frac{{2x + 3y}}{{2}}; x = {x_val}, y = {y_val}"

        else:  # mixed_exponents
            # Expression with multiple exponents and variables
            x_val = random.randint(2, 5)
            y_val = random.randint(2, 5)
            a = random.randint(1, 3)
            b = random.randint(2, 4)
            solution = a * (x_val ** 2) + b * (y_val ** 2)
            latex = f"{a}x^2 + {b}y^2; x = {x_val}, y = {y_val}"

        return EvaluatingProblem(latex=latex, solution=solution, difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = EvaluatingExpressionsGenerator()

    print("Testing Evaluating Expressions Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")
