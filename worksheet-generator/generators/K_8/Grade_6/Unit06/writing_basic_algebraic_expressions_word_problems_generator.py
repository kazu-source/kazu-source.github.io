"""Writing Basic Algebraic Expressions Word Problems Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class WritingBasicAlgebraicExpressionsWordProblemsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        n = random.randint(5, 15)
        latex = f"\\text{{Sarah has }}{n}\\text{{ more apples than Tom. Tom has }} x \\text{{ apples. Write expression for Sarah.}}"
        return Equation(latex=latex, solution=f"x + {n}", steps=[f"x + {n}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        n = random.randint(3, 8)
        latex = f"\\text{{A package has }}{n}\\text{{ times as many cookies as }} x\\text{{. Write expression.}}"
        return Equation(latex=latex, solution=f"{n}x", steps=[f"{n}x"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        cost, fee = random.randint(10, 25), random.randint(5, 15)
        latex = f"\\text{{Tickets cost }}\\${cost}\\text{{ each plus }}\\${fee}\\text{{ fee. Cost for }} x \\text{{ tickets?}}"
        return Equation(latex=latex, solution=f"{cost}x + {fee}", steps=[f"{cost}x + {fee}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        rate, hours = random.randint(12, 20), random.randint(35, 45)
        latex = f"\\text{{Work }}{hours}\\text{{ hours/week at }}\\${rate}\\text{{/hr. After }} x \\text{{ weeks?}}"
        return Equation(latex=latex, solution=f"{rate * hours}x", steps=[f"{rate} \\times {hours} \\times x = {rate*hours}x"], difficulty='challenge')

def main():
    gen = WritingBasicAlgebraicExpressionsWordProblemsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} = {p.solution}")
if __name__ == '__main__': main()
