"""One Step Equation Word Problems Generator - Grade 6 Unit 7"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class OneStepEquationWordProblemsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        x, b = random.randint(5, 20), random.randint(3, 12)
        latex = f"\\text{{Sarah has }}\\${b}\\text{{. After buying a book, she has }}\\${x}\\text{{. Book cost?}}"
        return Equation(latex=latex, solution=f"\\${b-x}", steps=[f"Cost = {b} - {x} = {b-x}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        x, a = random.randint(3, 15), random.randint(2, 6)
        latex = f"\\text{{A package of }} {a} \\text{{ pencils costs }}\\${a*x}\\text{{. Cost per pencil?}}"
        return Equation(latex=latex, solution=f"\\${x}", steps=[f"Cost per pencil = {a*x} \\div {a} = {x}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        x, fee = random.randint(15, 40), random.randint(5, 15)
        latex = f"\\text{{Total cost is }}\\${x+fee}\\text{{, including }}\\${fee}\\text{{ fee. Item cost?}}"
        return Equation(latex=latex, solution=f"\\${x}", steps=[f"Item cost = {x+fee} - {fee} = {x}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        total, num = random.randint(60, 120), random.randint(3, 8)
        while total % num != 0:
            total = random.randint(60, 120)
        per_person = total // num
        latex = f"\\text{{Group of }} {num} \\text{{ paid }}\\${total}\\text{{ total. Each paid equally. Amount per person?}}"
        return Equation(latex=latex, solution=f"\\${per_person}", steps=[f"Per person = {total} \\div {num} = {per_person}"], difficulty='challenge')

def main():
    gen = OneStepEquationWordProblemsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
