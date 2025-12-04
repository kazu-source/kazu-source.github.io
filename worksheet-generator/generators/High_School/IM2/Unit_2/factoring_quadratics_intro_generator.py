"""
Factoring Quadratics Introduction Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FactoringQuadraticsIntroGenerator:
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
        # x² + bx + c where factors are small positive integers
        p = random.randint(1, 5)
        q = random.randint(1, 5)
        b = p + q
        c = p * q

        latex = f"\\text{{Factor: }} x^2 + {b}x + {c}"
        solution = f"(x + {p})(x + {q})"
        steps = [
            f"Find two numbers that multiply to {c} and add to {b}",
            f"{p} × {q} = {c}",
            f"{p} + {q} = {b}",
            f"Answer: (x + {p})(x + {q})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # x² + bx + c with one or both factors negative
        p = random.randint(1, 6)
        q = random.randint(1, 6)

        sign_choice = random.choice(['both_neg', 'one_neg'])

        if sign_choice == 'both_neg':
            b = -(p + q)
            c = p * q
            latex = f"\\text{{Factor: }} x^2 - {p+q}x + {c}"
            solution = f"(x - {p})(x - {q})"
            steps = [
                f"Find two numbers that multiply to {c} and add to {b}",
                f"(-{p}) × (-{q}) = {c}",
                f"(-{p}) + (-{q}) = {b}",
                f"Answer: (x - {p})(x - {q})"
            ]
        else:  # one_neg
            if p > q:
                b = p - q
                c = -p * q
                latex = f"\\text{{Factor: }} x^2 + {b}x - {p*q}"
                solution = f"(x + {p})(x - {q})"
                steps = [
                    f"Find two numbers that multiply to {c} and add to {b}",
                    f"{p} × (-{q}) = {c}",
                    f"{p} + (-{q}) = {b}",
                    f"Answer: (x + {p})(x - {q})"
                ]
            else:
                b = q - p
                c = -p * q
                latex = f"\\text{{Factor: }} x^2 + {b}x - {p*q}"
                solution = f"(x + {q})(x - {p})"
                steps = [
                    f"Find two numbers that multiply to {c} and add to {b}",
                    f"{q} × (-{p}) = {c}",
                    f"{q} + (-{p}) = {b}",
                    f"Answer: (x + {q})(x - {p})"
                ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # ax² + bx + c where a > 1
        a = random.randint(2, 4)
        p = random.randint(1, 4)
        q = random.randint(1, 4)

        # (ax + p)(x + q) = ax² + (aq + p)x + pq
        b = a * q + p
        c = p * q

        latex = f"\\text{{Factor: }} {a}x^2 + {b}x + {c}"
        solution = f"({a}x + {p})(x + {q})"
        steps = [
            f"Find factors of {a} × {c} = {a*c} that add to {b}",
            f"Factors are {a*q} and {p}",
            f"{a}x² + {a*q}x + {p}x + {c}",
            f"{a}x(x + {q}) + {p}(x + {q})",
            f"({a}x + {p})(x + {q})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # ax² + bx + c with a > 1 and negative terms
        a = random.randint(2, 4)
        p = random.randint(1, 4)
        q = random.randint(1, 4)

        # (ax - p)(x - q) = ax² - (aq + p)x + pq
        b = -(a * q + p)
        c = p * q

        latex = f"\\text{{Factor: }} {a}x^2 - {abs(b)}x + {c}"
        solution = f"({a}x - {p})(x - {q})"
        steps = [
            f"Find factors of {a} × {c} = {a*c} that add to {b}",
            f"Factors are -{a*q} and -{p}",
            f"{a}x² - {a*q}x - {p}x + {c}",
            f"{a}x(x - {q}) - {p}(x - {q})",
            f"({a}x - {p})(x - {q})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FactoringQuadraticsIntroGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
