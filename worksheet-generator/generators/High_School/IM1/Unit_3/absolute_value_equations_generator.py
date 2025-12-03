"""
Absolute Value Equations Generator
Creates problems about solving absolute value equations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class AbsoluteValueEquationsGenerator:
    """Generates absolute value equation problems."""

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
        """Solve |x| = a"""
        a = random.randint(2, 10)

        latex = f"\\text{{Solve: }} |x| = {a}"
        solution = f"x = {a} \\text{{ or }} x = -{a}"

        steps = [
            f"\\text{{If }} |x| = {a}, \\text{{ then x could be {a} or -{a}}}",
            f"\\text{{Check: }} |{a}| = {a} \\checkmark",
            f"\\text{{Check: }} |{-a}| = {a} \\checkmark",
            f"x = {a} \\text{{ or }} x = -{a}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Solve |x + a| = b"""
        a = random.randint(-8, 8)
        while a == 0:
            a = random.randint(-8, 8)
        b = random.randint(2, 10)

        x1 = b - a
        x2 = -b - a

        if a > 0:
            eq = f"|x + {a}| = {b}"
        else:
            eq = f"|x - {abs(a)}| = {b}"

        latex = f"\\text{{Solve: }} {eq}"
        solution = f"x = {x1} \\text{{ or }} x = {x2}"

        steps = [
            f"\\text{{Case 1: }} x + {a} = {b}",
            f"x = {b} - {a} = {x1}",
            f"\\text{{Case 2: }} x + {a} = -{b}",
            f"x = -{b} - {a} = {x2}",
            f"\\text{{Solutions: }} x = {x1} \\text{{ or }} x = {x2}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Solve |ax + b| = c or equations with no solution"""
        problem_type = random.choice(['standard', 'no_solution'])

        if problem_type == 'standard':
            a = random.randint(2, 5)
            b = random.randint(-10, 10)
            c = random.randint(2, 12)

            # ax + b = c or ax + b = -c
            x1 = (c - b) / a
            x2 = (-c - b) / a

            # Make sure we get integer solutions
            b = random.randint(-10, 10)
            x1_int = random.randint(-5, 5)
            x2_int = random.randint(-5, 5)
            while x1_int == x2_int:
                x2_int = random.randint(-5, 5)

            # Solve backwards to get c
            val1 = a * x1_int + b
            val2 = a * x2_int + b

            # We need |ax + b| = c, so val1 = c or -c, same for val2
            if abs(val1) == abs(val2):
                c = abs(val1)
                x1, x2 = x1_int, x2_int
            else:
                # Use simpler case
                a = 2
                b = random.randint(-5, 5)
                c = random.randint(2, 8)
                x1 = (c - b) / a
                x2 = (-c - b) / a
                # Round if needed
                if x1 != int(x1):
                    b = 2 * random.randint(-3, 3)
                    c = 2 * random.randint(1, 5)
                    x1 = (c - b) // 2
                    x2 = (-c - b) // 2

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            latex = f"\\text{{Solve: }} |{a}x {b_str}| = {c}"
            solution = f"x = {int(x1)} \\text{{ or }} x = {int(x2)}"

            steps = [
                f"\\text{{Case 1: }} {a}x {b_str} = {c}",
                f"{a}x = {c - b}, \\text{{ so }} x = {int(x1)}",
                f"\\text{{Case 2: }} {a}x {b_str} = -{c}",
                f"{a}x = {-c - b}, \\text{{ so }} x = {int(x2)}"
            ]
        else:
            # |x + a| = -b (no solution)
            a = random.randint(1, 8)
            b = random.randint(2, 8)

            latex = f"\\text{{Solve: }} |x + {a}| = -{b}"
            solution = "\\text{No solution}"

            steps = [
                f"\\text{{Absolute value is always }} \\geq 0",
                f"\\text{{But }} -{b} < 0",
                f"\\text{{No solution exists}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Equations requiring isolation or with one extraneous solution"""
        problem_type = random.choice(['isolate', 'word_problem'])

        if problem_type == 'isolate':
            # a|x + b| + c = d
            a = random.randint(2, 4)
            b = random.randint(-5, 5)
            c = random.randint(-10, 10)

            # Choose d so |x + b| gives a positive value
            abs_val = random.randint(2, 8)
            d = a * abs_val + c

            x1 = abs_val - b
            x2 = -abs_val - b

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

            latex = f"\\text{{Solve: }} {a}|x {b_str}| {c_str} = {d}"
            solution = f"x = {x1} \\text{{ or }} x = {x2}"

            steps = [
                f"\\text{{Isolate the absolute value:}}",
                f"{a}|x {b_str}| = {d - c}",
                f"|x {b_str}| = {abs_val}",
                f"\\text{{Now solve: }} x {b_str} = {abs_val} \\text{{ or }} x {b_str} = -{abs_val}",
                f"x = {x1} \\text{{ or }} x = {x2}"
            ]
        else:
            # Word problem
            target = random.randint(70, 100)
            tolerance = random.randint(3, 8)

            low = target - tolerance
            high = target + tolerance

            latex = f"\\text{{A thermostat is set to {target}°F with a tolerance of {tolerance}°F. Write and solve an equation for the acceptable temperatures.}}"
            solution = f"|T - {target}| = {tolerance}, \\text{{ so }} T = {low}°F \\text{{ to }} {high}°F"

            steps = [
                f"\\text{{Temperature difference from target: }} |T - {target}|",
                f"\\text{{Must be within tolerance: }} |T - {target}| \\leq {tolerance}",
                f"\\text{{Boundary temps: }} T - {target} = \\pm{tolerance}",
                f"T = {target} + {tolerance} = {high} \\text{{ or }} T = {target} - {tolerance} = {low}",
                f"\\text{{Range: }} {low}°F \\text{{ to }} {high}°F"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = AbsoluteValueEquationsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
