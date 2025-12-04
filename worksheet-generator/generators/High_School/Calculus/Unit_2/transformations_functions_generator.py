"""
Transformations of Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class TransformationsFunctionsGenerator:
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
        h = random.randint(1, 5)
        k = random.randint(1, 6)

        latex = f"\\text{{Transform }} f(x) = x^2: \\text{{ right }} {h}, \\text{{ up }} {k}."
        solution = f"g(x) = (x - {h})^2 + {k}"
        steps = [
            f"\\text{{Right }} {h}: x - {h}",
            f"\\text{{Up }} {k}: + {k}",
            f"g(x) = (x - {h})^2 + {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 4)
        k = random.randint(1, 5)

        latex = f"\\text{{Transform }} f(x) = x^2: \\text{{ vertical stretch by }} {a}, \\text{{ up }} {k}."
        solution = f"g(x) = {a}x^2 + {k}"
        steps = [
            f"\\text{{Vertical stretch by }} {a}: {a}x^2",
            f"\\text{{Up }} {k}: + {k}",
            f"g(x) = {a}x^2 + {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 3)
        h = random.randint(1, 4)
        k = random.randint(1, 5)

        latex = f"\\text{{Transform }} f(x) = x^2: \\text{{ stretch by }} {a}, \\text{{ right }} {h}, \\text{{ up }} {k}."
        solution = f"g(x) = {a}(x - {h})^2 + {k}"
        steps = [
            f"\\text{{Vertical stretch: }} {a}",
            f"\\text{{Horizontal shift: }} x - {h}",
            f"\\text{{Vertical shift: }} + {k}",
            f"g(x) = {a}(x - {h})^2 + {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        h = random.randint(1, 3)
        k = random.randint(1, 4)

        latex = f"\\text{{Transform }} f(x) = x^3: \\text{{ reflect x-axis, stretch by }} {a}, \\text{{ left }} {h}, \\text{{ down }} {k}."
        solution = f"g(x) = -{a}(x + {h})^3 - {k}"
        steps = [
            "\\text{Reflect x-axis: } -f(x)",
            f"\\text{{Vertical stretch: }} {a}",
            f"\\text{{Left }} {h}: x + {h}",
            f"\\text{{Down }} {k}: - {k}",
            f"g(x) = -{a}(x + {h})^3 - {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = TransformationsFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
