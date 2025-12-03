"""
Solving Equations with Variables on Both Sides Generator
Generates problems where variables appear on both sides of the equation
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class SolvingEquationsWithVariablesOnBothSidesGenerator:
    """Generates equations with variables on both sides."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
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
        """Generate easy: Simple ax + b = cx + d."""
        # Ensure a != c for valid equation
        a = random.randint(3, 8)
        c = random.randint(1, a - 1)
        x = random.randint(-10, 10)
        b = random.randint(-15, 15)
        d = a * x + b - c * x

        # Format: ax + b = cx + d
        left_const = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        right_const = f"+ {d}" if d >= 0 else f"- {abs(d)}"

        latex = f"{a}x {left_const} = {c}x {right_const}"
        solution = str(x)

        steps = [
            f"\\text{{Subtract }} {c}x \\text{{ from both sides}}",
            f"{a - c}x {left_const} = {d}",
            f"\\text{{Subtract }} {b} \\text{{ from both sides}}" if b > 0 else f"\\text{{Add }} {abs(b)} \\text{{ to both sides}}",
            f"{a - c}x = {d - b}",
            f"\\text{{Divide by }} {a - c}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium: Equations requiring more steps."""
        problem_type = random.choice(['larger_coef', 'negative_coef', 'move_larger'])

        if problem_type == 'larger_coef':
            # Larger coefficients
            a = random.randint(5, 12)
            c = random.randint(2, a - 1)
            x = random.randint(-8, 8)
            b = random.randint(-20, 20)
            d = a * x + b - c * x

            left_const = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            right_const = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}x {left_const} = {c}x {right_const}"

        elif problem_type == 'negative_coef':
            # Negative coefficient on one side
            a = random.randint(2, 6)
            c = -random.randint(1, 5)
            x = random.randint(-8, 8)
            b = random.randint(-15, 15)
            d = a * x + b - c * x

            left_const = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            right_const = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}x {left_const} = {c}x {right_const}"

        else:  # move_larger
            # Need to move the larger variable term
            a = random.randint(2, 5)
            c = random.randint(a + 1, 10)
            x = random.randint(-8, 8)
            b = random.randint(-15, 15)
            d = a * x + b - c * x

            left_const = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            right_const = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}x {left_const} = {c}x {right_const}"

        solution = str(x)
        steps = [
            f"\\text{{Move variable terms to one side}}",
            f"\\text{{Move constant terms to other side}}",
            f"\\text{{Divide to solve}}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard: Include distribution on one or both sides."""
        problem_type = random.choice(['distribute_left', 'distribute_right', 'both_sides'])

        if problem_type == 'distribute_left':
            # a(x + b) = cx + d
            a = random.choice([2, 3, 4])
            c = random.randint(1, 6)
            x = random.randint(-6, 6)
            b = random.randint(-5, 5)
            d = a * (x + b) - c * x

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}(x {b_str}) = {c}x {d_str}"

        elif problem_type == 'distribute_right':
            # ax + b = c(x + d)
            a = random.randint(3, 7)
            c = random.choice([2, 3])
            x = random.randint(-6, 6)
            d = random.randint(-5, 5)
            b = c * (x + d) - a * x

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}x {b_str} = {c}(x {d_str})"

        else:  # both_sides
            # a(x + b) = c(x + d)
            a = random.choice([2, 3])
            c = random.choice([4, 5])
            x = random.randint(-5, 5)
            b = random.randint(-4, 4)
            d = (a * (x + b) - c * x) // c if (a * (x + b) - c * x) % c == 0 else random.randint(-4, 4)
            # Recalculate x for clean solution
            if a != c:
                d = random.randint(-4, 4)
                x = (c * d - a * b) // (a - c) if (c * d - a * b) % (a - c) == 0 else random.randint(-5, 5)
                # Verify
                if a * (x + b) != c * (x + d):
                    x = random.randint(-5, 5)
                    d = (a * (x + b) - c * x) // c

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}(x {b_str}) = {c}(x {d_str})"

        solution = str(x)
        steps = [
            f"\\text{{Distribute on each side}}",
            f"\\text{{Collect variable terms}}",
            f"\\text{{Collect constant terms}}",
            f"\\text{{Solve for x}}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex equations or special cases."""
        problem_type = random.choice(['fractions', 'no_solution', 'infinite'])

        if problem_type == 'fractions':
            # Fractional coefficients
            a = random.choice([2, 4])  # Coefficient that divides evenly
            c = random.choice([2, 3])
            x = a * random.randint(-4, 4)  # Ensure clean division
            b = random.randint(-10, 10)
            d = x // a * a + b - c * x // 2

            latex = f"\\frac{{{a}x}}{{{a}}} + {b} = \\frac{{{c}x}}{{{2}}} + {d}"
            # Simplify: x + b = (c/2)x + d
            solution = str(x)

            steps = [
                f"\\text{{Simplify fractions}}",
                f"x + {b} = \\frac{{{c}}}{{{2}}}x + {d}",
                f"\\text{{Clear fractions by multiplying by 2}}",
                f"\\text{{Solve for x}}",
                f"x = {x}"
            ]

        elif problem_type == 'no_solution':
            # Equations with no solution: ax + b = ax + c where b != c
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            c = b + random.randint(1, 5)  # c != b

            left_const = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            right_const = f"+ {c}" if c >= 0 else f"- {abs(c)}"

            latex = f"{a}x {left_const} = {a}x {right_const}"
            solution = "No solution"

            steps = [
                f"\\text{{Subtract }} {a}x \\text{{ from both sides}}",
                f"{b} = {c}",
                f"\\text{{This is false, so no solution exists}}"
            ]

        else:  # infinite
            # Equations with infinite solutions: ax + b = ax + b
            a = random.randint(2, 6)
            b = random.randint(-10, 10)

            const_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"

            # Same expression on both sides (disguised)
            latex = f"{a}x {const_str} = {a}x {const_str}"
            solution = "All real numbers (infinite solutions)"

            steps = [
                f"\\text{{Both sides are identical}}",
                f"{a}x {const_str} = {a}x {const_str}",
                f"\\text{{True for all x, infinite solutions}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SolvingEquationsWithVariablesOnBothSidesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
