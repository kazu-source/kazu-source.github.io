"""
Dividing Quadratics by Linear Factors Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DividingQuadraticsLinearFactorsGenerator:
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
        b = random.randint(2, 8)
        latex = f"\\frac{{{a*b}x^2}}{{{b}x}}"
        solution = f"{a}x"
        steps = [f"Divide coefficients: {a*b}/{b} = {a}", f"Subtract exponents: x^2/x = x", f"Result: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(1, 5)
        b = random.randint(2, 6)
        c = a + b
        d = a * b
        latex = f"(x^2 + {c}x + {d}) \\div (x + {a})"
        solution = f"x + {b}"
        steps = [f"Factor numerator: (x + {a})(x + {b})", f"Cancel (x + {a})", f"Result: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        r = random.randint(1, 5)
        latex = f"\\frac{{x^2 + {a+b}x + {a*b+r}}}{{x + {a}}}"
        solution = f"x + {b} + \\frac{{{r}}}{{x + {a}}}"
        steps = [f"Division gives quotient x + {b}", f"Remainder: {r}", f"Result: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(2, 5)
        coef = c * a
        latex = f"\\frac{{{c}x^2 + {c*(a+b)}x + {c*a*b}}}{{x + {a}}}"
        solution = f"{c}x + {c*b}"
        steps = [f"Factor out {c}: {c}(x^2 + {a+b}x + {a*b})", f"Divide: {c}(x + {b})", f"Result: {{solution}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = DividingQuadraticsLinearFactorsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
