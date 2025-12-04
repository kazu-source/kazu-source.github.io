"""
Dilations of Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DilationsFunctionsGenerator:
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
        a = random.randint(2, 5)

        latex = f"\\text{{Vertically stretch }} f(x) = x^2 \\text{{ by a factor of }} {a}."
        solution = f"g(x) = {a}x^2"
        steps = [
            f"\\text{{Vertical stretch: multiply output by }} {a}",
            f"g(x) = {a} \\cdot f(x)",
            f"g(x) = {a}x^2"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 4)

        latex = f"\\text{{Vertically compress }} f(x) = x^2 \\text{{ by a factor of }} \\frac{{1}}{{{a}}}."
        solution = f"g(x) = \\frac{{1}}{{{a}}}x^2"
        steps = [
            f"\\text{{Vertical compression: multiply output by }} \\frac{{1}}{{{a}}}",
            f"g(x) = \\frac{{1}}{{{a}}} \\cdot f(x)",
            f"g(x) = \\frac{{1}}{{{a}}}x^2"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        b = random.randint(2, 4)

        latex = f"\\text{{Horizontally compress }} f(x) = x^2 \\text{{ by a factor of }} \\frac{{1}}{{{b}}}."
        solution = f"g(x) = ({b}x)^2 = {b**2}x^2"
        steps = [
            f"\\text{{Horizontal compression: multiply input by }} {b}",
            f"g(x) = f({b}x)",
            f"g(x) = ({b}x)^2",
            f"g(x) = {b**2}x^2"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        b = random.randint(2, 3)

        latex = f"\\text{{Vertically stretch }} f(x) = |x| \\text{{ by }} {a}, \\text{{ then horizontally stretch by }} {b}."
        solution = f"g(x) = {a}\\left|\\frac{{x}}{{{b}}}\\right|"
        steps = [
            f"\\text{{Vertical stretch by }} {a}: {a}|x|",
            f"\\text{{Horizontal stretch by }} {b}: \\text{{ divide input by }} {b}",
            f"g(x) = {a}\\left|\\frac{{x}}{{{b}}}\\right|"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = DilationsFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
