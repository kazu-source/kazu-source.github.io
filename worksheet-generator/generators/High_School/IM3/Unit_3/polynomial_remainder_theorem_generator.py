"""
Polynomial Remainder Theorem Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PolynomialRemainderTheoremGenerator:
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
        # Find remainder using theorem
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        # Evaluate at x = -a
        remainder = (-a)**2 + b*(-a) + c

        latex = f"\\text{{Find remainder when }} x^2 + {b}x + {c} \\text{{ is divided by }} x + {a}"
        solution = f"{remainder}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Cubic polynomial remainder
        a = random.randint(1, 3)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        # f(-a)
        remainder = (-a)**3 + b*(-a)**2 + c*(-a) + d

        latex = f"\\text{{Find remainder: }} \\frac{{x^3 + {b}x^2 + {c}x + {d}}}{{x + {a}}}"
        solution = f"{remainder}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Use remainder theorem to find value
        a = random.randint(1, 4)
        k = random.randint(-9, 9)
        target_remainder = random.randint(1, 20)

        # f(a) = a^2 + ka + something = target_remainder
        # something = target_remainder - a^2 - ka
        const = target_remainder - a**2 - k*a

        latex = f"\\text{{If }} f(x) = x^2 + {k}x + {const}\\text{{, find }} f({a})"
        solution = f"{target_remainder}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Factor theorem application
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        # Check if (x - a) is a factor
        remainder = a**2 + b*a + c

        if remainder == 0:
            latex = f"\\text{{Is }} (x - {a}) \\text{{ a factor of }} x^2 + {b}x + {c}?"
            solution = "Yes (remainder is 0)"
        else:
            latex = f"\\text{{Is }} (x - {a}) \\text{{ a factor of }} x^2 + {b}x + {c}?"
            solution = f"No (remainder is {remainder})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = PolynomialRemainderTheoremGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
