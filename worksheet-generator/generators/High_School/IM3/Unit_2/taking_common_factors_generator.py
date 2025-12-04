"""
Taking Common Factors Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class TakingCommonFactorsGenerator:
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
        # Factor out common binomial
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        latex = f"\\text{{Factor: }} {a}(x + {c}) + {b}(x + {c})"
        solution = f"(x + {c})({a} + {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Factor by grouping - 4 terms
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        latex = f"\\text{{Factor by grouping: }} {a}x^3 + {a*c}x^2 + {b}x + {b*c}"
        solution = f"(x^2 + {c})({a}x + {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Complex grouping
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        latex = f"\\text{{Factor by grouping: }} {a}x^3 - {a*c}x^2 + {b}x - {b*c}"
        solution = f"(x^2 + {c})({a}x - {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Factor completely with GCF first then grouping
        gcf = random.randint(2, 4)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)

        coef1 = gcf * a
        coef2 = gcf * a * c
        coef3 = gcf * b
        coef4 = gcf * b * c

        latex = f"\\text{{Factor completely: }} {coef1}x^3 + {coef2}x^2 + {coef3}x + {coef4}"
        solution = f"{gcf}(x^2 + {c})({a}x + {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = TakingCommonFactorsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
