"""
Find Inverse Functions and Relations Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FindInverseFunctionsRelationsGenerator:
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
        a = random.randint(2, 6)

        latex = f"\\text{{Find the inverse of }} f(x) = {a}x."
        solution = f"f^{{-1}}(x) = \\frac{{x}}{{{a}}}"
        steps = [
            f"y = {a}x",
            "\\text{Swap } x \\text{ and } y: x = {a}y",
            f"\\text{{Solve for }} y: y = \\frac{{x}}{{{a}}}",
            f"f^{{-1}}(x) = \\frac{{x}}{{{a}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        b = random.randint(1, 8)

        latex = f"\\text{{Find the inverse of }} f(x) = x + {b}."
        solution = f"f^{{-1}}(x) = x - {b}"
        steps = [
            f"y = x + {b}",
            f"\\text{{Swap }} x \\text{{ and }} y: x = y + {b}",
            f"\\text{{Solve for }} y: y = x - {b}",
            f"f^{{-1}}(x) = x - {b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(1, 6)

        latex = f"\\text{{Find the inverse of }} f(x) = {a}x + {b}."
        solution = f"f^{{-1}}(x) = \\frac{{x - {b}}}{{{a}}}"
        steps = [
            f"y = {a}x + {b}",
            f"\\text{{Swap }} x \\text{{ and }} y: x = {a}y + {b}",
            f"x - {b} = {a}y",
            f"y = \\frac{{x - {b}}}{{{a}}}",
            f"f^{{-1}}(x) = \\frac{{x - {b}}}{{{a}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 4)

        latex = f"\\text{{Find the inverse of }} f(x) = \\frac{{{a}x + {b}}}{{{c}}}."
        solution = f"f^{{-1}}(x) = \\frac{{{c}x - {b}}}{{{a}}}"
        steps = [
            f"y = \\frac{{{a}x + {b}}}{{{c}}}",
            f"\\text{{Swap }} x \\text{{ and }} y: x = \\frac{{{a}y + {b}}}{{{c}}}",
            f"{c}x = {a}y + {b}",
            f"{c}x - {b} = {a}y",
            f"y = \\frac{{{c}x - {b}}}{{{a}}}",
            f"f^{{-1}}(x) = \\frac{{{c}x - {b}}}{{{a}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FindInverseFunctionsRelationsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
