"""
Limits of Trigonometric Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LimitsTrigonometricGenerator:
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
        c = random.randint(1, 4)
        latex = f"\\lim_{{x \\to {c}}} {a}x^2"
        result = a * c**2
        solution = f"{result}"
        steps = [f"= {a}({c})^2 = {result}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        c = random.randint(2, 4)
        latex = f"\\lim_{{x \\to {c}}} \\sqrt{{x+1}}"
        result = (c+1)**0.5
        solution = f"{result:.2f}"
        steps = [f"= \\sqrt{{{c}+1}} = {solution}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\lim_{x \\to 4} \\frac{\\sqrt{x}-2}{x-4}"
        solution = "\\frac{1}{4}"
        steps = ["\\text{Rationalize numerator}", "= \\frac{1}{4}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\lim_{x \\to 0} \\frac{1-\\cos(x)}{x^2}"
        solution = "\\frac{1}{2}"
        steps = ["\\text{Use L'Hopital or trig identity}", "= \\frac{1}{2}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = LimitsTrigonometricGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
