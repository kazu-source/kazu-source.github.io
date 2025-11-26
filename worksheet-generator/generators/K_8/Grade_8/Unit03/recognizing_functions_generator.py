"""
Recognizing Functions Generator - Grade 8 Unit 3
Generates problems about identifying whether relations are functions
Example: Is this set of ordered pairs a function? {(1,2), (2,3), (1,4)}
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class RecognizingFunctionsGenerator:
    """Generates recognizing functions problems."""

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
        is_function = random.choice([True, False])

        if is_function:
            points = [(1, 2), (2, 4), (3, 6), (4, 8)]
            random.shuffle(points)
            points = points[:3]
            latex = f"\\text{{Is this a function? }} \\{{{points[0]}, {points[1]}, {points[2]}\\}}"
            solution = "\\text{Yes, each input has exactly one output}"
        else:
            x_repeat = random.randint(1, 5)
            y1, y2 = random.randint(1, 8), random.randint(9, 15)
            other_point = (random.randint(6, 10), random.randint(1, 10))
            points = [(x_repeat, y1), (x_repeat, y2), other_point]
            random.shuffle(points)
            latex = f"\\text{{Is this a function? }} \\{{{points[0]}, {points[1]}, {points[2]}\\}}"
            solution = f"\\text{{No, }} x = {x_repeat} \\text{{ has two outputs}}"

        steps = [
            "\\text{Check if any x-value repeats}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 6)
        b = random.randint(-5, 8)

        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        latex = f"\\text{{Is }} y = {m}x {b_str} \\text{{ a function?}}"
        solution = "\\text{Yes, passes vertical line test}"
        steps = [
            f"y = {m}x {b_str}",
            "\\text{Each x gives exactly one y}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['equation', 'table'])

        if problem_type == 'equation':
            latex = f"\\text{{Is }} x = 5 \\text{{ a function of }} y?"
            solution = "\\text{No, one input (x=5) maps to many outputs (all y)}"
            steps = [
                "\\text{For any y-value, x is always 5}",
                "\\text{Not a function of y}",
                solution
            ]
        else:
            x_vals = [1, 2, 3, 4]
            y_vals = [random.randint(2, 8) for _ in range(4)]

            latex = f"\\text{{Is this table a function? x: }} {x_vals[0]}, {x_vals[1]}, {x_vals[2]}, {x_vals[3]}; \\text{{ y: }} {y_vals[0]}, {y_vals[1]}, {y_vals[2]}, {y_vals[3]}"
            solution = "\\text{Yes, each x has one y}"
            steps = [
                "\\text{Check for repeated x-values}",
                "\\text{No x-values repeat}",
                solution
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Is } x^2 + y^2 = 25 \\text{ a function?}"
        solution = "\\text{No, fails vertical line test}"
        steps = [
            "\\text{This is a circle}",
            "\\text{Some x-values have two y-values}",
            "\\text{Example: when } x = 0, y = \\pm 5",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = RecognizingFunctionsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
