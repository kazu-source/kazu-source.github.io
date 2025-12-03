"""
Multi-Step Equations Generator
Creates problems about solving equations requiring multiple steps
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class MultiStepEquationsGenerator:
    """Generates multi-step equation problems."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Two-step equations: ax + b = c"""
        a = random.randint(2, 8)
        x = random.randint(-10, 10)
        b = random.randint(-15, 15)
        c = a * x + b

        # Format equation
        if b >= 0:
            eq = f"{a}x + {b} = {c}"
        else:
            eq = f"{a}x - {abs(b)} = {c}"

        latex = f"\\text{{Solve: }} {eq}"
        solution = str(x)

        steps = [
            f"\\text{{Subtract }} {b} \\text{{ from both sides: }} {a}x = {c - b}",
            f"\\text{{Divide both sides by }} {a}: x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Equations with parentheses or fractions"""
        problem_type = random.choice(['parentheses', 'fraction'])

        if problem_type == 'parentheses':
            # a(x + b) = c
            a = random.randint(2, 5)
            x = random.randint(-8, 8)
            b = random.randint(-10, 10)
            c = a * (x + b)

            if b >= 0:
                eq = f"{a}(x + {b}) = {c}"
            else:
                eq = f"{a}(x - {abs(b)}) = {c}"

            latex = f"\\text{{Solve: }} {eq}"
            solution = str(x)

            steps = [
                f"\\text{{Distribute: }} {a}x + {a * b} = {c}",
                f"\\text{{Subtract }} {a * b}: {a}x = {c - a * b}",
                f"\\text{{Divide by }} {a}: x = {x}"
            ]
        else:
            # x/a + b = c (ensure integer solution)
            a = random.randint(2, 6)
            x = random.randint(-5, 5) * a  # Make x divisible by a
            b = random.randint(-10, 10)
            c = x // a + b

            if b >= 0:
                eq = f"\\frac{{x}}{{{a}}} + {b} = {c}"
            else:
                eq = f"\\frac{{x}}{{{a}}} - {abs(b)} = {c}"

            latex = f"\\text{{Solve: }} {eq}"
            solution = str(x)

            steps = [
                f"\\text{{Subtract }} {b}: \\frac{{x}}{{{a}}} = {c - b}",
                f"\\text{{Multiply by }} {a}: x = {a} \\cdot {c - b} = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Variables on both sides or combining like terms"""
        problem_type = random.choice(['both_sides', 'combine_first'])

        if problem_type == 'both_sides':
            # ax + b = cx + d
            a = random.randint(3, 8)
            c = random.randint(1, a - 1)  # Ensure a > c
            x = random.randint(-8, 8)
            b = random.randint(-15, 15)
            d = a * x + b - c * x

            # Format equation
            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            eq = f"{a}x {b_str} = {c}x {d_str}"

            latex = f"\\text{{Solve: }} {eq}"
            solution = str(x)

            steps = [
                f"\\text{{Subtract }} {c}x \\text{{ from both sides: }} {a - c}x {b_str} = {d}",
                f"\\text{{Subtract }} {b} \\text{{ from both sides: }} {a - c}x = {d - b}",
                f"\\text{{Divide by }} {a - c}: x = {x}"
            ]
        else:
            # ax + bx + c = d (combine like terms first)
            a = random.randint(2, 5)
            b = random.randint(1, 5)
            x = random.randint(-8, 8)
            c = random.randint(-15, 15)
            d = (a + b) * x + c

            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

            eq = f"{a}x + {b}x {c_str} = {d}"

            latex = f"\\text{{Solve: }} {eq}"
            solution = str(x)

            steps = [
                f"\\text{{Combine like terms: }} {a + b}x {c_str} = {d}",
                f"\\text{{Subtract }} {c}: {a + b}x = {d - c}",
                f"\\text{{Divide by }} {a + b}: x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex multi-step with parentheses on both sides"""
        problem_type = random.choice(['double_dist', 'nested', 'word_problem'])

        if problem_type == 'double_dist':
            # a(x + b) + c = d(x + e)
            a = random.randint(2, 4)
            d = random.randint(1, 3)
            while a == d:
                d = random.randint(1, 3)
            x = random.randint(-5, 5)
            b = random.randint(-5, 5)
            c = random.randint(-10, 10)
            # Calculate e from the equation
            # a(x + b) + c = d(x + e)
            # ax + ab + c = dx + de
            # (a-d)x + ab + c = de
            # e = [(a-d)x + ab + c] / d
            # For integer e, choose values carefully
            left_side = a * (x + b) + c
            e = random.randint(-5, 5)
            # Recalculate to make it work
            right_side = d * (x + e)
            c = right_side - a * (x + b)

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
            e_str = f"+ {e}" if e >= 0 else f"- {abs(e)}"

            eq = f"{a}(x {b_str}) {c_str} = {d}(x {e_str})"

            latex = f"\\text{{Solve: }} {eq}"
            solution = str(x)

            steps = [
                f"\\text{{Distribute: }} {a}x + {a*b} {c_str} = {d}x + {d*e}",
                f"\\text{{Simplify: }} {a}x + {a*b + c} = {d}x + {d*e}",
                f"\\text{{Get variables on one side: }} {a - d}x = {d*e - a*b - c}",
                f"\\text{{Divide: }} x = {x}"
            ]

        elif problem_type == 'nested':
            # Multiple steps with careful construction
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            x = random.randint(-5, 5)
            c = random.randint(-8, 8)
            result = a * (b * x + c)

            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
            eq = f"{a}({b}x {c_str}) = {result}"

            latex = f"\\text{{Solve: }} {eq}"
            solution = str(x)

            steps = [
                f"\\text{{Distribute: }} {a * b}x + {a * c} = {result}",
                f"\\text{{Subtract }} {a * c}: {a * b}x = {result - a * c}",
                f"\\text{{Divide by }} {a * b}: x = {x}"
            ]

        else:
            # Word problem
            x = random.randint(5, 15)
            rate = random.randint(2, 5)
            start = random.randint(10, 30)
            total = start + rate * x

            latex = f"\\text{{A pool has {start} gallons and fills at {rate} gallons per minute. How many minutes until it has {total} gallons?}}"
            solution = str(x)

            steps = [
                f"\\text{{Set up equation: }} {start} + {rate}m = {total}",
                f"\\text{{Subtract }} {start}: {rate}m = {total - start}",
                f"\\text{{Divide by }} {rate}: m = {x} \\text{{ minutes}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = MultiStepEquationsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
