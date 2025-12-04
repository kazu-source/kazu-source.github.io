"""
Solving Equations Parenthesis Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingEquationsParenthesisGenerator:
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
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(10, 25)
        x_val = (c - a * b) // a

        latex = f"{a}(x + {b}) = {c}"
        solution = f"x = {x_val}"
        steps = [f"Distribute: {a}x + {a * b} = {c}", f"Subtract {a * b} from both sides", f"{a}x = {c - a * b}", f"Divide by {a}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 7)
        c = random.randint(1, 6)
        result = a * b - a * c

        latex = f"{a}({b}x - {c}) = {result}"
        solution = f"x = {b // 1}"
        steps = [f"Distribute: {a * b}x - {a * c} = {result}", f"Add {a * c} to both sides", f"{a * b}x = {result + a * c}", f"Divide by {a * b}", f"x = {(result + a * c) // (a * b)}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(8, 20)

        x_val = (d - c) // (a * b)

        latex = f"{a}({b}x + {c}) = {d}"
        solution = f"x = {x_val}"
        steps = [f"Distribute: {a * b}x + {a * c} = {d}", f"Subtract {a * c}: {a * b}x = {d - a * c}", f"Divide by {a * b}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(2, 5)
        c = random.randint(1, 4)
        d = random.randint(1, 6)
        e = random.randint(10, 25)

        # a(bx + c) + dx = e
        x_coef = a * b + d
        const = a * c
        x_val = (e - const) // x_coef

        latex = f"{a}({b}x + {c}) + {d}x = {e}"
        solution = f"x = {x_val}"
        steps = [f"Distribute: {a * b}x + {a * c} + {d}x = {e}", f"Combine: {x_coef}x + {const} = {e}", f"Subtract {const}: {x_coef}x = {e - const}", f"Divide by {x_coef}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingEquationsParenthesisGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
