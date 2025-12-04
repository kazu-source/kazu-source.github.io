"""
Find Limits from Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FindLimitsGraphsGenerator:
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
        y_val = random.randint(2, 8)

        latex = f"\\text{{From a graph, if }} f(x) \\text{{ approaches }} {y_val} \\text{{ as }} x \\to {x_val}, \\text{{ find }} \\lim_{{x \\to {x_val}}} f(x)."
        solution = f"{y_val}"
        steps = [
            f"\\text{{Graph shows function approaches }} {y_val}",
            f"\\lim_{{x \\to {x_val}}} f(x) = {y_val}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_val = random.randint(1, 5)
        a = random.randint(1, 3)
        b = random.randint(1, 5)

        latex = f"\\text{{Evaluate }} \\lim_{{x \\to {x_val}}} ({a}x + {b})."
        result = a * x_val + b
        solution = f"{result}"
        steps = [
            f"\\text{{Substitute }} x = {x_val}:",
            f"= {a}({x_val}) + {b}",
            f"= {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Evaluate } \\lim_{x \\to 2} \\frac{x^2-4}{x-2}."
        solution = "4"
        steps = [
            "\\frac{x^2-4}{x-2} = \\frac{(x-2)(x+2)}{x-2}",
            "= x + 2 \\text{ for } x \\neq 2",
            "\\lim_{x \\to 2} (x+2) = 4"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Evaluate } \\lim_{x \\to 0} \\frac{\\sin(x)}{x}."
        solution = "1"
        steps = [
            "\\text{Standard limit from calculus:}",
            "\\lim_{x \\to 0} \\frac{\\sin(x)}{x} = 1"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FindLimitsGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
