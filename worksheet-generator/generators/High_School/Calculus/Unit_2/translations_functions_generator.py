"""
Translations of Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class TranslationsFunctionsGenerator:
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
        k = random.randint(2, 7)
        direction = random.choice(['up', 'down'])

        if direction == 'up':
            latex = f"\\text{{Translate }} f(x) = x^2 \\text{{ up }} {k} \\text{{ units. Write the new function.}}"
            solution = f"g(x) = x^2 + {k}"
            steps = [
                "\\text{Vertical translation up: add to output}",
                f"g(x) = f(x) + {k}",
                f"g(x) = x^2 + {k}"
            ]
        else:
            latex = f"\\text{{Translate }} f(x) = x^2 \\text{{ down }} {k} \\text{{ units. Write the new function.}}"
            solution = f"g(x) = x^2 - {k}"
            steps = [
                "\\text{Vertical translation down: subtract from output}",
                f"g(x) = f(x) - {k}",
                f"g(x) = x^2 - {k}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        h = random.randint(2, 6)
        direction = random.choice(['left', 'right'])

        if direction == 'left':
            latex = f"\\text{{Translate }} f(x) = x^2 \\text{{ left }} {h} \\text{{ units. Write the new function.}}"
            solution = f"g(x) = (x + {h})^2"
            steps = [
                "\\text{Horizontal translation left: add to input}",
                f"g(x) = f(x + {h})",
                f"g(x) = (x + {h})^2"
            ]
        else:
            latex = f"\\text{{Translate }} f(x) = x^2 \\text{{ right }} {h} \\text{{ units. Write the new function.}}"
            solution = f"g(x) = (x - {h})^2"
            steps = [
                "\\text{Horizontal translation right: subtract from input}",
                f"g(x) = f(x - {h})",
                f"g(x) = (x - {h})^2"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        h = random.randint(1, 5)
        k = random.randint(1, 6)

        latex = f"\\text{{Translate }} f(x) = x^2 \\text{{ right }} {h} \\text{{ and up }} {k}. \\text{{ Write the new function.}}"
        solution = f"g(x) = (x - {h})^2 + {k}"
        steps = [
            f"\\text{{Horizontal shift right: }} x - {h}",
            f"\\text{{Vertical shift up: }} + {k}",
            f"g(x) = (x - {h})^2 + {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        h = random.randint(1, 4)
        k = random.randint(1, 5)

        latex = f"\\text{{Translate }} f(x) = |x| \\text{{ left }} {h} \\text{{ and down }} {k}. \\text{{ Write the new function.}}"
        solution = f"g(x) = |x + {h}| - {k}"
        steps = [
            f"\\text{{Horizontal shift left: }} x + {h}",
            f"\\text{{Vertical shift down: }} - {k}",
            f"g(x) = |x + {h}| - {k}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = TranslationsFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
