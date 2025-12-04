"""
Limits with Division Law Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LimitsDivisionLawGenerator:
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
        b = random.randint(1, 4)
        c = random.randint(2, 4)

        latex = f"\\text{{Evaluate }} \\lim_{{x \\to {c}}} \\frac{{{a}x}}{{{b}}}."
        result = (a * c) / b
        solution = f"{result:.2f}" if result != int(result) else f"{int(result)}"
        steps = [
            f"= \\frac{{{a}({c})}}{{{b}}}",
            f"= \\frac{{{a*c}}}{{{b}}}",
            f"= {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        c = random.randint(1, 4)

        latex = f"\\text{{Evaluate }} \\lim_{{x \\to {c}}} \\frac{{x+1}}{{x}}."
        result = (c + 1) / c
        solution = f"{result:.2f}" if result != int(result) else f"{int(result)}"
        steps = [
            f"= \\frac{{{c}+1}}{{{c}}}",
            f"= \\frac{{{c+1}}}{{{c}}}",
            f"= {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Evaluate } \\lim_{x \\to 3} \\frac{x^2-9}{x-3}."
        solution = "6"
        steps = [
            "= \\lim_{x \\to 3} \\frac{(x-3)(x+3)}{x-3}",
            "= \\lim_{x \\to 3} (x+3)",
            "= 6"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Evaluate } \\lim_{x \\to 0} \\frac{\\sin(3x)}{x}."
        solution = "3"
        steps = [
            "= 3 \\cdot \\lim_{x \\to 0} \\frac{\\sin(3x)}{3x}",
            "= 3 \\cdot 1",
            "= 3"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = LimitsDivisionLawGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
