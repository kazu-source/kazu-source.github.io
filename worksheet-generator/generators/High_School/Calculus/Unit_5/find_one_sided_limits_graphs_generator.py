"""
Find One-Sided Limits from Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FindOneSidedLimitsGraphsGenerator:
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
        left_val = random.randint(2, 6)

        latex = f"\\text{{From a graph, find }} \\lim_{{x \\to {x_val}^-}} f(x) \\text{{ if the left side approaches }} {left_val}."
        solution = f"{left_val}"
        steps = [
            f"\\text{{Left-hand limit (from left): }} {left_val}",
            f"\\lim_{{x \\to {x_val}^-}} f(x) = {left_val}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_val = random.randint(1, 5)
        right_val = random.randint(3, 7)

        latex = f"\\text{{From a graph, find }} \\lim_{{x \\to {x_val}^+}} f(x) \\text{{ if the right side approaches }} {right_val}."
        solution = f"{right_val}"
        steps = [
            f"\\text{{Right-hand limit (from right): }} {right_val}",
            f"\\lim_{{x \\to {x_val}^+}} f(x) = {right_val}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(1, 4)

        latex = f"\\text{{Find }} \\lim_{{x \\to {x_val}^-}} \\frac{{1}}{{x-{x_val}}}."
        solution = "-\\infty"
        steps = [
            f"\\text{{As }} x \\to {x_val}^-, x - {x_val} \\to 0^-",
            f"\\frac{{1}}{{x-{x_val}}} \\to -\\infty"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Find } \\lim_{x \\to 0^+} \\frac{1}{x}."
        solution = "\\infty"
        steps = [
            "\\text{As } x \\to 0^+, x \\to 0 \\text{ from positive side}",
            "\\frac{1}{x} \\to \\infty"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FindOneSidedLimitsGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
