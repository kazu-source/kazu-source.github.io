"""
Number of Solutions to Systems Generator - Grade 8 Unit 4
Generates problems about determining number of solutions to systems
Example: How many solutions: y = 2x + 1, y = 2x + 3?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class NumberOfSolutionsToSystemsGenerator:
    """Generates number of solutions to systems problems."""

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
        solution_type = random.choice(['one', 'none', 'infinite'])

        if solution_type == 'one':
            m1, m2 = random.randint(2, 5), random.randint(-3, -1)
            b1, b2 = random.randint(1, 6), random.randint(3, 8)
            latex = f"\\text{{How many solutions: }} y = {m1}x + {b1}, y = {m2}x + {b2}?"
            solution = "\\text{One solution (different slopes)}"
        elif solution_type == 'none':
            m = random.randint(2, 6)
            b1, b2 = random.randint(1, 5), random.randint(7, 12)
            latex = f"\\text{{How many solutions: }} y = {m}x + {b1}, y = {m}x + {b2}?"
            solution = "\\text{No solution (parallel lines)}"
        else:
            m, b = random.randint(2, 6), random.randint(1, 8)
            latex = f"\\text{{How many solutions: }} y = {m}x + {b}, y = {m}x + {b}?"
            solution = "\\text{Infinitely many solutions (same line)}"

        steps = [
            "\\text{Compare slopes and y-intercepts}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        solution_type = random.choice(['one', 'none', 'infinite'])

        if solution_type == 'one':
            m1, m2 = random.randint(2, 5), random.randint(1, 4)
            while m1 == m2:
                m2 = random.randint(1, 4)
            b1, b2 = random.randint(-3, 5), random.randint(-2, 6)

            b1_str = f"+ {b1}" if b1 >= 0 else f"- {abs(b1)}"
            b2_str = f"+ {b2}" if b2 >= 0 else f"- {abs(b2)}"

            latex = f"\\text{{How many solutions: }} y = {m1}x {b1_str}, y = {m2}x {b2_str}?"
            solution = "\\text{One solution}"
            steps = [f"\\text{{Slopes different: }} {m1} \\neq {m2}", solution]
        elif solution_type == 'none':
            m, b1, b2 = random.randint(2, 6), random.randint(1, 5), random.randint(7, 12)
            latex = f"\\text{{How many solutions: }} y = {m}x + {b1}, y = {m}x + {b2}?"
            solution = "\\text{No solution}"
            steps = [f"\\text{{Same slope, different intercepts}}", solution]
        else:
            m, b = random.randint(2, 6), random.randint(1, 8)
            # Same line in different form
            a, c = m, b
            latex = f"\\text{{How many solutions: }} y = {m}x + {b}, y = {a}x + {c}?"
            solution = "\\text{Infinitely many}"
            steps = ["\\text{Same line}", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        solution_type = random.choice(['one', 'none', 'infinite'])

        if solution_type == 'one':
            a1, b1, c1 = random.randint(2, 4), random.randint(2, 4), random.randint(8, 16)
            a2, b2, c2 = random.randint(1, 3), random.randint(3, 5), random.randint(10, 18)

            latex = f"\\text{{How many solutions: }} {a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}?"

            # Check if slopes are different
            slope1 = -a1 / b1
            slope2 = -a2 / b2

            if abs(slope1 - slope2) > 0.01:
                solution = "\\text{One solution}"
            else:
                solution = "\\text{Check slopes}"
        elif solution_type == 'none':
            a, b = random.randint(2, 4), random.randint(2, 4)
            c1, c2 = random.randint(8, 12), random.randint(15, 20)

            latex = f"\\text{{How many solutions: }} {a}x + {b}y = {c1}, {a}x + {b}y = {c2}?"
            solution = "\\text{No solution (parallel)}"
        else:
            a, b, c = random.randint(2, 4), random.randint(2, 4), random.randint(10, 16)
            mult = random.randint(2, 3)

            latex = f"\\text{{How many solutions: }} {a}x + {b}y = {c}, {a * mult}x + {b * mult}y = {c * mult}?"
            solution = "\\text{Infinitely many (same line)}"

        steps = ["\\text{Convert to slope-intercept form}", solution]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{A system has infinitely many solutions. If one equation is } y = 3x + 5, \\text{ what could the other be?}"
        solution = "y = 3x + 5 \\text{ (or equivalent form)}"
        steps = [
            "\\text{For infinite solutions, equations must be equivalent}",
            "\\text{Same slope and y-intercept}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = NumberOfSolutionsToSystemsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
