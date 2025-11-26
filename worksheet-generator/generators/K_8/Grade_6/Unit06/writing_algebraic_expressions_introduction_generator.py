"""Writing Algebraic Expressions Introduction Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class WritingAlgebraicExpressionsIntroductionGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        n = random.randint(3, 9)
        latex = f"\\text{{Write: a number plus }}{n}"
        return Equation(latex=latex, solution=f"x + {n}", steps=[f"x + {n}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        n = random.randint(2, 8)
        latex = f"\\text{{Write: a number times }}{n}"
        return Equation(latex=latex, solution=f"{n}x", steps=[f"{n}x"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        n = random.randint(2, 7)
        m = random.randint(3, 9)
        latex = f"\\text{{Write: }}{n}\\text{{ times a number, minus }}{m}"
        return Equation(latex=latex, solution=f"{n}x - {m}", steps=[f"{n}x - {m}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        n = random.randint(2, 6)
        latex = f"\\text{{Write: the square of a number, divided by }}{n}"
        return Equation(latex=latex, solution=f"\\frac{{x^2}}{{{n}}}", steps=[f"x^2 \\div {n}"], difficulty='challenge')

def main():
    gen = WritingAlgebraicExpressionsIntroductionGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} = {p.solution}")
if __name__ == '__main__': main()
