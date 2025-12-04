"""
End Behavior of Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EndBehaviorPolynomialsGenerator:
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
        # Even degree, positive leading coefficient
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Describe end behavior: }} f(x) = {a}x^2 + {b}x"
        solution = "As x → -∞, f(x) → ∞; As x → ∞, f(x) → ∞"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Odd degree, positive leading coefficient
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{Describe end behavior: }} f(x) = {a}x^3 + {b}x^2"
        solution = "As x → -∞, f(x) → -∞; As x → ∞, f(x) → ∞"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Negative leading coefficient
        a = random.randint(-5, -1)
        b = random.randint(1, 5)
        degree = random.choice([2, 4])

        if degree == 2:
            latex = f"\\text{{Describe end behavior: }} f(x) = {a}x^2 + {b}x"
            solution = "As x → -∞, f(x) → -∞; As x → ∞, f(x) → -∞"
        else:
            latex = f"\\text{{Describe end behavior: }} f(x) = {a}x^4 + {b}x^2"
            solution = "As x → -∞, f(x) → -∞; As x → ∞, f(x) → -∞"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # High degree with negative leading coefficient
        a = random.randint(-3, -1)
        b = random.randint(1, 5)

        latex = f"\\text{{Describe end behavior: }} f(x) = {a}x^5 + {b}x^3"
        solution = "As x → -∞, f(x) → ∞; As x → ∞, f(x) → -∞"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = EndBehaviorPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
