"""
Adding and Subtracting Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class AddingSubtractingPolynomialsGenerator:
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
        # Adding simple polynomials
        a1, b1, c1 = random.randint(1, 5), random.randint(-9, 9), random.randint(-9, 9)
        a2, b2, c2 = random.randint(1, 5), random.randint(-9, 9), random.randint(-9, 9)

        a_sum = a1 + a2
        b_sum = b1 + b2
        c_sum = c1 + c2

        latex = f"({a1}x^2 + {b1}x + {c1}) + ({a2}x^2 + {b2}x + {c2})"
        solution = f"{a_sum}x^2 + {b_sum}x + {c_sum}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Subtracting polynomials
        a1, b1, c1 = random.randint(3, 9), random.randint(-9, 9), random.randint(-9, 9)
        a2, b2, c2 = random.randint(1, 5), random.randint(-9, 9), random.randint(-9, 9)

        a_diff = a1 - a2
        b_diff = b1 - b2
        c_diff = c1 - c2

        latex = f"({a1}x^2 + {b1}x + {c1}) - ({a2}x^2 + {b2}x + {c2})"
        solution = f"{a_diff}x^2 + {b_diff}x + {c_diff}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Adding/subtracting cubic polynomials
        a1, b1, c1, d1 = random.randint(1, 5), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9)
        a2, b2, c2, d2 = random.randint(1, 5), random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9)

        op = random.choice(['+', '-'])

        if op == '+':
            a_res, b_res, c_res, d_res = a1+a2, b1+b2, c1+c2, d1+d2
            latex = f"({a1}x^3 + {b1}x^2 + {c1}x + {d1}) + ({a2}x^3 + {b2}x^2 + {c2}x + {d2})"
        else:
            a_res, b_res, c_res, d_res = a1-a2, b1-b2, c1-c2, d1-d2
            latex = f"({a1}x^3 + {b1}x^2 + {c1}x + {d1}) - ({a2}x^3 + {b2}x^2 + {c2}x + {d2})"

        solution = f"{a_res}x^3 + {b_res}x^2 + {c_res}x + {d_res}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Multiple operations with mixed degrees
        a1, b1, c1 = random.randint(1, 5), random.randint(-9, 9), random.randint(-9, 9)
        a2, b2, c2 = random.randint(1, 5), random.randint(-9, 9), random.randint(-9, 9)
        a3, b3, c3 = random.randint(1, 5), random.randint(-9, 9), random.randint(-9, 9)

        a_res = a1 + a2 - a3
        b_res = b1 + b2 - b3
        c_res = c1 + c2 - c3

        latex = f"({a1}x^2 + {b1}x + {c1}) + ({a2}x^2 + {b2}x + {c2}) - ({a3}x^2 + {b3}x + {c3})"
        solution = f"{a_res}x^2 + {b_res}x + {c_res}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = AddingSubtractingPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
