"""
Inverses of Trigonometric Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class InversesTrigFunctionsGenerator:
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
        values = [
            ("0", "0"), ("\\frac{1}{2}", "\\frac{\\pi}{6}"),
            ("\\frac{\\sqrt{2}}{2}", "\\frac{\\pi}{4}"), ("\\frac{\\sqrt{3}}{2}", "\\frac{\\pi}{3}"),
            ("1", "\\frac{\\pi}{2}")
        ]
        val, result = random.choice(values)

        latex = f"\\text{{Find }} \\arcsin\\left({val}\\right)."
        solution = result
        steps = [
            f"\\sin^{{-1}}({val}) = \\theta",
            f"\\sin(\\theta) = {val}",
            f"\\theta = {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        values = [
            ("0", "0"), ("\\frac{1}{2}", "\\frac{\\pi}{3}"),
            ("\\frac{\\sqrt{2}}{2}", "\\frac{\\pi}{4}"), ("\\frac{\\sqrt{3}}{2}", "\\frac{\\pi}{6}"),
            ("1", "0")
        ]
        val, result = random.choice(values)

        latex = f"\\text{{Find }} \\arccos\\left({val}\\right)."
        solution = result
        steps = [
            f"\\cos^{{-1}}({val}) = \\theta",
            f"\\cos(\\theta) = {val}",
            f"\\theta = {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        values = [
            ("0", "0"), ("1", "\\frac{\\pi}{4}"),
            ("\\sqrt{3}", "\\frac{\\pi}{3}"), ("-1", "-\\frac{\\pi}{4}")
        ]
        val, result = random.choice(values)

        latex = f"\\text{{Find }} \\arctan\\left({val}\\right)."
        solution = result
        steps = [
            f"\\tan^{{-1}}({val}) = \\theta",
            f"\\tan(\\theta) = {val}",
            f"\\theta = {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Find } \\sin(\\arccos(\\frac{3}{5}))."
        solution = "\\frac{4}{5}"
        steps = [
            "\\text{Let } \\theta = \\arccos(\\frac{3}{5})",
            "\\text{Then } \\cos(\\theta) = \\frac{3}{5}",
            "\\text{Using } \\sin^2(\\theta) + \\cos^2(\\theta) = 1:",
            "\\sin^2(\\theta) = 1 - (\\frac{3}{5})^2 = 1 - \\frac{9}{25} = \\frac{16}{25}",
            "\\sin(\\theta) = \\frac{4}{5}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = InversesTrigFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
