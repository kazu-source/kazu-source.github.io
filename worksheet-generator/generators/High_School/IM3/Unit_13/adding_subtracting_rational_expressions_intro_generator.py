"""
Adding and Subtracting Rational Expressions Introduction Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AddingSubtractingRationalExpressionsIntroGenerator:
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
        # Same denominator
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = random.randint(2, 9)

        latex = f"\\frac{{{a}}}{{x}} + \\frac{{{b}}}{{x}}"
        solution = f"\\frac{{{a+b}}}{{x}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Different monomial denominators
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        latex = f"\\frac{{{a}}}{{x}} + \\frac{{{b}}}{{y}}"
        solution = f"\\frac{{{a}y + {b}x}}{{xy}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # LCD with numbers
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\frac{{{a}}}{{x}} + \\frac{{{b}}}{{2x}}"
        solution = f"\\frac{{{2*a + b}}}{{2x}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Different binomial denominators
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\frac{{1}}{{x + {a}}} + \\frac{{1}}{{x + {b}}}"
        solution = f"\\frac{{2x + {a+b}}}{{(x + {a})(x + {b})}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = AddingSubtractingRationalExpressionsIntroGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
