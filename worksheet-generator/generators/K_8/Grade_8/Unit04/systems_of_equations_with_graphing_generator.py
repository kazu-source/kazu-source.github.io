"""
Systems of Equations with Graphing Generator - Grade 8 Unit 4
Generates problems about solving systems by graphing
Example: Solve by graphing: y = 2x + 1 and y = -x + 4
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SystemsOfEquationsWithGraphingGenerator:
    """Generates systems with graphing problems."""

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
        x = random.randint(1, 5)
        m1, m2 = random.randint(1, 3), random.randint(-3, -1)
        b1 = random.randint(1, 6)
        y = m1 * x + b1
        b2 = y - m2 * x

        latex = f"\\text{{Solve by graphing: }} y = {m1}x + {b1}, y = {m2}x + {b2}"
        solution = f"({x}, {y})"
        steps = [
            f"\\text{{Graph both lines}}",
            f"\\text{{Find intersection point}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x = random.randint(2, 6)
        m1, m2 = random.randint(2, 5), random.randint(-4, -1)
        b1, b2 = random.randint(1, 8), random.randint(5, 12)
        y = m1 * x + b1

        # Adjust b2 so they intersect at integer point
        b2 = y - m2 * x

        b1_str = f"+ {b1}" if b1 >= 0 else f"- {abs(b1)}"
        b2_str = f"+ {b2}" if b2 >= 0 else f"- {abs(b2)}"

        latex = f"\\text{{Solve: }} y = {m1}x {b1_str}, y = {m2}x {b2_str}"
        solution = f"({x}, {y})"
        steps = [
            f"{m1}x {b1_str} = {m2}x {b2_str}",
            f"{m1 - m2}x = {b2 - b1}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        m1, m2 = random.randint(2, 5), random.randint(2, 5)

        if m1 == m2:
            # Parallel lines - no solution
            b1, b2 = random.randint(2, 6), random.randint(8, 12)
            latex = f"\\text{{Solve: }} y = {m1}x + {b1}, y = {m2}x + {b2}"
            solution = "\\text{No solution (parallel lines)}"
            steps = [
                f"\\text{{Slopes equal: }} {m1} = {m2}",
                f"\\text{{Y-intercepts different: }} {b1} \\neq {b2}",
                solution
            ]
        else:
            x = random.randint(1, 5)
            b1 = random.randint(1, 8)
            y = m1 * x + b1
            b2 = y - m2 * x

            latex = f"\\text{{Solve: }} y = {m1}x + {b1}, y = {m2}x + {b2}"
            solution = f"({x}, {y})"
            steps = [
                f"{m1}x + {b1} = {m2}x + {b2}",
                f"x = {x}, y = {y}",
                solution
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a, b, c = random.randint(2, 4), random.randint(2, 4), random.randint(8, 16)
        m = random.randint(2, 5)
        d = random.randint(3, 8)

        latex = f"\\text{{Solve: }} {a}x + {b}y = {c}, y = {m}x + {d}"
        solution = "\\text{Convert to slope-intercept and graph}"
        steps = [
            f"\\text{{Equation 1: }} y = -\\frac{{{a}}}{{{b}}}x + \\frac{{{c}}}{{{b}}}",
            f"\\text{{Equation 2: }} y = {m}x + {d}",
            "\\text{Graph both and find intersection}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = SystemsOfEquationsWithGraphingGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
