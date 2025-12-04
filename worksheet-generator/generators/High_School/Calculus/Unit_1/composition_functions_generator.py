"""
Composition of Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CompositionFunctionsGenerator:
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
        a = random.randint(2, 5)
        b = random.randint(1, 6)

        latex = f"f(x) = {a}x, g(x) = x + {b}. \\text{{ Find }} (f \\circ g)(x)."
        solution = f"{a}x + {a * b}"
        steps = [
            f"(f \\circ g)(x) = f(g(x))",
            f"= f(x + {b})",
            f"= {a}(x + {b})",
            f"= {a}x + {a * b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 5)
        c = random.randint(2, 4)

        latex = f"f(x) = {a}x + {b}, g(x) = {c}x. \\text{{ Find }} (f \\circ g)(x)."
        solution = f"{a * c}x + {b}"
        steps = [
            f"(f \\circ g)(x) = f(g(x))",
            f"= f({c}x)",
            f"= {a}({c}x) + {b}",
            f"= {a * c}x + {b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 5)
        c = random.randint(2, 4)
        d = random.randint(1, 5)

        latex = f"f(x) = {a}x + {b}, g(x) = {c}x + {d}. \\text{{ Find }} (f \\circ g)(x)."
        solution = f"{a * c}x + {a * d + b}"
        steps = [
            f"(f \\circ g)(x) = f(g(x))",
            f"= f({c}x + {d})",
            f"= {a}({c}x + {d}) + {b}",
            f"= {a * c}x + {a * d} + {b}",
            f"= {a * c}x + {a * d + b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        b = random.randint(1, 4)

        latex = f"f(x) = x^2, g(x) = {a}x + {b}. \\text{{ Find }} (f \\circ g)(x)."
        solution = f"{a**2}x^2 + {2*a*b}x + {b**2}"
        steps = [
            f"(f \\circ g)(x) = f(g(x))",
            f"= f({a}x + {b})",
            f"= ({a}x + {b})^2",
            f"= {a**2}x^2 + {2*a*b}x + {b**2}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CompositionFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
