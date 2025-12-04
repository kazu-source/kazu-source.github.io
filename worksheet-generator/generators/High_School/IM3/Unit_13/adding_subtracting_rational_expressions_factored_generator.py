"""
Adding and Subtracting Rational Expressions with Factored Denominators Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AddingSubtractingRationalExpressionsFactoredGenerator:
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
        # Common binomial factor
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\frac{{1}}{{x + {a}}} + \\frac{{2}}{{x + {a}}}"
        solution = f"\\frac{{3}}{{x + {a}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # LCD is one of the denominators
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\frac{{1}}{{x + {a}}} + \\frac{{1}}{{(x + {a})(x + {b})}}"
        solution = f"\\frac{{x + {a+b}}}{{(x + {a})(x + {b})}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # LCD requires factoring
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\frac{{1}}{{x^2 - {a**2}}} + \\frac{{1}}{{x - {a}}}"
        solution = f"\\frac{{x + {a} + 1}}{{(x + {a})(x - {a})}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex denominators
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\frac{{x}}{{x^2 - {a**2}}} - \\frac{{1}}{{x + {a}}}"
        solution = f"\\frac{{x - (x - {a})}}{{(x + {a})(x - {a})}} = \\frac{{{a}}}{{(x + {a})(x - {a})}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = AddingSubtractingRationalExpressionsFactoredGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
