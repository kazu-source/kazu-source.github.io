"""
Combination Equation Types Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CombinationEquationTypesGenerator:
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
        b = random.randint(-8, 8)

        latex = f"\\text{{Identify the form: }} y = {m}x + {b}"
        solution = "Slope-intercept form"
        steps = ["Form: y = mx + b", "Answer: Slope-intercept form"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        c = random.randint(10, 30)

        latex = f"\\text{{Identify the form: }} {a}x + {b}y = {c}"
        solution = "Standard form"
        steps = ["Form: Ax + By = C", "Answer: Standard form"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        m = random.randint(2, 6)
        x1 = random.randint(1, 5)
        y1 = random.randint(2, 10)

        forms = [
            ("slope-intercept", f"y = {m}x + {y1 - m * x1}"),
            ("point-slope", f"y - {y1} = {m}(x - {x1})"),
            ("standard", f"{m}x - y = {m * x1 - y1}")
        ]

        form_type, equation = random.choice(forms)

        latex = f"\\text{{Identify the form: }} {equation}"
        solution = f"{form_type.title()} form"
        steps = [f"Pattern matches {form_type} form", f"Answer: {form_type.title()} form"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        m = random.randint(2, 5)
        x1 = random.randint(1, 4)
        y1 = random.randint(3, 10)
        b = y1 - m * x1

        latex = f"\\text{{Convert }} y - {y1} = {m}(x - {x1}) \\text{{ to both other forms}}"
        solution = f"Slope-intercept: y = {m}x + {b}, Standard: {m}x - y = {m*x1 - y1}"
        steps = [f"Slope-intercept: y = {m}x + {b}", f"Standard: {m}x - y = -{b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CombinationEquationTypesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
