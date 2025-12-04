"""
Factoring Using Structure Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FactoringUsingStructureGenerator:
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
        # Perfect square trinomial
        a = random.randint(1, 5)

        latex = f"\\text{{Factor: }} x^2 + {2*a}x + {a**2}"
        solution = f"(x + {a})^2"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Difference of squares
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        latex = f"\\text{{Factor: }} {a**2}x^2 - {b**2}"
        solution = f"({a}x + {b})({a}x - {b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Sum of cubes
        a = random.randint(1, 5)

        latex = f"\\text{{Factor: }} x^3 + {a**3}"
        solution = f"(x + {a})(x^2 - {a}x + {a**2})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Difference of cubes
        a = random.randint(2, 5)

        latex = f"\\text{{Factor: }} x^3 - {a**3}"
        solution = f"(x - {a})(x^2 + {a}x + {a**2})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = FactoringUsingStructureGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
