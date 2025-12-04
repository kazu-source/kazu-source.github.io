"""
Determine if Limit Exists Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DetermineLimitExistsGenerator:
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
        x_val = random.randint(1, 5)
        val = random.randint(3, 8)

        latex = f"\\text{{If }} \\lim_{{x \\to {x_val}^-}} f(x) = {val} \\text{{ and }} \\lim_{{x \\to {x_val}^+}} f(x) = {val}, \\text{{ does }} \\lim_{{x \\to {x_val}}} f(x) \\text{{ exist?}}"
        solution = "Yes"
        steps = [
            f"\\text{{Left limit: }} {val}",
            f"\\text{{Right limit: }} {val}",
            "\\text{Both equal, so limit exists}",
            f"\\lim_{{x \\to {x_val}}} f(x) = {val}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_val = random.randint(1, 5)
        left_val = random.randint(2, 5)
        right_val = left_val + random.randint(1, 3)

        latex = f"\\text{{If }} \\lim_{{x \\to {x_val}^-}} f(x) = {left_val} \\text{{ and }} \\lim_{{x \\to {x_val}^+}} f(x) = {right_val}, \\text{{ does the limit exist?}}"
        solution = "No"
        steps = [
            f"\\text{{Left limit: }} {left_val}",
            f"\\text{{Right limit: }} {right_val}",
            f"{left_val} \\neq {right_val}",
            "\\text{Limits not equal, so limit does not exist}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Does } \\lim_{x \\to 0} \\frac{|x|}{x} \\text{ exist?}"
        solution = "No"
        steps = [
            "\\lim_{x \\to 0^-} \\frac{|x|}{x} = \\lim_{x \\to 0^-} \\frac{-x}{x} = -1",
            "\\lim_{x \\to 0^+} \\frac{|x|}{x} = \\lim_{x \\to 0^+} \\frac{x}{x} = 1",
            "-1 \\neq 1",
            "\\text{Limit does not exist}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Does } \\lim_{x \\to 2} \\frac{x^2-4}{x-2} \\text{ exist?}"
        solution = "Yes, equals 4"
        steps = [
            "\\frac{x^2-4}{x-2} = \\frac{(x-2)(x+2)}{x-2} = x+2 \\text{ for } x \\neq 2",
            "\\lim_{x \\to 2} (x+2) = 4",
            "\\text{Removable discontinuity}",
            "\\text{Limit exists and equals 4}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = DetermineLimitExistsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
