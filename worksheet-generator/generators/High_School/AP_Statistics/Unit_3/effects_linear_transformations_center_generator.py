"""
Effects of Linear Transformations on Center Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EffectsLinearTransformationsCenterGenerator:
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
        data = [10, 15, 20, 25, 30]
        question = f"\\text{{Data: {', '.join(map(str, data))}. Add 5 to each. What is new mean?}}"
        solution = f"{sum(data)/len(data) + 5}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        data = [12, 18, 24]
        question = f"\\text{{Original mean is {sum(data)/len(data)}. Multiply each by 3. New mean?}}"
        solution = f"{sum(data)/len(data) * 3}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        question = "\\text{{Mean=50, std=10. Transform: }}\\ y = 2x + 5\\text{{. New mean?}}"
        solution = "New mean = 105"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = "\\text{{Explain why adding constant k to all values adds k to mean but}}\\text{{doesn't change median position. Give example.}}"
        solution = "Adding constant shifts all values equally, so mean shifts by k. Median is middle value, which shifts but relative position unchanged. Ex: [1,2,3] median=2, [6,7,8] median=7"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = EffectsLinearTransformationsCenterGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
