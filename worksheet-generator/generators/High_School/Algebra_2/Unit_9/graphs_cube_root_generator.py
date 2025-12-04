"""
Graphs Cube Root Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphsCubeRootGenerator:
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
        latex = f"{a}x + {b}"
        solution = f"{a}x + {b}"
        steps = ["Step 1", "Step 2"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 10)
        b = random.randint(1, 10)
        latex = f"{a}x^2 + {b}"
        solution = f"{a}x^2 + {b}"
        steps = ["Step 1", "Step 2"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 10)
        b = random.randint(1, 10)
        latex = f"{a}x^3 + {b}x"
        solution = f"{a}x^3 + {b}x"
        steps = ["Step 1", "Step 2"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 10)
        b = random.randint(1, 10)
        latex = f"{a}x^4 + {b}x^2"
        solution = f"{a}x^4 + {b}x^2"
        steps = ["Step 1", "Step 2", "Step 3"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GraphsCubeRootGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
