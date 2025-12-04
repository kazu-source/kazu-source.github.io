"""
Linear Equations Unknown Coefficients Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LinearEquationsUnknownCoefficientsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        m = random.randint(2, 8)
        x_val = random.randint(1, 5)
        y_val = random.randint(10, 30)
        b = y_val - m * x_val

        latex = f"\\text{{If }} y = {m}x + b \\text{{ passes through }} ({x_val}, {y_val})\\text{{, find }} b"
        solution = f"b = {b}"
        steps = [f"Substitute point: {y_val} = {m}({x_val}) + b", f"{y_val} = {m * x_val} + b", f"b = {y_val} - {m * x_val}", f"b = {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 7)
        x_val = random.randint(2, 6)
        b = random.randint(-10, 10)
        y_val = m * x_val + b

        latex = f"\\text{{If }} y = mx + {b} \\text{{ passes through }} ({x_val}, {y_val})\\text{{, find }} m"
        solution = f"m = {m}"
        steps = [f"Substitute: {y_val} = m({x_val}) + {b}", f"{y_val - b} = {x_val}m", f"m = {y_val - b} / {x_val}", f"m = {m}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(1, 5), random.randint(5, 15)
        x2 = x1 + random.randint(1, 4)
        m = random.randint(2, 6)
        y2 = y1 + m * (x2 - x1)

        latex = f"\\text{{Find the slope of the line through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})"
        solution = f"m = {m}"
        steps = [f"m = \\frac{{y_2 - y_1}}{{x_2 - x_1}}", f"m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}}", f"m = \\frac{{{y2 - y1}}}{{{x2 - x1}}}", f"m = {m}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x1, y1 = random.randint(0, 4), random.randint(2, 10)
        m = random.randint(2, 5)
        b = y1 - m * x1

        latex = f"\\text{{Write the equation of the line with slope }} {m} \\text{{ through }} ({x1}, {y1})"
        solution = f"y = {m}x + {b}"
        steps = [f"Use y = mx + b", f"Substitute point: {y1} = {m}({x1}) + b", f"b = {b}", f"Equation: y = {m}x + {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = LinearEquationsUnknownCoefficientsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
