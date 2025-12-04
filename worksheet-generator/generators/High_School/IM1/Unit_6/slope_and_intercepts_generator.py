"""
Slope and Intercepts Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SlopeAndInterceptsGenerator:
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
        m = random.randint(2, 8)
        b = random.randint(-10, 10)

        latex = f"\\text{{Find slope and y-intercept of }} y = {m}x + {b}"
        solution = f"slope = {m}, y-intercept = {b}"
        steps = [f"Form: y = mx + b", f"Slope m = {m}", f"Y-intercept b = {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 6)
        b = random.randint(-8, 8)

        latex = f"\\text{{Write the equation with slope {m} and y-intercept {b}}}"
        solution = f"y = {m}x + {b}"
        steps = ["Use y = mx + b", f"m = {m}, b = {b}", f"y = {m}x + {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        m = random.randint(2, 5)
        b = random.randint(-6, 6)
        x_int = -b / m

        latex = f"\\text{{For }} y = {m}x + {b}\\text{{, find slope, y-intercept, and x-intercept}}"
        solution = f"slope: {m}, y-int: {b}, x-int: {x_int:.1f}"
        steps = [f"Slope = {m}", f"Y-intercept = {b}", f"X-intercept: 0 = {m}x + {b}, x = {x_int:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 8)
        c = random.randint(10, 25)

        m = -a / b
        y_int = c / b

        latex = f"\\text{{Rewrite }} {a}x + {b}y = {c} \\text{{ in slope-intercept form}}"
        solution = f"y = {m:.1f}x + {y_int:.1f}"
        steps = [f"Solve for y: {b}y = -{a}x + {c}", f"y = -{a}/{b}x + {c}/{b}", f"y = {m:.1f}x + {y_int:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SlopeAndInterceptsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
