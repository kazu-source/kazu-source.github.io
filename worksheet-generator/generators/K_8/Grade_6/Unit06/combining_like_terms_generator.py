"""Combining Like Terms Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class CombiningLikeTermsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        a, b = random.randint(2, 9), random.randint(2, 9)
        latex = f"\\text{{Simplify: }}{a}x + {b}x"
        return Equation(latex=latex, solution=f"{a+b}x", steps=[f"{a+b}x"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        a, b, c = random.randint(2, 7), random.randint(2, 7), random.randint(2, 9)
        latex = f"\\text{{Simplify: }}{a}x + {b}x + {c}"
        return Equation(latex=latex, solution=f"{a+b}x + {c}", steps=[f"{a+b}x + {c}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        a, b, c, d = random.randint(2, 6), random.randint(2, 6), random.randint(2, 6), random.randint(2, 6)
        latex = f"\\text{{Simplify: }}{a}x + {b}y + {c}x + {d}y"
        return Equation(latex=latex, solution=f"{a+c}x + {b+d}y", steps=[f"{a+c}x + {b+d}y"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        a, b, c, d, e = random.randint(2, 5), random.randint(2, 5), random.randint(2, 5), random.randint(2, 5), random.randint(3, 9)
        latex = f"\\text{{Simplify: }}{a}x + {b} + {c}x - {d} + {e}"
        return Equation(latex=latex, solution=f"{a+c}x + {b-d+e}", steps=[f"{a+c}x + {b-d+e}"], difficulty='challenge')

def main():
    gen = CombiningLikeTermsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} = {p.solution}")
if __name__ == '__main__': main()
