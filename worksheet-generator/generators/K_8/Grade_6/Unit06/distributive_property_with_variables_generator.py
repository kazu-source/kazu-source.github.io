"""Distributive Property with Variables Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class DistributivePropertyWithVariablesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        a, b = random.randint(2, 9), random.randint(2, 9)
        latex = f"\\text{{Expand: }}{a}(x + {b})"
        return Equation(latex=latex, solution=f"{a}x + {a*b}", steps=[f"{a}x + {a*b}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        a, b, c = random.randint(2, 7), random.randint(2, 7), random.randint(2, 7)
        latex = f"\\text{{Expand: }}{a}({b}x + {c})"
        return Equation(latex=latex, solution=f"{a*b}x + {a*c}", steps=[f"{a*b}x + {a*c}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        a, b, c = random.randint(2, 6), random.randint(2, 6), random.randint(2, 6)
        latex = f"\\text{{Expand: }}{a}(x - {b}) + {c}"
        return Equation(latex=latex, solution=f"{a}x - {a*b} + {c}", steps=[f"{a}x - {a*b} + {c}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        a, b, c, d = random.randint(2, 5), random.randint(2, 5), random.randint(2, 5), random.randint(2, 5)
        latex = f"\\text{{Expand: }}{a}({b}x + {c}y + {d})"
        return Equation(latex=latex, solution=f"{a*b}x + {a*c}y + {a*d}", steps=[f"{a*b}x + {a*c}y + {a*d}"], difficulty='challenge')

def main():
    gen = DistributivePropertyWithVariablesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex} = {p.solution}")
if __name__ == '__main__': main()
