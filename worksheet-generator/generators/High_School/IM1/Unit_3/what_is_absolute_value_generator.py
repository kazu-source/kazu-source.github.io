"""
What is Absolute Value Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WhatIsAbsoluteValueGenerator:
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
        a = random.randint(1, 20)

        latex = f"|{a}| = ?"
        solution = f"{a}"
        steps = [f"Absolute value of positive number is itself", f"|{a}| = {a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(1, 20)

        latex = f"|-{a}| = ?"
        solution = f"{a}"
        steps = [f"Absolute value makes negative positive", f"|-{a}| = {a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(3, 12)
        b = random.randint(1, 8)
        result = abs(a - b)

        latex = f"|{a} - {b}| = ?"
        solution = f"{result}"
        steps = [f"Evaluate inside: {a} - {b} = {a - b}", f"|{a - b}| = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(5, 15)
        c = random.randint(1, 6)
        inner = a - b
        result = abs(inner) + c

        latex = f"|{a} - {b}| + {c} = ?"
        solution = f"{result}"
        steps = [f"Evaluate inside: {a} - {b} = {inner}", f"|{inner}| = {abs(inner)}", f"{abs(inner)} + {c} = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WhatIsAbsoluteValueGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
