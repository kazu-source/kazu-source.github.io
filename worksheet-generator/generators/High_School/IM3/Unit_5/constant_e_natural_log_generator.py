"""
Constant e and Natural Log Generator
"""
import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ConstantENaturalLogGenerator:
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
        # Simple natural log
        exp = random.randint(1, 5)

        latex = f"\\ln(e^{{{exp}}})"
        solution = f"{exp}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Convert to exponential form
        value = random.randint(2, 20)

        latex = f"\\text{{If }} \\ln(x) = {value}\\text{{, find }} x"
        solution = f"x = e^{{{value}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Natural log properties
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        latex = f"\\text{{Simplify: }} \\ln(e^{{{a}}}) + \\ln(e^{{{b}}})"
        solution = f"{a + b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Solve equation with e
        k = random.randint(2, 9)
        value = random.randint(10, 100)

        latex = f"\\text{{Solve: }} e^x = {value}"
        solution = f"x = \\ln({value})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ConstantENaturalLogGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
