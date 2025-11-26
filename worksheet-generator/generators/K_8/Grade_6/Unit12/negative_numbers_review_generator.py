"""Negative Numbers Review Generator - Grade 6 Unit 12"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class NegativeNumbersReviewGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        num = random.randint(1, 20)
        latex = f"\\text{{What is the opposite of {num}?}}"
        return Equation(latex=latex, solution=f"-{num}", steps=[f"Opposite: -{num}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        num1, num2 = random.randint(-15, 15), random.randint(-15, 15)
        while num1 == num2:
            num2 = random.randint(-15, 15)
        comp = ">" if num1 > num2 else "<"
        latex = f"\\text{{Compare: {num1} ___ {num2}}}"
        return Equation(latex=latex, solution=comp, steps=[f"{num1} {comp} {num2}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        nums = [random.randint(-20, 20) for _ in range(5)]
        sorted_nums = sorted(nums)
        latex = f"\\text{{Order from least to greatest: {', '.join(map(str, nums))}}}"
        return Equation(latex=latex, solution=', '.join(map(str, sorted_nums)), steps=[f"Ordered: {', '.join(map(str, sorted_nums))}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        num = random.randint(-20, 20)
        abs_val = abs(num)
        latex = f"\\text{{Find absolute value: |{num}|}}"
        return Equation(latex=latex, solution=str(abs_val), steps=[f"|{num}| = {abs_val}"], difficulty='challenge')

def main():
    gen = NegativeNumbersReviewGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
