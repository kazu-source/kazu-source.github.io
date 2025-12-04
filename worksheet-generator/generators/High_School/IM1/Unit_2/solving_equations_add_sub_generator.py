"""
Solving Equations Add/Sub Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingEquationsAddSubGenerator:
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
        a = random.randint(1, 12)
        b = random.randint(1, 15)
        x_val = b - a

        latex = f"x + {a} = {b}"
        solution = f"x = {x_val}"
        steps = [f"Subtract {a} from both sides", f"x = {b} - {a}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(5, 15)
        b = random.randint(1, 10)
        x_val = a + b

        latex = f"x - {b} = {a}"
        solution = f"x = {x_val}"
        steps = [f"Add {b} to both sides", f"x = {a} + {b}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(8, 20)
        b = random.randint(3, 12)
        x_val = a - b

        latex = f"{a} = x + {b}"
        solution = f"x = {x_val}"
        steps = [f"Subtract {b} from both sides", f"{a} - {b} = x", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(5, 15)
        b = random.randint(3, 10)
        c = random.randint(1, 8)
        x_val = a + b - c

        latex = f"x + {c} - {b} = {a}"
        solution = f"x = {x_val}"
        steps = [f"Simplify left: x + {c} - {b} = x + {c - b}", f"x + {c - b} = {a}", f"Subtract {c - b} from both sides" if c > b else f"Subtract {c - b} from both sides", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingEquationsAddSubGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
