"""
Combining Like Terms Full Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CombiningLikeTermsFullGenerator:
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
        a = random.randint(3, 8)
        b = random.randint(2, 7)
        c = random.randint(1, 6)
        d = random.randint(1, 9)

        x_coef = a + b

        latex = f"\\text{{Simplify: }} {a}x + {c} + {b}x - {d}"
        const = c - d
        if const >= 0:
            solution = f"{x_coef}x + {const}"
        else:
            solution = f"{x_coef}x - {abs(const)}"
        steps = [f"Combine x: {a}x + {b}x = {x_coef}x", f"Combine constants: {c} - {d} = {const}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(3, 7)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(2, 6)
        e = random.randint(1, 8)

        x2_coef = a + b
        x1_coef = c

        latex = f"\\text{{Simplify: }} {a}x^2 + {c}x + {b}x^2 - {d} + {e}"
        const = e - d
        if const >= 0:
            solution = f"{x2_coef}x^2 + {x1_coef}x + {const}"
        else:
            solution = f"{x2_coef}x^2 + {x1_coef}x - {abs(const)}"
        steps = [f"Combine x^2: {a}x^2 + {b}x^2 = {x2_coef}x^2", f"x term: {c}x", f"Constants: {e} - {d} = {const}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(3, 7)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(2, 5)
        e = random.randint(1, 4)
        f = random.randint(1, 7)

        x2_coef = a - c
        x1_coef = b + d

        latex = f"\\text{{Simplify: }} {a}x^2 + {b}x - {c}x^2 + {d}x + {e} - {f}"
        const = e - f
        if const >= 0:
            solution = f"{x2_coef}x^2 + {x1_coef}x + {const}"
        else:
            solution = f"{x2_coef}x^2 + {x1_coef}x - {abs(const)}"
        steps = [f"Combine x^2: {a}x^2 - {c}x^2 = {x2_coef}x^2", f"Combine x: {b}x + {d}x = {x1_coef}x", f"Combine constants: {e} - {f} = {const}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        c = random.randint(1, 4)
        d = random.randint(1, 4)
        e = random.randint(1, 3)
        f = random.randint(1, 4)
        g = random.randint(1, 6)
        h = random.randint(1, 5)

        x2_coef = a + c - e
        x1_coef = b - d + f
        const = g - h

        latex = f"\\text{{Simplify: }} {a}x^2 + {b}x + {c}x^2 - {d}x - {e}x^2 + {f}x + {g} - {h}"
        if const >= 0:
            solution = f"{x2_coef}x^2 + {x1_coef}x + {const}"
        else:
            solution = f"{x2_coef}x^2 + {x1_coef}x - {abs(const)}"
        steps = [f"Combine x^2: {a} + {c} - {e} = {x2_coef}", f"Combine x: {b} - {d} + {f} = {x1_coef}", f"Combine constants: {g} - {h} = {const}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CombiningLikeTermsFullGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
