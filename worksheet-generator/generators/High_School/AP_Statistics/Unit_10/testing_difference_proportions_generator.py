"""
Testing Difference Proportions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class TestingDifferenceProportionsGenerator:
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
        question = "H0 for two proportions?"; solution = "p1 = p2"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        question = "Pooled proportion?"; solution = "Total successes / total n"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        question = "Why pool?"; solution = "Assumes H0 true (p1=p2)"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = "Test statistic?"; solution = "z = (p1-hat - p2-hat)/SE_pooled"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = TestingDifferenceProportionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
