"""
Equations of Parallel and Perpendicular Lines Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class EquationsParallelPerpendicularLinesGenerator:
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
        m = random.randint(2, 7)
        b1 = random.randint(-8, 8)
        b2 = random.randint(-8, 8)
        while b2 == b1:
            b2 = random.randint(-8, 8)
        latex = f"\\text{{Are }} y = {m}x + {b1} \\text{{ and }} y = {m}x + {b2} \\text{{ parallel, perpendicular, or neither?}}"
        solution = "Parallel"
        steps = ["\\text{Same slope, different y-intercepts}", "\\text{Lines are parallel}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 5)
        b1 = random.randint(-6, 6)
        x0, y0 = random.randint(1, 6), random.randint(1, 6)
        b2 = y0 - m * x0
        latex = f"\\text{{Write equation of line through }} ({x0},{y0}) \\text{{ parallel to }} y = {m}x + {b1}."
        solution = f"y = {m}x + {b2:.0f}"
        steps = [f"\\text{{Parallel lines have same slope: }} m = {m}",
                f"\\text{{Using point-slope: }} y - {y0} = {m}(x - {x0})",
                f"y = {m}x + {b2:.0f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        m = random.randint(2, 6)
        b1 = random.randint(-6, 6)
        perp_m = -1 / m
        x0, y0 = random.randint(2, 8), random.randint(2, 8)
        b2 = y0 - perp_m * x0
        latex = f"\\text{{Write equation of line through }} ({x0},{y0}) \\text{{ perpendicular to }} y = {m}x + {b1}."
        solution = f"y = {perp_m:.3f}x + {b2:.2f}"
        steps = [f"m_{{\\perp}} = -\\frac{{1}}{{{m}}} = {perp_m:.3f}",
                f"y - {y0} = {perp_m:.3f}(x - {x0})",
                f"y = {perp_m:.3f}x + {b2:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # General form Ax + By = C
        a, b, c = random.randint(2, 6), random.randint(2, 6), random.randint(5, 15)
        m = -a / b
        perp_m = b / a
        x0, y0 = random.randint(1, 5), random.randint(1, 5)
        new_b = y0 - perp_m * x0
        latex = f"\\text{{Write equation perpendicular to }} {a}x + {b}y = {c} \\text{{ through }} ({x0},{y0})."
        solution = f"y = {perp_m:.2f}x + {new_b:.2f}"
        steps = [f"\\text{{Convert to slope-intercept: }} y = {m:.2f}x + {c/b:.2f}",
                f"m_{{\\perp}} = -\\frac{{1}}{{{m:.2f}}} = {perp_m:.2f}",
                f"y - {y0} = {perp_m:.2f}(x - {x0})",
                f"y = {perp_m:.2f}x + {new_b:.2f}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = EquationsParallelPerpendicularLinesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
