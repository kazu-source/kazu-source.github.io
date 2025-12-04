"""
Power Rule Ii Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PowerRuleIiGenerator:
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
        a = random.randint(2, 5)
        x = random.randint(10, 30)

        latex = f"\\text{{Solve problem about power rule ii}} (\\text{{easy}})"
        solution = f"{a * x}"
        steps = [
            f"\\text{{Step 1}}",
            f"\\text{{Solution: }} {a * x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(1, 4)

        latex = f"\\text{{Solve problem about power rule ii}} (\\text{{medium}})"
        solution = f"{a + b}"
        steps = [
            f"\\text{{Step 1}}",
            f"\\text{{Solution: }} {a + b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 3)

        latex = f"\\text{{Solve problem about power rule ii}} (\\text{{hard}})"
        solution = f"{a * b}"
        steps = [
            f"\\text{{Step 1}}",
            f"\\text{{Solution: }} {a * b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        b = random.randint(2, 3)

        latex = f"\\text{{Solve problem about power rule ii}} (\\text{{challenge}})"
        solution = f"{a ** b}"
        steps = [
            f"\\text{{Step 1}}",
            f"\\text{{Solution: }} {a ** b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PowerRuleIiGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
