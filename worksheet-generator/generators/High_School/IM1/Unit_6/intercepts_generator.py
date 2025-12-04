"""
Intercepts Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class InterceptsGenerator:
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
        b = random.randint(-10, 10)

        latex = f"\\text{{Find the y-intercept of }} y = {m}x + {b}"
        solution = f"{b}"
        steps = ["Y-intercept is where x = 0", f"When x = 0, y = {b}", f"Answer: {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 6)
        b = random.randint(1, 15)
        x_int = -b / m

        latex = f"\\text{{Find the x-intercept of }} y = {m}x + {b}"
        solution = f"x = {x_int:.1f}"
        steps = ["X-intercept is where y = 0", f"0 = {m}x + {b}", f"{m}x = -{b}", f"x = -{b}/{m} = {x_int:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        m = random.randint(2, 5)
        b = random.randint(-8, 8)
        x_int = -b / m

        latex = f"\\text{{Find both intercepts of }} y = {m}x + {b}"
        solution = f"x-intercept: {x_int:.1f}, y-intercept: {b}"
        steps = [f"Y-intercept: x = 0, y = {b}", f"X-intercept: y = 0", f"0 = {m}x + {b}, x = {x_int:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(2, 10)
        c = random.randint(10, 30)

        latex = f"\\text{{Find both intercepts of }} {a}x + {b}y = {c}"
        x_int = c / a
        y_int = c / b
        solution = f"x-intercept: {x_int:.1f}, y-intercept: {y_int:.1f}"
        steps = [f"X-intercept (y=0): {a}x = {c}, x = {x_int:.1f}", f"Y-intercept (x=0): {b}y = {c}, y = {y_int:.1f}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = InterceptsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
