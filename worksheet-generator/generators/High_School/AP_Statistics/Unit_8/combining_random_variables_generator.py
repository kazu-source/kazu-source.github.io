"""
Combining Random Variables Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CombiningRandomVariablesGenerator:
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
        question = "E(X)=10, E(Y)=20. E(X+Y)?"; solution = "30"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        question = "Var(X)=4, Var(Y)=9, independent. Var(X+Y)?"; solution = "13"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        question = "SD(X)=2, SD(Y)=3, independent. SD(X+Y)?"; solution = "sqrt(13)"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = "E(X)=5, E(Y)=8. E(X-Y)?"; solution = "-3"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = CombiningRandomVariablesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
