"""
Circle Basics Generator
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class CircleBasicsGenerator:
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
        r = random.randint(5, 12)
        latex = f"\\text{{Find circumference of circle with radius }} {r}."
        c = 2 * math.pi * r
        solution = f"{c:.2f}"
        steps = [f"C = 2\\pi r = 2\\pi({r}) = {c:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        r = random.randint(4, 10)
        area = math.pi * r * r
        latex = f"\\text{{Find area of circle with radius }} {r}."
        solution = f"{area:.2f}"
        steps = [f"A = \\pi r^2 = \\pi({r})^2 = {area:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        d = random.randint(10, 20)
        r = d / 2
        area = math.pi * r * r
        latex = f"\\text{{Circle has diameter }} {d}. \\text{{ Find area.}}"
        solution = f"{area:.2f}"
        steps = [f"r = \\frac{d}{2} = \\frac{{{d}}}{{2}} = {r}",
                f"A = \\pi r^2 = \\pi({r})^2 = {area:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        c = random.randint(30, 60)
        r = c / (2 * math.pi)
        area = math.pi * r * r
        latex = f"\\text{{Circle has circumference }} {c}. \\text{{ Find area.}}"
        solution = f"{area:.2f}"
        steps = [f"C = 2\\pi r \\Rightarrow r = \\frac{{C}}{{2\\pi}} = \\frac{{{c}}}{{2\\pi}} = {r:.2f}",
                f"A = \\pi r^2 = {area:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = CircleBasicsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
