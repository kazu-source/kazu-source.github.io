"""
Intervals of Positive and Negative Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class IntervalsPosNegGenerator:
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
                latex = f"\\text{{When is }} f(x) = x - {a} \\text{{ positive?}}"
                solution = f"x > {a}"
                steps = [f"Set f(x) > 0", f"x - {a} > 0", f"x > {a}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                a = random.randint(1, 5)
                b = random.randint(a+1, 8)
                latex = f"\\text{{When is }} f(x) = (x - {a})(x - {b}) \\text{{ negative?}}"
                solution = f"{a} < x < {b}"
                steps = [f"Zeros at x = {a}, {b}", f"Test intervals", f"Negative between zeros: {a} < x < {b}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                a = random.randint(1, 3)
                b = random.randint(4, 7)
                c = random.randint(8, 10)
                latex = f"\\text{{Find where }} f(x) = (x - {a})(x - {b})(x - {c}) > 0"
                solution = f"({a}, {b}) \\cup ({c}, \\infty)"
                steps = [f"Zeros: {a}, {b}, {c}", f"Test intervals", f"Positive on: ({a}, {b}) \\cup ({c}, \\infty)"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                a = random.randint(1, 4)
                b = a + random.randint(2, 4)
                latex = f"\\text{{Find where }} f(x) = \\frac{{(x - {a})}}{{(x - {b})}} \\leq 0"
                solution = f"[{a}, {b})"
                steps = [f"Zero at x = {a}", f"Vertical asymptote at x = {b}", f"Negative/zero on: [{a}, {b})"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = IntervalsPosNegGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
