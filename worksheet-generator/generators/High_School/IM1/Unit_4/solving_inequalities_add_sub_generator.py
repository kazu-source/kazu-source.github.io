"""
Solving Inequalities Add/Sub Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingInequalitiesAddSubGenerator:
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
        b = random.randint(5, 20)

        latex = f"x + {a} < {b}"
        solution = f"x < {b - a}"
        steps = [f"Subtract {a} from both sides", f"x < {b} - {a}", f"x < {b - a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(5, 15)
        b = random.randint(1, 10)

        latex = f"x - {b} > {a}"
        solution = f"x > {a + b}"
        steps = [f"Add {b} to both sides", f"x > {a} + {b}", f"x > {a + b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(8, 20)
        b = random.randint(3, 12)
        op = random.choice(['\\leq', '\\geq'])

        if op == '\\leq':
            latex = f"{a} \\geq x + {b}"
            solution = f"x \\leq {a - b}"
            steps = [f"Subtract {b} from both sides", f"{a - b} \\geq x", f"x \\leq {a - b}"]
        else:
            latex = f"{a} \\leq x - {b}"
            solution = f"x \\geq {a + b}"
            steps = [f"Add {b} to both sides", f"{a + b} \\leq x", f"x \\geq {a + b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(10, 25)
        b = random.randint(3, 10)
        c = random.randint(1, 8)

        latex = f"x + {b} - {c} \\leq {a}"
        combined = b - c
        solution = f"x \\leq {a - combined}"
        steps = [f"Simplify left: x + {b} - {c} = x + {combined}", f"x + {combined} \\leq {a}", f"Subtract {combined} from both sides", f"x \\leq {a - combined}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingInequalitiesAddSubGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
