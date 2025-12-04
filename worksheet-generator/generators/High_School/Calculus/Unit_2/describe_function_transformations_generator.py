"""
Describe Function Transformations Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DescribeFunctionTransformationsGenerator:
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
        h = random.randint(2, 6)
        direction = random.choice(['right', 'left'])

        if direction == 'right':
            latex = f"\\text{{Describe how }} g(x) = (x - {h})^2 \\text{{ is transformed from }} f(x) = x^2."
            solution = f"Shifted right {h} units"
            steps = [
                f"\\text{{Compare: }} g(x) = (x - {h})^2 \\text{{ to }} f(x) = x^2",
                f"\\text{{Form: }} f(x - h) \\text{{ where }} h = {h}",
                f"\\text{{Horizontal shift right }} {h} \\text{{ units}}"
            ]
        else:
            latex = f"\\text{{Describe how }} g(x) = (x + {h})^2 \\text{{ is transformed from }} f(x) = x^2."
            solution = f"Shifted left {h} units"
            steps = [
                f"\\text{{Compare: }} g(x) = (x + {h})^2 \\text{{ to }} f(x) = x^2",
                f"\\text{{Form: }} f(x + h) \\text{{ where }} h = {h}",
                f"\\text{{Horizontal shift left }} {h} \\text{{ units}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        k = random.randint(1, 6)

        latex = f"\\text{{Describe: }} g(x) = {a}x^2 + {k} \\text{{ from }} f(x) = x^2."
        solution = f"Vertical stretch by {a}, shift up {k}"
        steps = [
            f"\\text{{Coefficient }} {a}: \\text{{ vertical stretch by }} {a}",
            f"\\text{{Constant }} +{k}: \\text{{ vertical shift up }} {k}",
            f"\\text{{Combined: stretch by }} {a}, \\text{{ shift up }} {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        h = random.randint(1, 5)
        k = random.randint(1, 6)

        latex = f"\\text{{Describe: }} g(x) = {a}(x - {h})^2 + {k} \\text{{ from }} f(x) = x^2."
        solution = f"Stretch {a}, right {h}, up {k}"
        steps = [
            f"\\text{{Coefficient }} {a}: \\text{{ vertical stretch}}",
            f"(x - {h}): \\text{{ shift right }} {h}",
            f"+{k}: \\text{{ shift up }} {k}",
            f"\\text{{All three transformations applied}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        h = random.randint(1, 4)
        k = random.randint(1, 5)

        latex = f"\\text{{Describe: }} g(x) = -{a}|x + {h}| - {k} \\text{{ from }} f(x) = |x|."
        solution = f"Reflect x-axis, stretch {a}, left {h}, down {k}"
        steps = [
            "\\text{Negative sign: reflect across x-axis}",
            f"\\text{{Coefficient }} {a}: \\text{{ vertical stretch}}",
            f"x + {h}: \\text{{ shift left }} {h}",
            f"-{k}: \\text{{ shift down }} {k}",
            "\\text{Four transformations combined}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = DescribeFunctionTransformationsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
