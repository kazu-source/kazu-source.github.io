"""
Find Values of Functions from Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FindValuesFunctionsGraphsGenerator:
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
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)

        latex = f"\\text{{Given a graph of }} f(x) \\text{{ passes through }} ({x}, {y}), \\text{{ find }} f({x})."
        solution = f"{y}"
        steps = [
            f"\\text{{The point }} ({x}, {y}) \\text{{ is on the graph}}",
            f"\\text{{This means when }} x = {x}, y = {y}",
            f"\\therefore f({x}) = {y}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
        x2, y2 = random.randint(-5, 5), random.randint(-5, 5)

        latex = f"\\text{{A graph of }} f(x) \\text{{ passes through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2}). "
        latex += f"\\text{{Find }} f({x1}) + f({x2})."
        solution = f"{y1 + y2}"
        steps = [
            f"f({x1}) = {y1} \\text{{ from point }} ({x1}, {y1})",
            f"f({x2}) = {y2} \\text{{ from point }} ({x2}, {y2})",
            f"f({x1}) + f({x2}) = {y1} + {y2} = {y1 + y2}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x1, y1 = random.randint(-4, 4), random.randint(-4, 4)
        x2, y2 = random.randint(-4, 4), random.randint(-4, 4)
        k = random.randint(2, 5)

        latex = f"\\text{{Given }} f({x1}) = {y1} \\text{{ and }} f({x2}) = {y2}, \\text{{ find }} {k}f({x1}) - f({x2})."
        result = k * y1 - y2
        solution = f"{result}"
        steps = [
            f"{k}f({x1}) = {k} \\cdot {y1} = {k * y1}",
            f"{k}f({x1}) - f({x2}) = {k * y1} - {y2}",
            f"= {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x1, y1 = random.randint(-3, 3), random.randint(1, 5)
        x2, y2 = random.randint(-3, 3), random.randint(1, 5)

        latex = f"\\text{{From a graph: }} f({x1}) = {y1}, f({x2}) = {y2}. \\text{{ Find }} \\frac{{f({x1})}}{{f({x2})}}."
        if y2 == 0:
            y2 = 1
        result = y1 / y2
        solution = f"{result:.2f}" if result != int(result) else f"{int(result)}"
        steps = [
            f"\\frac{{f({x1})}}{{f({x2})}} = \\frac{{{y1}}}{{{y2}}}",
            f"= {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FindValuesFunctionsGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
