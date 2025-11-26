"""Equivalent Expressions Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class EquivalentExpressionsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        a, b = random.randint(2, 9), random.randint(2, 9)
        latex = f"\\text{{Are }}{a}x + {b}x\\text{{ and }}{a+b}x\\text{{ equivalent?}}"
        return Equation(latex=latex, solution="Yes", steps=["Yes, they are equivalent"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        a, b, c = random.randint(2, 7), random.randint(2, 7), random.randint(2, 7)
        latex = f"\\text{{Are }}{a}(x + {b})\\text{{ and }}{a}x + {a*b}\\text{{ equivalent?}}"
        return Equation(latex=latex, solution="Yes", steps=["Yes, by distributive property"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        a, b, c = random.randint(2, 6), random.randint(2, 6), random.randint(2, 6)
        wrong = a * b + 1
        latex = f"\\text{{Are }}{a}(x + {b})\\text{{ and }}{a}x + {wrong}\\text{{ equivalent?}}"
        return Equation(latex=latex, solution="No", steps=[f"No, {a}(x+{b}) = {a}x + {a*b}, not {a}x + {wrong}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        a, b, c = random.randint(2, 5), random.randint(2, 5), random.randint(2, 5)
        latex = f"\\text{{Write an expression equivalent to }}{a}x + {b}x + {c}"
        return Equation(latex=latex, solution=f"{a+b}x + {c}", steps=[f"Combine like terms: {a+b}x + {c}"], difficulty='challenge')

def main():
    gen = EquivalentExpressionsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
