"""
Point Slope Form Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PointSlopeFormGenerator:
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
        m = random.randint(2, 7)
        x1 = random.randint(1, 6)
        y1 = random.randint(1, 10)

        latex = f"\\text{{Write point-slope form with slope {m} through }} ({x1}, {y1})"
        solution = f"y - {y1} = {m}(x - {x1})"
        steps = ["Use y - y₁ = m(x - x₁)", f"m = {m}, point ({x1}, {y1})", f"y - {y1} = {m}(x - {x1})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 6)
        x1 = random.randint(-5, 5)
        y1 = random.randint(-5, 5)

        latex = f"\\text{{Write point-slope form: slope {m}, point }} ({x1}, {y1})"
        if x1 >= 0:
            solution = f"y - {y1} = {m}(x - {x1})"
        else:
            solution = f"y - {y1} = {m}(x + {abs(x1)})"
        steps = ["Use y - y₁ = m(x - x₁)", f"Substitute values", solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(1, 5), random.randint(2, 10)
        x2 = x1 + random.randint(1, 4)
        m = random.randint(2, 6)
        y2 = y1 + m * (x2 - x1)

        latex = f"\\text{{Write point-slope form through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})"
        solution = f"y - {y1} = {m}(x - {x1})"
        steps = [f"Find slope: m = ({y2}-{y1})/({x2}-{x1}) = {m}", f"Use point ({x1}, {y1})", f"y - {y1} = {m}(x - {x1})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        m = random.randint(2, 5)
        x1 = random.randint(1, 5)
        y1 = random.randint(2, 10)
        b = y1 - m * x1

        latex = f"\\text{{Convert }} y - {y1} = {m}(x - {x1}) \\text{{ to slope-intercept form}}"
        solution = f"y = {m}x + {b}"
        steps = [f"Distribute: y - {y1} = {m}x - {m * x1}", f"Add {y1}: y = {m}x - {m * x1} + {y1}", f"y = {m}x + {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PointSlopeFormGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
