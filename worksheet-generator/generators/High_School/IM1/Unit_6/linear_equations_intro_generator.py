"""
Linear Equations Intro Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LinearEquationsIntroGenerator:
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
        b = random.randint(1, 12)

        latex = f"\\text{{Is }} y = {a}x + {b} \\text{{ a linear equation?}}"
        solution = "Yes"
        steps = ["Form is y = mx + b", "Highest power of x is 1", "Answer: Yes, it is linear"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 7)
        b = random.randint(1, 10)

        latex = f"\\text{{Is }} y = {a}x^2 + {b} \\text{{ a linear equation?}}"
        solution = "No"
        steps = ["Has x^2 term", "Highest power of x is 2", "Answer: No, it is not linear"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        m = random.randint(2, 8)
        b = random.randint(-10, 10)

        latex = f"\\text{{Identify the slope and y-intercept of }} y = {m}x + {b}"
        solution = f"slope = {m}, y-intercept = {b}"
        steps = [f"Form: y = mx + b", f"Slope m = {m}", f"Y-intercept b = {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        m = random.randint(2, 6)
        b = random.randint(-8, 8)
        x_val = random.randint(1, 5)
        y_val = m * x_val + b

        latex = f"\\text{{For }} y = {m}x + {b}\\text{{, find y when }} x = {x_val}"
        solution = f"y = {y_val}"
        steps = [f"Substitute x = {x_val}", f"y = {m}({x_val}) + {b}", f"y = {m * x_val} + {b}", f"y = {y_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = LinearEquationsIntroGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
