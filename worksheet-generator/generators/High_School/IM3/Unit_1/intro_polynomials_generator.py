"""
Introduction to Polynomials Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class IntroPolynomialsGenerator:
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
        # Identify degree and leading coefficient
        a = random.randint(1, 5)
        b = random.randint(-9, 9)
        c = random.randint(-9, 9)
        degree = random.randint(2, 3)

        if degree == 2:
            latex = f"\\text{{Identify the degree and leading coefficient of }} {a}x^2 + {b}x + {c}"
            solution = f"Degree: 2, Leading coefficient: {a}"
        else:
            latex = f"\\text{{Identify the degree and leading coefficient of }} {a}x^3 + {b}x^2 + {c}x"
            solution = f"Degree: 3, Leading coefficient: {a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Classify polynomial by degree
        a = random.randint(1, 5)
        b = random.randint(-9, 9)
        c = random.randint(-9, 9)
        d = random.randint(-9, 9)

        poly_type = random.choice(['quadratic', 'cubic', 'quartic'])

        if poly_type == 'quadratic':
            latex = f"\\text{{Classify }} {a}x^2 + {b}x + {c} \\text{{ by degree}}"
            solution = "Quadratic (degree 2)"
        elif poly_type == 'cubic':
            latex = f"\\text{{Classify }} {a}x^3 + {b}x^2 + {c}x + {d} \\text{{ by degree}}"
            solution = "Cubic (degree 3)"
        else:
            latex = f"\\text{{Classify }} {a}x^4 + {b}x^3 + {c}x^2 + {d} \\text{{ by degree}}"
            solution = "Quartic (degree 4)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Standard form and number of terms
        a = random.randint(1, 5)
        b = random.randint(-9, 9)
        c = random.randint(-9, 9)

        latex = f"\\text{{Write in standard form: }} {b}x + {a}x^3 + {c}"
        solution = f"{a}x^3 + {b}x + {c} (3 terms, trinomial)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Identify all characteristics
        a = random.randint(2, 5)
        b = random.randint(-9, 9)
        c = random.randint(-9, 9)
        d = random.randint(-9, 9)

        latex = f"\\text{{For }} f(x) = {a}x^4 + {b}x^3 + {c}x + {d}\\text{{, identify degree, leading coefficient, constant term, and number of terms}}"
        solution = f"Degree: 4, Leading coefficient: {a}, Constant: {d}, Terms: 4 (polynomial)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = IntroPolynomialsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
