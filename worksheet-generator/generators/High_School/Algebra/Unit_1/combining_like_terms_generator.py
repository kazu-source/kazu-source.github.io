"""
Combining Like Terms Generator - Practice combining like terms
Generates problems focused on simplifying expressions by combining like terms
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class CombiningLikeTermsGenerator:
    """Generates combining like terms problems."""

    def __init__(self, seed=None):
        """Initialize the combining like terms generator."""
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
        """Generate a single combining like terms problem."""

        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _format_term(self, coef: int, var: str, first: bool = False) -> str:
        """Format a term with proper signs."""
        if coef == 0:
            return ""
        elif coef == 1:
            if first:
                return var
            else:
                return f" + {var}"
        elif coef == -1:
            return f" - {var}"
        elif coef > 0:
            if first:
                return f"{coef}{var}"
            else:
                return f" + {coef}{var}"
        else:  # coef < 0
            return f" - {abs(coef)}{var}"

    def _generate_easy(self) -> Equation:
        """Generate easy combining like terms problems (same variable)."""
        var = random.choice(['x', 'y', 'n'])

        # Two like terms: 3x + 5x
        coef1 = random.randint(1, 9)
        coef2 = random.randint(1, 9)

        latex = f"{coef1}{var} + {coef2}{var}"
        total = coef1 + coef2
        solution = f"{total}{var}"

        return Equation(latex=latex, solution=0, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium combining like terms problems (multiple terms, one variable)."""
        var = random.choice(['x', 'y', 'a', 'n'])

        problem_type = random.choice(['three_terms', 'with_constant', 'subtraction'])

        if problem_type == 'three_terms':
            # 2x + 5x + 3x
            coef1 = random.randint(1, 7)
            coef2 = random.randint(1, 7)
            coef3 = random.randint(1, 7)

            latex = f"{coef1}{var} + {coef2}{var} + {coef3}{var}"
            total = coef1 + coef2 + coef3
            solution = f"{total}{var}"

        elif problem_type == 'with_constant':
            # 3x + 5 + 2x
            coef1 = random.randint(1, 8)
            const = random.randint(1, 12)
            coef2 = random.randint(1, 8)

            latex = f"{coef1}{var} + {const} + {coef2}{var}"
            total_coef = coef1 + coef2
            solution = f"{total_coef}{var} + {const}"

        else:  # subtraction
            # 7x - 3x
            coef1 = random.randint(5, 12)
            coef2 = random.randint(1, coef1 - 1)

            latex = f"{coef1}{var} - {coef2}{var}"
            total = coef1 - coef2
            solution = f"{total}{var}"

        return Equation(latex=latex, solution=0, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard combining like terms problems (multiple variables)."""
        problem_type = random.choice(['two_vars', 'mixed_ops', 'three_vars'])

        if problem_type == 'two_vars':
            # 3x + 2y + 5x + 4y
            x_coef1 = random.randint(1, 7)
            y_coef1 = random.randint(1, 7)
            x_coef2 = random.randint(1, 7)
            y_coef2 = random.randint(1, 7)

            latex = f"{x_coef1}x + {y_coef1}y + {x_coef2}x + {y_coef2}y"
            x_total = x_coef1 + x_coef2
            y_total = y_coef1 + y_coef2
            solution = f"{x_total}x + {y_total}y"

        elif problem_type == 'mixed_ops':
            # 5x - 2x + 3 + 4x - 1
            x_coef1 = random.randint(4, 9)
            x_coef2 = random.randint(1, x_coef1 - 1)
            const1 = random.randint(2, 8)
            x_coef3 = random.randint(1, 6)
            const2 = random.randint(1, const1)

            latex = f"{x_coef1}x - {x_coef2}x + {const1} + {x_coef3}x - {const2}"
            x_total = x_coef1 - x_coef2 + x_coef3
            const_total = const1 - const2
            solution = f"{x_total}x + {const_total}"

        else:  # three_vars
            # 2x + 3y + 4z + 5x + 2y
            x_coef1 = random.randint(1, 5)
            y_coef1 = random.randint(1, 5)
            z_coef = random.randint(1, 5)
            x_coef2 = random.randint(1, 5)
            y_coef2 = random.randint(1, 5)

            latex = f"{x_coef1}x + {y_coef1}y + {z_coef}z + {x_coef2}x + {y_coef2}y"
            x_total = x_coef1 + x_coef2
            y_total = y_coef1 + y_coef2
            solution = f"{x_total}x + {y_total}y + {z_coef}z"

        return Equation(latex=latex, solution=0, steps=[solution], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge combining like terms problems (more terms, negative coefficients, multi-variable)."""
        problem_type = random.choice(['many_terms', 'negative_heavy', 'four_vars', 'complex_mixed'])

        if problem_type == 'many_terms':
            # Five or more terms with two variables
            var = random.choice(['x', 'y', 'a'])
            coef1 = random.randint(2, 8)
            coef2 = random.randint(-6, -1)
            coef3 = random.randint(1, 7)
            coef4 = random.randint(-5, -1)
            coef5 = random.randint(1, 6)
            const1 = random.randint(3, 12)
            const2 = random.randint(-8, -1)

            terms = []
            total_coef = 0
            for coef in [coef1, coef2, coef3, coef4, coef5]:
                total_coef += coef
                terms.append(self._format_term(coef, var, len(terms) == 0))

            total_const = const1 + const2
            latex = "".join(terms) + f" + {const1} - {abs(const2)}"

            if total_const >= 0:
                solution = f"{total_coef}{var} + {total_const}"
            else:
                solution = f"{total_coef}{var} - {abs(total_const)}"

        elif problem_type == 'negative_heavy':
            # Multiple negative coefficients
            var = random.choice(['x', 'y', 'n'])
            coef1 = random.randint(-8, -3)
            coef2 = random.randint(2, 9)
            coef3 = random.randint(-7, -2)
            coef4 = random.randint(3, 8)

            term1 = self._format_term(coef1, var, True)
            term2 = self._format_term(coef2, var, False)
            term3 = self._format_term(coef3, var, False)
            term4 = self._format_term(coef4, var, False)

            latex = term1 + term2 + term3 + term4
            total = coef1 + coef2 + coef3 + coef4
            solution = f"{total}{var}"

        elif problem_type == 'four_vars':
            # Four different variables
            x_coef1 = random.randint(2, 7)
            y_coef1 = random.randint(2, 6)
            z_coef1 = random.randint(1, 5)
            w_coef1 = random.randint(1, 5)
            x_coef2 = random.randint(-5, -1)
            y_coef2 = random.randint(1, 6)
            z_coef2 = random.randint(-4, -1)

            latex = f"{x_coef1}x + {y_coef1}y + {z_coef1}z + {w_coef1}w - {abs(x_coef2)}x + {y_coef2}y - {abs(z_coef2)}z"
            x_total = x_coef1 + x_coef2
            y_total = y_coef1 + y_coef2
            z_total = z_coef1 + z_coef2
            solution = f"{x_total}x + {y_total}y + {z_total}z + {w_coef1}w"

        else:  # complex_mixed
            # Three variables with constants and negative coefficients
            x_coef1 = random.randint(3, 9)
            y_coef1 = random.randint(-6, -2)
            const1 = random.randint(5, 15)
            x_coef2 = random.randint(-7, -2)
            z_coef1 = random.randint(2, 8)
            y_coef2 = random.randint(3, 8)
            const2 = random.randint(-10, -3)
            x_coef3 = random.randint(1, 6)

            latex = f"{x_coef1}x - {abs(y_coef1)}y + {const1} - {abs(x_coef2)}x + {z_coef1}z + {y_coef2}y - {abs(const2)} + {x_coef3}x"
            x_total = x_coef1 + x_coef2 + x_coef3
            y_total = y_coef1 + y_coef2
            const_total = const1 + const2

            if y_total >= 0:
                solution = f"{x_total}x + {y_total}y + {z_coef1}z + {const_total}"
            else:
                solution = f"{x_total}x - {abs(y_total)}y + {z_coef1}z + {const_total}"

        return Equation(latex=latex, solution=0, steps=[solution], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = CombiningLikeTermsGenerator()

    print("Testing Combining Like Terms Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. Simplify: {problem.latex}")
            print(f"   Solution: {problem.solution}\n")
