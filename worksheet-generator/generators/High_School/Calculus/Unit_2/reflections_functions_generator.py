"""
Reflections of Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ReflectionsFunctionsGenerator:
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
        axis = random.choice(['x-axis', 'y-axis'])

        if axis == 'x-axis':
            latex = "\\text{Reflect } f(x) = x^2 \\text{ across the x-axis. Write the new function.}"
            solution = "g(x) = -x^2"
            steps = [
                "\\text{Reflection across x-axis: multiply output by -1}",
                "g(x) = -f(x)",
                "g(x) = -x^2"
            ]
        else:
            latex = "\\text{Reflect } f(x) = x^2 \\text{ across the y-axis. Write the new function.}"
            solution = "g(x) = (-x)^2 = x^2"
            steps = [
                "\\text{Reflection across y-axis: multiply input by -1}",
                "g(x) = f(-x)",
                "g(x) = (-x)^2 = x^2",
                "\\text{Note: } x^2 \\text{ is symmetric about y-axis}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        axis = random.choice(['x-axis', 'y-axis'])

        if axis == 'x-axis':
            latex = f"\\text{{Reflect }} f(x) = {a}x \\text{{ across the x-axis.}}"
            solution = f"g(x) = -{a}x"
            steps = [
                "\\text{Reflection across x-axis: } g(x) = -f(x)",
                f"g(x) = -{a}x"
            ]
        else:
            latex = f"\\text{{Reflect }} f(x) = {a}x + 1 \\text{{ across the y-axis.}}"
            solution = f"g(x) = -{a}x + 1"
            steps = [
                "\\text{Reflection across y-axis: } g(x) = f(-x)",
                f"g(x) = {a}(-x) + 1",
                f"g(x) = -{a}x + 1"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Reflect } f(x) = |x| \\text{ across the x-axis, then shift up 3 units.}"
        solution = "g(x) = -|x| + 3"
        steps = [
            "\\text{First reflection: } -f(x) = -|x|",
            "\\text{Then shift up 3: } -|x| + 3",
            "g(x) = -|x| + 3"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        h = random.randint(1, 4)

        latex = f"\\text{{Reflect }} f(x) = x^3 \\text{{ across the y-axis, then shift right }} {h} \\text{{ units.}}"
        solution = f"g(x) = -(x - {h})^3"
        steps = [
            "\\text{Reflection across y-axis: } f(-x) = (-x)^3 = -x^3",
            f"\\text{{Shift right }} {h}: \\text{{ replace }} x \\text{{ with }} x - {h}",
            f"g(x) = -(x - {h})^3"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ReflectionsFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
