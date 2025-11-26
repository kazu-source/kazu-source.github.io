"""
Constructing Linear Models Generator - Grade 8 Unit 3
Generates problems about building linear models from data
Example: Given data points, construct a linear equation
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ConstructingLinearModelsGenerator:
    """Generates constructing linear models problems."""

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
        m = random.randint(2, 6)
        b = random.randint(5, 15)
        x = random.randint(0, 5)
        y = m * x + b

        latex = f"\\text{{A quantity starts at }} {b} \\text{{ and increases by }} {m} \\text{{ per unit. Write the equation.}}"
        solution = f"y = {m}x + {b}"
        steps = [
            f"\\text{{Initial value (y-intercept): }} {b}",
            f"\\text{{Rate of change (slope): }} {m}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x1, x2 = random.randint(1, 4), random.randint(6, 10)
        m = random.randint(2, 5)
        y1 = random.randint(10, 20)
        y2 = y1 + m * (x2 - x1)
        b = y1 - m * x1

        latex = f"\\text{{A linear relationship has values }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2}). \\text{{ Find the equation.}}"
        solution = f"y = {m}x + {b}"
        steps = [
            f"m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = {m}",
            f"{y1} = {m}({x1}) + b",
            f"b = {b}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        initial = random.randint(100, 200)
        decrease = random.randint(5, 15)
        time = random.randint(4, 8)
        remaining = initial - decrease * time

        latex = f"\\text{{A tank has }} {initial} \\text{{ gallons. After }} {time} \\text{{ hours, it has }} {remaining} \\text{{ gallons. Find the equation for gallons over time.}}"
        solution = f"g(t) = {initial} - {decrease}t"
        steps = [
            f"\\text{{Rate: }} \\frac{{{remaining} - {initial}}}{{{time} - 0}} = -{decrease}",
            f"\\text{{Initial: }} {initial}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        cost1 = random.randint(50, 100)
        cost2 = random.randint(120, 180)
        units1 = random.randint(5, 10)
        units2 = random.randint(15, 25)

        m = (cost2 - cost1) / (units2 - units1)
        b = cost1 - m * units1

        latex = f"\\text{{Producing }} {units1} \\text{{ items costs $${cost1}. Producing }} {units2} \\text{{ items costs $${cost2}. Find the cost function.}}"
        solution = f"C(x) = {m:.1f}x + {b:.1f}"
        steps = [
            f"m = \\frac{{{cost2} - {cost1}}}{{{units2} - {units1}}} = {m:.1f}",
            f"{cost1} = {m:.1f}({units1}) + b",
            f"b = {b:.1f}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = ConstructingLinearModelsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
