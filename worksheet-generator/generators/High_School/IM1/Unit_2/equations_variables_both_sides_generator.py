"""
Equations Variables Both Sides Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EquationsVariablesBothSidesGenerator:
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
        a = random.randint(3, 8)
        b = random.randint(1, 6)
        c = random.randint(1, 10)

        x_val = c

        latex = f"{a}x = {b}x + {c}"
        solution = f"x = {c // (a - b)}"
        steps = [f"Subtract {b}x from both sides", f"{a - b}x = {c}", f"Divide by {a - b}", f"x = {c // (a - b)}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(4, 9)
        b = random.randint(2, 6)
        c = random.randint(5, 15)
        d = random.randint(1, 8)

        latex = f"{a}x + {c} = {b}x + {d}"
        x_val = (d - c) // (a - b) if (d - c) % (a - b) == 0 else (d - c + 1) // (a - b)
        solution = f"x = {x_val}"
        steps = [f"Subtract {b}x from both sides: {a - b}x + {c} = {d}", f"Subtract {c} from both sides: {a - b}x = {d - c}", f"Divide by {a - b}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(5, 10)
        b = random.randint(2, 7)
        c = random.randint(3, 12)
        d = random.randint(8, 20)

        latex = f"{a}x - {c} = {b}x + {d}"
        x_val = (d + c) // (a - b)
        solution = f"x = {x_val}"
        steps = [f"Subtract {b}x: {a - b}x - {c} = {d}", f"Add {c}: {a - b}x = {d + c}", f"Divide by {a - b}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(3, 7)
        b = random.randint(2, 5)
        c = random.randint(1, 6)
        d = random.randint(2, 5)
        e = random.randint(1, 8)

        # ax + b = cx - dx + e
        # Simplify right: (c-d)x + e
        right_coef = c - d
        x_val = (e - b) // (a - right_coef) if a != right_coef else 0

        latex = f"{a}x + {b} = {c}x - {d}x + {e}"
        solution = f"x = {x_val}"
        steps = [f"Simplify right: {c}x - {d}x = {right_coef}x", f"Equation: {a}x + {b} = {right_coef}x + {e}", f"Subtract {right_coef}x: {a - right_coef}x + {b} = {e}", f"Subtract {b}: {a - right_coef}x = {e - b}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = EquationsVariablesBothSidesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
