"""
Normal Distribution - Working with Areas Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class NormalDistributionWorkingAreasGenerator:
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
        question = "Standard normal. Find area between z=-1 and z=1"
        solution = "0.6826 or about 68%"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        question = "Normal: mean=65, SD=5. Find area above 70"
        z = (70-65)/5
        solution = f"z={z}, area = 0.1587 or 15.87%"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        question = "Normal: mean=100, SD=10. Find 25th percentile"
        z = -0.67
        x = 100 + (-0.67)*10
        solution = f"z=-0.67, x={round(x,1)}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = "Find IQR for standard normal distribution"
        solution = "Q1 at z=-0.67, Q3 at z=0.67, IQR = 1.34"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = NormalDistributionWorkingAreasGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
