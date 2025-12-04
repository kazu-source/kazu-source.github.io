"""
Mean and SD Random Variables Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MeanStdRandomVariablesGenerator:
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
        question = "P(X=1)=0.6, P(X=2)=0.4. E(X)?"; solution = "1.4"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        question = "E(X)=10. E(2X+5)?"; solution = "25"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        question = "Var(X)=4. SD(X)?"; solution = "2"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = "E(X)=5, SD=2. E(3X)?"; solution = "15"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = MeanStdRandomVariablesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
