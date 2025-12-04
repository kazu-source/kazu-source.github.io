"""
Polynomial Division by Linear Factors Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PolynomialDivisionLinearFactorsGenerator:
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
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        latex = f"(x^2 + {a+b}x + {a*b}) \\div (x + {a})"
        solution = f"x + {b}"
        steps = [f"Factor or use division", f"(x + {a})(x + {b}) \\div (x + {a})", f"Solution: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = a + b
        d = a * b
        latex = f"\\frac{{x^2 + {c}x + {d}}}{{x + {a}}}"
        solution = f"x + {b}"
        steps = [f"Divide x^2 by x: x", f"Multiply back and subtract", f"Result: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(1, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        coef2 = a + b
        coef1 = a*b + c
        coef0 = a*c
        latex = f"\\frac{{x^3 + {coef2}x^2 + {coef1}x + {coef0}}}{{x + {a}}}"
        solution = f"x^2 + {b}x + {c}"
        steps = [f"Use polynomial long division", f"Result: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 4)
        c = random.randint(1, 4)
        r = random.randint(1, 6)
        latex = f"\\frac{{x^3 + {a+b}x^2 + {a*b+c}x + {a*c+r}}}{{x + {a}}}"
        solution = f"x^2 + {b}x + {c} + \\frac{{{r}}}{{x + {a}}}"
        steps = [f"Long division with remainder", f"Result: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PolynomialDivisionLinearFactorsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
