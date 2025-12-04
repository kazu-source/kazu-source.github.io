"""
Residuals Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ResidualsGenerator:
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
        y_actual, y_pred = 50, 45
        question = f"Actual={y_actual}, Predicted={y_pred}. Find residual"
        solution = f"Residual = {y_actual - y_pred}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        question = "Residual = 10. Was prediction too high or low?"
        solution = "Too low (actual > predicted)"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        residuals = [2, -3, 1, 4, -2]
        question = "Residuals: 2,-3,1,4,-2. Sum?"
        solution = "Sum close to 0"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = "Residual plot shows fan shape. What?"
        solution = "Non-constant variance (heteroscedasticity)"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ResidualsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
