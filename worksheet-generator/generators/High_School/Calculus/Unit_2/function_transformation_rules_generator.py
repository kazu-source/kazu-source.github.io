"""
Function Transformation Rules Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FunctionTransformationRulesGenerator:
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
        k = random.randint(2, 6)
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            latex = f"\\text{{Describe the transformation: }} g(x) = f(x) + {k}"
            solution = f"Shift up {k} units"
            steps = [
                f"\\text{{Form: }} g(x) = f(x) + k",
                f"k = {k}",
                f"\\text{{Vertical shift up by }} {k} \\text{{ units}}"
            ]
        elif direction == 'down':
            latex = f"\\text{{Describe the transformation: }} g(x) = f(x) - {k}"
            solution = f"Shift down {k} units"
            steps = [
                f"\\text{{Form: }} g(x) = f(x) - k",
                f"k = {k}",
                f"\\text{{Vertical shift down by }} {k} \\text{{ units}}"
            ]
        elif direction == 'left':
            latex = f"\\text{{Describe the transformation: }} g(x) = f(x + {k})"
            solution = f"Shift left {k} units"
            steps = [
                f"\\text{{Form: }} g(x) = f(x + k)",
                f"k = {k}",
                f"\\text{{Horizontal shift left by }} {k} \\text{{ units}}"
            ]
        else:
            latex = f"\\text{{Describe the transformation: }} g(x) = f(x - {k})"
            solution = f"Shift right {k} units"
            steps = [
                f"\\text{{Form: }} g(x) = f(x - k)",
                f"k = {k}",
                f"\\text{{Horizontal shift right by }} {k} \\text{{ units}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 4)
        transform_type = random.choice(['vertical_stretch', 'vertical_compression', 'horizontal_stretch'])

        if transform_type == 'vertical_stretch':
            latex = f"\\text{{Describe: }} g(x) = {a}f(x)"
            solution = f"Vertical stretch by factor {a}"
            steps = [
                f"\\text{{Form: }} g(x) = af(x), a > 1",
                f"a = {a}",
                f"\\text{{Vertical stretch by factor }} {a}"
            ]
        elif transform_type == 'vertical_compression':
            latex = f"\\text{{Describe: }} g(x) = \\frac{{1}}{{{a}}}f(x)"
            solution = f"Vertical compression by factor 1/{a}"
            steps = [
                f"\\text{{Form: }} g(x) = af(x), 0 < a < 1",
                f"a = \\frac{{1}}{{{a}}}",
                f"\\text{{Vertical compression by factor }} \\frac{{1}}{{{a}}}"
            ]
        else:
            latex = f"\\text{{Describe: }} g(x) = f({a}x)"
            solution = f"Horizontal compression by factor 1/{a}"
            steps = [
                f"\\text{{Form: }} g(x) = f(bx), b > 1",
                f"b = {a}",
                f"\\text{{Horizontal compression by factor }} \\frac{{1}}{{{a}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        reflection = random.choice(['x-axis', 'y-axis'])

        if reflection == 'x-axis':
            latex = "\\text{Describe: } g(x) = -f(x)"
            solution = "Reflection across x-axis"
            steps = [
                "\\text{Form: } g(x) = -f(x)",
                "\\text{Multiply output by -1}",
                "\\text{Reflection across x-axis}"
            ]
        else:
            latex = "\\text{Describe: } g(x) = f(-x)"
            solution = "Reflection across y-axis"
            steps = [
                "\\text{Form: } g(x) = f(-x)",
                "\\text{Multiply input by -1}",
                "\\text{Reflection across y-axis}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        h = random.randint(1, 4)
        k = random.randint(1, 5)

        latex = f"\\text{{Describe: }} g(x) = {a}f(x - {h}) + {k}"
        solution = f"Right {h}, vertical stretch {a}, up {k}"
        steps = [
            f"\\text{{Horizontal shift: }} x - {h} \\text{{ means right }} {h}",
            f"\\text{{Vertical stretch: }} {a}f(...) \\text{{ means stretch by }} {a}",
            f"\\text{{Vertical shift: }} + {k} \\text{{ means up }} {k}",
            f"\\text{{Combined: shift right }} {h}, \\text{{ stretch by }} {a}, \\text{{ shift up }} {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FunctionTransformationRulesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
