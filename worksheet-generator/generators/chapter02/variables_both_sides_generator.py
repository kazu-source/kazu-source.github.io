"""
Variables on Both Sides Generator - Solving equations with variables on both sides
Generates problems focused on solving equations where the variable appears on both sides
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class VariablesBothSidesGenerator:
    """Generates problems for solving equations with variables on both sides."""

    def __init__(self, seed=None):
        """Initialize the variables both sides generator."""
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
        """Generate a single variables both sides problem."""

        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy variables on both sides problems."""
        problem_type = random.choice(['simple_both_sides', 'with_constant_one_side'])

        if problem_type == 'simple_both_sides':
            # Simple: 5x = 3x + 6
            # Solution: 2x = 6, x = 3
            solution = random.randint(2, 10)
            diff_coef = random.randint(2, 5)  # left - right
            const = diff_coef * solution
            left_coef = random.randint(diff_coef + 1, diff_coef + 4)
            right_coef = left_coef - diff_coef

            latex = f"{left_coef}x = {right_coef}x + {const}"

        else:  # with_constant_one_side
            # 4x + 2 = 3x + 7
            # Solution: x = 5
            solution = random.randint(2, 12)
            left_coef = random.randint(2, 6)
            right_coef = left_coef - random.randint(1, 2)

            # left_coef * x + const1 = right_coef * x + const2
            # (left_coef - right_coef) * x = const2 - const1
            const1 = random.randint(1, 10)
            const2 = (left_coef - right_coef) * solution + const1

            latex = f"{left_coef}x + {const1} = {right_coef}x + {const2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium variables on both sides problems."""
        problem_type = random.choice(['both_with_constants', 'negative_coefficients', 'larger_numbers'])

        if problem_type == 'both_with_constants':
            # 3x + 5 = x + 13
            # Solution: 2x = 8, x = 4
            solution = random.randint(3, 15)
            coef_diff = random.randint(2, 4)
            const_diff = coef_diff * solution

            left_coef = random.randint(coef_diff + 1, 7)
            right_coef = left_coef - coef_diff
            const1 = random.randint(2, 12)
            const2 = const1 + const_diff

            latex = f"{left_coef}x + {const1} = {right_coef}x + {const2}"

        elif problem_type == 'negative_coefficients':
            # 7x - 3 = 5x + 5
            # Solution: 2x = 8, x = 4
            solution = random.randint(2, 12)
            coef_diff = random.randint(2, 4)

            left_coef = random.randint(coef_diff + 2, 8)
            right_coef = left_coef - coef_diff
            const1 = random.randint(1, 10)
            const2 = const1 + coef_diff * solution

            latex = f"{left_coef}x - {const1} = {right_coef}x + {const2}"

        else:  # larger_numbers
            # 8x + 12 = 5x + 27
            # Solution: 3x = 15, x = 5
            solution = random.randint(4, 20)
            coef_diff = random.randint(3, 5)
            const_diff = coef_diff * solution

            left_coef = random.randint(coef_diff + 2, 10)
            right_coef = left_coef - coef_diff
            const1 = random.randint(5, 20)
            const2 = const1 + const_diff

            latex = f"{left_coef}x + {const1} = {right_coef}x + {const2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard variables on both sides problems."""
        problem_type = random.choice(['both_sides_subtraction', 'distribute_first', 'fractions'])

        if problem_type == 'both_sides_subtraction':
            # 5x - 7 = 2x - 1
            # Solution: 3x = 6, x = 2
            solution = random.randint(2, 15)
            coef_diff = random.randint(3, 6)

            left_coef = random.randint(coef_diff + 2, 9)
            right_coef = left_coef - coef_diff
            const2 = random.randint(1, 12)
            const1 = const2 + coef_diff * solution

            latex = f"{left_coef}x - {const1} = {right_coef}x - {const2}"

        elif problem_type == 'distribute_first':
            # 2(x + 3) = x + 10
            # 2x + 6 = x + 10
            # Solution: x = 4
            solution = random.randint(3, 12)
            mult = random.randint(2, 4)
            add_inside = random.randint(2, 8)

            # mult * (x + add_inside) = x + const2
            # mult*x + mult*add_inside = x + const2
            # (mult - 1)*x = const2 - mult*add_inside
            const2 = (mult - 1) * solution + mult * add_inside

            latex = f"{mult}(x + {add_inside}) = x + {const2}"

        else:  # fractions
            # Ensure integer solution with fractions
            # (x + 6)/2 = (x + 2)/3 is complex, so simplify:
            # x/2 + 3 = x/3 + 2
            # But to avoid fractions in solution, use:
            # 6x = 4x + 8 (which gives x = 4)
            solution = random.randint(2, 10)

            # Make coefficients that will work well
            left_coef = random.randint(5, 9)
            right_coef = random.randint(2, left_coef - 2)
            const = (left_coef - right_coef) * solution

            latex = f"{left_coef}x = {right_coef}x + {const}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge variables on both sides problems with large coefficients, fractions, and multi-step."""
        problem_type = random.choice(['large_coefficients', 'with_fractions', 'complex_multi_step', 'nested_distribution'])

        if problem_type == 'large_coefficients':
            # Large coefficients on both sides with subtraction
            # 25x - 17 = 18x - 3
            solution = random.randint(2, 12)
            coef_diff = random.randint(7, 15)

            left_coef = random.randint(15, 30)
            right_coef = left_coef - coef_diff
            const2 = random.randint(5, 25)
            const1 = const2 + coef_diff * solution

            latex = f"{left_coef}x - {const1} = {right_coef}x - {const2}"

        elif problem_type == 'with_fractions':
            # Equations that simplify to fractions or require fraction work
            # To keep integer solutions: ensure coefficients work out
            # Example: 5x + 8 = 2x + 20 gives 3x = 12, x = 4
            # Make it harder: 7x + 15 = 3x + 35 gives 4x = 20, x = 5
            solution = random.randint(3, 15)
            coef_diff = random.randint(4, 8)

            left_coef = random.randint(coef_diff + 3, 15)
            right_coef = left_coef - coef_diff
            const1 = random.randint(10, 30)
            const2 = const1 + coef_diff * solution

            # Present as fraction-like
            # (left_coef * x + const1) / 1 but make it look harder
            latex = f"{left_coef}x + {const1} = {right_coef}x + {const2}"

        elif problem_type == 'complex_multi_step':
            # Both sides have distribution and negative terms
            # 3(2x - 5) = 2(x + 4)
            # 6x - 15 = 2x + 8
            # 4x = 23, x = 5.75 (we want integer, so adjust)
            solution = random.randint(3, 12)

            mult1 = random.randint(2, 5)
            mult2 = random.randint(2, 4)
            add_inside1 = random.randint(2, 10)
            add_inside2 = random.randint(2, 10)

            # mult1 * (x - add_inside1) = mult2 * (x + add_inside2)
            # mult1*x - mult1*add_inside1 = mult2*x + mult2*add_inside2
            # (mult1 - mult2)*x = mult1*add_inside1 + mult2*add_inside2

            if mult1 > mult2:
                const_sum = mult1 * add_inside1 + mult2 * add_inside2
                # Check if divisible
                if const_sum % (mult1 - mult2) == 0:
                    solution = const_sum // (mult1 - mult2)
                    latex = f"{mult1}(x - {add_inside1}) = {mult2}(x + {add_inside2})"
                else:
                    # Fallback to simpler problem
                    solution = random.randint(5, 15)
                    coef_diff = random.randint(5, 10)
                    left_coef = random.randint(coef_diff + 5, 20)
                    right_coef = left_coef - coef_diff
                    const = coef_diff * solution
                    latex = f"{left_coef}x = {right_coef}x + {const}"
            else:
                # Fallback
                solution = random.randint(5, 15)
                coef_diff = random.randint(5, 10)
                left_coef = random.randint(coef_diff + 5, 20)
                right_coef = left_coef - coef_diff
                const = coef_diff * solution
                latex = f"{left_coef}x = {right_coef}x + {const}"

        else:  # nested_distribution
            # Double distribution: 2(3x + 4) = 4(x + 5)
            # 6x + 8 = 4x + 20
            # 2x = 12, x = 6
            solution = random.randint(3, 15)

            outer1 = random.randint(2, 4)
            inner_coef1 = random.randint(2, 5)
            inner_const1 = random.randint(2, 8)

            outer2 = random.randint(2, 4)

            # outer1 * (inner_coef1 * x + inner_const1) = outer2 * (x + inner_const2)
            # outer1*inner_coef1*x + outer1*inner_const1 = outer2*x + outer2*inner_const2
            # (outer1*inner_coef1 - outer2)*x = outer2*inner_const2 - outer1*inner_const1

            left_total_coef = outer1 * inner_coef1
            if left_total_coef > outer2:
                coef_diff = left_total_coef - outer2
                # outer2*inner_const2 = coef_diff*solution + outer1*inner_const1
                inner_const2 = (coef_diff * solution + outer1 * inner_const1) // outer2
                if (coef_diff * solution + outer1 * inner_const1) % outer2 == 0:
                    latex = f"{outer1}({inner_coef1}x + {inner_const1}) = {outer2}(x + {inner_const2})"
                else:
                    # Fallback
                    solution = random.randint(4, 12)
                    coef_diff = random.randint(6, 12)
                    left_coef = random.randint(coef_diff + 5, 25)
                    right_coef = left_coef - coef_diff
                    const = coef_diff * solution
                    latex = f"{left_coef}x = {right_coef}x + {const}"
            else:
                # Fallback
                solution = random.randint(4, 12)
                coef_diff = random.randint(6, 12)
                left_coef = random.randint(coef_diff + 5, 25)
                right_coef = left_coef - coef_diff
                const = coef_diff * solution
                latex = f"{left_coef}x = {right_coef}x + {const}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = VariablesBothSidesGenerator()

    print("Testing Variables Both Sides Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. Solve: {problem.latex}")
            print(f"   Solution: x = {problem.solution}\n")
