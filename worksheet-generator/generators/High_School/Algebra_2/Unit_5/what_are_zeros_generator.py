"""
What Are Zeros Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WhatAreZerosGenerator:
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
                latex = f"\\text{{Find zeros of }} f(x) = x - {a}"
                solution = f"x = {a}"
                steps = [f"Set f(x) = 0", f"x - {a} = 0", f"x = {a}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                a = random.randint(1, 5)
                b = random.randint(1, 6)
                latex = f"\\text{{Find zeros of }} f(x) = (x - {a})(x + {b})"
                solution = f"x = {a}, x = -{b}"
                steps = [f"Set each factor = 0", f"x - {a} = 0 \\rightarrow x = {a}", f"x + {b} = 0 \\rightarrow x = -{b}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                a = random.randint(1, 4)
                b = random.randint(1, 5)
                c = a + b
                d = a * b
                latex = f"\\text{{Find zeros of }} f(x) = x^2 - {c}x + {d}"
                solution = f"x = {a}, x = {b}"
                steps = [f"Factor: (x - {a})(x - {b})", f"Set each factor = 0", f"Zeros: x = {a}, x = {b}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                a = random.randint(1, 3)
                b = random.randint(1, 4)
                c = random.randint(1, 4)
                latex = f"\\text{{Find zeros of }} f(x) = {a}x^3 - {a*b*c}x"
                solution = f"x = 0, x = \\pm\\sqrt{{{b*c}}}"
                steps = [f"Factor: {a}x(x^2 - {b*c})", f"x = 0 or x^2 = {b*c}", f"Zeros: x = 0, \\pm\\sqrt{{{b*c}}}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WhatAreZerosGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
