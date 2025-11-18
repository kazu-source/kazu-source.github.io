"""
Substitution of Variables Generator - Practice substituting values for variables
Generates problems focused on the substitution process
"""

import random
from dataclasses import dataclass
from typing import List


@dataclass
class SubstitutionProblem:
    """Represents a substitution problem."""
    latex: str  # LaTeX formatted problem
    solution: int  # The answer
    difficulty: str


class SubstitutionGenerator:
    """Generates variable substitution problems."""

    def __init__(self, seed=None):
        """Initialize the substitution generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[SubstitutionProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
            num_problems: Number of problems to generate

        Returns:
            List of SubstitutionProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> SubstitutionProblem:
        """Generate a single substitution problem."""

        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> SubstitutionProblem:
        """Generate easy substitution problems."""
        var = random.choice(['x', 'n', 'a'])
        value = random.randint(1, 10)

        problem_type = random.choice(['direct', 'simple_add', 'simple_mult'])

        if problem_type == 'direct':
            # Direct substitution: x when x = 5
            solution = value
            latex = f"\\text{{Substitute: }} {var} \\text{{ when }} {var} = {value}"

        elif problem_type == 'simple_add':
            # Simple addition: x + 3 when x = 5
            add = random.randint(1, 8)
            solution = value + add
            latex = f"\\text{{Substitute: }} {var} + {add} \\text{{ when }} {var} = {value}"

        else:  # simple_mult
            # Simple multiplication: 3x when x = 4
            mult = random.randint(2, 7)
            solution = mult * value
            latex = f"\\text{{Substitute: }} {mult}{var} \\text{{ when }} {var} = {value}"

        return SubstitutionProblem(latex=latex, solution=solution, difficulty='easy')

    def _generate_medium(self) -> SubstitutionProblem:
        """Generate medium substitution problems."""
        var = random.choice(['x', 'n', 'y', 'a'])
        value = random.randint(2, 12)

        problem_type = random.choice(['two_step', 'with_parentheses', 'squared'])

        if problem_type == 'two_step':
            # ax + b when x = value
            a = random.randint(2, 8)
            b = random.randint(1, 10)
            solution = a * value + b
            latex = f"\\text{{Substitute: }} {a}{var} + {b} \\text{{ when }} {var} = {value}"

        elif problem_type == 'with_parentheses':
            # a(x + b) when x = value
            a = random.randint(2, 6)
            b = random.randint(1, 8)
            solution = a * (value + b)
            latex = f"\\text{{Substitute: }} {a}({var} + {b}) \\text{{ when }} {var} = {value}"

        else:  # squared
            # x^2 when x = value (keep value small)
            value = random.randint(2, 8)
            solution = value ** 2
            latex = f"\\text{{Substitute: }} {var}^2 \\text{{ when }} {var} = {value}"

        return SubstitutionProblem(latex=latex, solution=solution, difficulty='medium')

    def _generate_hard(self) -> SubstitutionProblem:
        """Generate hard substitution problems."""
        problem_type = random.choice(['multi_var', 'complex_exp', 'fraction'])

        if problem_type == 'multi_var':
            # ax + by when x = val1, y = val2
            x_val = random.randint(2, 9)
            y_val = random.randint(2, 9)
            a = random.randint(2, 7)
            b = random.randint(2, 7)
            solution = a * x_val + b * y_val
            latex = f"\\text{{Substitute: }} {a}x + {b}y \\text{{ when }} x = {x_val}, y = {y_val}"

        elif problem_type == 'complex_exp':
            # ax^2 + bx when x = val
            x_val = random.randint(2, 6)
            a = random.randint(1, 5)
            b = random.randint(2, 8)
            solution = a * (x_val ** 2) + b * x_val
            latex = f"\\text{{Substitute: }} {a}x^2 + {b}x \\text{{ when }} x = {x_val}"

        else:  # fraction
            # (ax + b) / c when x = val
            x_val = random.randint(2, 6)
            c = random.randint(2, 4)
            # Ensure divisible result
            result = random.randint(4, 12)
            numerator = result * c
            a = random.randint(2, 5)
            b = numerator - (a * x_val)

            if b >= 0:
                solution = result
                latex = f"\\text{{Substitute: }} \\frac{{{a}x + {b}}}{{{c}}} \\text{{ when }} x = {x_val}"
            else:
                # Fallback
                solution = (3 * x_val + 6) // 3
                latex = f"\\text{{Substitute: }} \\frac{{3x + 6}}{{3}} \\text{{ when }} x = {x_val}"

        return SubstitutionProblem(latex=latex, solution=solution, difficulty='hard')

    def _generate_challenge(self) -> SubstitutionProblem:
        """Generate challenge substitution problems (multiple variables with different values, complex expressions)."""
        problem_type = random.choice(['three_vars_complex', 'quadratic_multi_var', 'nested_operations', 'four_vars'])

        if problem_type == 'three_vars_complex':
            # Three variables with squared and linear terms
            x_val = random.randint(2, 6)
            y_val = random.randint(2, 6)
            z_val = random.randint(2, 6)
            a = random.randint(1, 4)
            b = random.randint(2, 5)
            c = random.randint(2, 5)
            solution = a * (x_val ** 2) + b * y_val - c * z_val
            latex = f"\\text{{Substitute: }} {a}x^2 + {b}y - {c}z \\text{{ when }} x = {x_val}, y = {y_val}, z = {z_val}"

        elif problem_type == 'quadratic_multi_var':
            # Quadratic expression with two variables
            x_val = random.randint(2, 5)
            y_val = random.randint(2, 5)
            a = random.randint(1, 3)
            b = random.randint(2, 5)
            c = random.randint(1, 8)
            solution = a * (x_val ** 2) + b * (y_val ** 2) + c
            latex = f"\\text{{Substitute: }} {a}x^2 + {b}y^2 + {c} \\text{{ when }} x = {x_val}, y = {y_val}"

        elif problem_type == 'nested_operations':
            # Nested parentheses with multiple variables
            x_val = random.randint(2, 8)
            y_val = random.randint(2, 8)
            a = random.randint(2, 5)
            b = random.randint(2, 6)
            c = random.randint(2, 4)
            solution = a * (b * x_val + c * y_val)
            latex = f"\\text{{Substitute: }} {a}({b}x + {c}y) \\text{{ when }} x = {x_val}, y = {y_val}"

        else:  # four_vars
            # Four different variables
            w_val = random.randint(2, 7)
            x_val = random.randint(2, 7)
            y_val = random.randint(2, 7)
            z_val = random.randint(2, 7)
            a = random.randint(1, 4)
            b = random.randint(1, 4)
            c = random.randint(1, 4)
            d = random.randint(1, 4)
            solution = a * w_val + b * x_val + c * y_val - d * z_val
            latex = f"\\text{{Substitute: }} {a}w + {b}x + {c}y - {d}z \\text{{ when }} w = {w_val}, x = {x_val}, y = {y_val}, z = {z_val}"

        return SubstitutionProblem(latex=latex, solution=solution, difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = SubstitutionGenerator()

    print("Testing Substitution Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")
