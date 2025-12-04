"""
Chain Rule Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ChainRuleGenerator:
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
        # (ax + b)^n
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        n = random.randint(2, 4)

        latex = f"\\text{{Find }} \\frac{{d}}{{dx}}[({a}x + {b})^{n}]"
        # Derivative: n(ax+b)^(n-1) * a
        coef = n * a
        new_exp = n - 1
        solution = f"{coef}({a}x + {b})^{new_exp}"
        steps = [
            f"\\text{{Let }} u = {a}x + {b}",
            f"\\frac{{du}}{{dx}} = {a}",
            f"\\frac{{d}}{{dx}}[u^{n}] = {n}u^{{{new_exp}}} \\cdot \\frac{{du}}{{dx}}",
            f"= {n}({a}x + {b})^{{{new_exp}}} \\cdot {a}",
            f"= {coef}({a}x + {b})^{{{new_exp}}}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # sin(ax) or cos(ax)
        a = random.randint(2, 5)
        func_type = random.choice(['sin', 'cos'])

        if func_type == 'sin':
            latex = f"\\text{{Find }} \\frac{{d}}{{dx}}[\\sin({a}x)]"
            solution = f"{a}\\cos({a}x)"
            steps = [
                f"\\text{{Let }} u = {a}x",
                f"\\frac{{du}}{{dx}} = {a}",
                f"\\frac{{d}}{{dx}}[\\sin(u)] = \\cos(u) \\cdot \\frac{{du}}{{dx}}",
                f"= \\cos({a}x) \\cdot {a}",
                f"= {a}\\cos({a}x)"
            ]
        else:
            latex = f"\\text{{Find }} \\frac{{d}}{{dx}}[\\cos({a}x)]"
            solution = f"-{a}\\sin({a}x)"
            steps = [
                f"\\text{{Let }} u = {a}x",
                f"\\frac{{du}}{{dx}} = {a}",
                f"\\frac{{d}}{{dx}}[\\cos(u)] = -\\sin(u) \\cdot \\frac{{du}}{{dx}}",
                f"= -\\sin({a}x) \\cdot {a}",
                f"= -{a}\\sin({a}x)"
            ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # e^(ax^2)
        a = random.randint(2, 4)

        latex = f"\\text{{Find }} \\frac{{d}}{{dx}}[e^{{{a}x^2}}]"
        coef = 2 * a
        solution = f"{coef}x \\cdot e^{{{a}x^2}}"
        steps = [
            f"\\text{{Let }} u = {a}x^2",
            f"\\frac{{du}}{{dx}} = {coef}x",
            f"\\frac{{d}}{{dx}}[e^u] = e^u \\cdot \\frac{{du}}{{dx}}",
            f"= e^{{{a}x^2}} \\cdot {coef}x",
            f"= {coef}x \\cdot e^{{{a}x^2}}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # ln(sin(x)) or similar nested function
        a = random.randint(2, 4)

        latex = f"\\text{{Find }} \\frac{{d}}{{dx}}[\\ln(\\sin({a}x))]"
        solution = f"{a}\\cot({a}x)"
        steps = [
            f"\\text{{Let }} u = \\sin({a}x)",
            f"\\frac{{d}}{{dx}}[\\ln(u)] = \\frac{{1}}{{u}} \\cdot \\frac{{du}}{{dx}}",
            f"\\frac{{du}}{{dx}} = {a}\\cos({a}x)",
            f"= \\frac{{{a}\\cos({a}x)}}{{\\sin({a}x)}}",
            f"= {a}\\cot({a}x)"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ChainRuleGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
