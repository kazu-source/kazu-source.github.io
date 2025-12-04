"""
Standard Form Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class StandardFormGenerator:
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
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        c = random.randint(10, 30)

        latex = f"\\text{{Is }} {a}x + {b}y = {c} \\text{{ in standard form?}}"
        solution = "Yes"
        steps = ["Standard form: Ax + By = C", "All coefficients are integers", "Answer: Yes"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(12, 30)

        x_int = c / a
        y_int = c / b

        latex = f"\\text{{Find both intercepts of }} {a}x + {b}y = {c}"
        solution = f"x-int: {x_int:.1f}, y-int: {y_int:.1f}"
        steps = [f"X-intercept (y=0): {a}x = {c}, x = {x_int:.1f}", f"Y-intercept (x=0): {b}y = {c}, y = {y_int:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        m = random.randint(2, 6)
        b = random.randint(-8, 8)

        a = m
        c = b

        latex = f"\\text{{Convert }} y = {m}x + {b} \\text{{ to standard form}}"
        solution = f"-{m}x + y = {b}" if m > 0 else f"{abs(m)}x + y = {b}"
        steps = [f"Move x term: -{m}x + y = {b}", "Or multiply by -1 if needed", f"Standard form: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(12, 30)

        m = -a / b
        y_int = c / b

        latex = f"\\text{{Convert }} {a}x + {b}y = {c} \\text{{ to slope-intercept form}}"
        solution = f"y = {m:.1f}x + {y_int:.1f}"
        steps = [f"Solve for y: {b}y = -{a}x + {c}", f"y = -{a}/{b}x + {c}/{b}", f"y = {m:.1f}x + {y_int:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = StandardFormGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
