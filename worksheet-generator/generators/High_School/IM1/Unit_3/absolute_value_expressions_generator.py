"""
Absolute Value Expressions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AbsoluteValueExpressionsGenerator:
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
        b = random.randint(1, 10)
        x_val = random.randint(1, 5)
        result = abs(a * x_val + b)

        latex = f"\\text{{Evaluate }} |{a}x + {b}| \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Substitute x = {x_val}", f"|{a}({x_val}) + {b}|", f"|{a * x_val} + {b}|", f"|{a * x_val + b}| = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(5, 15)
        x_val = random.randint(1, 4)
        inner = a * x_val - b
        result = abs(inner)

        latex = f"\\text{{Evaluate }} |{a}x - {b}| \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Substitute x = {x_val}", f"|{a}({x_val}) - {b}|", f"|{a * x_val} - {b}|", f"|{inner}| = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(1, 5)
        x_val = random.randint(-3, -1)
        inner = a * x_val + b
        result = abs(inner) - c

        latex = f"\\text{{Evaluate }} |{a}x + {b}| - {c} \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Substitute x = {x_val}", f"|{a}({x_val}) + {b}| - {c}", f"|{a * x_val} + {b}| - {c}", f"|{inner}| - {c}", f"{abs(inner)} - {c} = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(1, 6)
        c = random.randint(2, 7)
        d = random.randint(1, 5)
        x_val = random.randint(-2, 2)

        inner1 = a * x_val - b
        inner2 = c * x_val + d
        result = abs(inner1) + abs(inner2)

        latex = f"\\text{{Evaluate }} |{a}x - {b}| + |{c}x + {d}| \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Substitute x = {x_val}", f"|{a * x_val} - {b}| + |{c * x_val} + {d}|", f"|{inner1}| + |{inner2}|", f"{abs(inner1)} + {abs(inner2)} = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = AbsoluteValueExpressionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
