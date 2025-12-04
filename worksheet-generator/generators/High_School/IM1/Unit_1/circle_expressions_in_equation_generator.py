"""
Circle Expressions in Equation Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CircleExpressionsInEquationGenerator:
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
        c = random.randint(1, 15)

        latex = f"\\text{{Circle the expression in: }} {a}x + {b} = {c}"
        solution = f"{a}x + {b}"
        steps = [f"The left side {a}x + {b} is an expression", f"The right side {c} is also an expression", f"Both sides of = are expressions"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(1, 10)
        c = random.randint(1, 12)
        d = random.randint(1, 15)

        latex = f"\\text{{Circle all expressions in: }} {a}x + {b} = {c}x - {d}"
        solution = f"{a}x + {b} and {c}x - {d}"
        steps = [f"Left side is expression: {a}x + {b}", f"Right side is expression: {c}x - {d}", "Both sides are expressions"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 7)
        b = random.randint(1, 9)
        c = random.randint(1, 8)
        d = random.randint(1, 12)
        e = random.randint(1, 10)

        latex = f"\\text{{Circle all expressions in: }} {a}({b}x - {c}) = {d}x + {e}"
        solution = f"{a}({b}x - {c}), {b}x - {c}, {d}x + {e}"
        steps = [f"Left side: {a}({b}x - {c}) is an expression", f"Inside parentheses: {b}x - {c} is also an expression", f"Right side: {d}x + {e} is an expression"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(1, 7)
        d = random.randint(2, 5)
        e = random.randint(1, 9)
        f = random.randint(1, 12)

        latex = f"\\text{{Circle all expressions in: }} {a}({b}x + {c}) - {d}x = {e}({f} - x)"
        solution = f"{a}({b}x + {c}) - {d}x, {b}x + {c}, {e}({f} - x), {f} - x"
        steps = [f"Left side: {a}({b}x + {c}) - {d}x", f"Inside left parentheses: {b}x + {c}", f"Right side: {e}({f} - x)", f"Inside right parentheses: {f} - x"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CircleExpressionsInEquationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
