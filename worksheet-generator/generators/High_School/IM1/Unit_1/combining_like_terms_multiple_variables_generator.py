"""
Combining Like Terms Multiple Variables Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CombiningLikeTermsMultipleVariablesGenerator:
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
        a = random.randint(2, 8)
        b = random.randint(1, 9)
        c = random.randint(1, 7)
        d = random.randint(1, 8)

        latex = f"\\text{{Simplify: }} {a}x + {b}y + {c}x + {d}y"
        x_coef = a + c
        y_coef = b + d
        solution = f"{x_coef}x + {y_coef}y"
        steps = [f"Combine x terms: {a}x + {c}x = {x_coef}x", f"Combine y terms: {b}y + {d}y = {y_coef}y", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(3, 8)
        b = random.randint(2, 7)
        c = random.randint(1, 6)
        d = random.randint(1, 9)
        e = random.randint(1, 8)

        x_coef = a + c
        y_coef = b + d

        latex = f"\\text{{Simplify: }} {a}x + {b}y + {c}x + {d}y + {e}"
        solution = f"{x_coef}x + {y_coef}y + {e}"
        steps = [f"Combine x: {a}x + {c}x = {x_coef}x", f"Combine y: {b}y + {d}y = {y_coef}y", f"Keep constant: {e}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(4, 9)
        b = random.randint(2, 7)
        c = random.randint(1, 6)
        d = random.randint(3, 8)
        e = random.randint(1, 5)

        x_coef = a - c
        y_coef = b + d

        latex = f"\\text{{Simplify: }} {a}x + {b}y - {c}x + {d}y + {e}"
        solution = f"{x_coef}x + {y_coef}y + {e}"
        steps = [f"Combine x: {a}x - {c}x = {x_coef}x", f"Combine y: {b}y + {d}y = {y_coef}y", f"Keep constant: {e}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(3, 7)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(2, 6)
        e = random.randint(1, 5)
        f = random.randint(1, 4)
        g = random.randint(1, 8)

        x_coef = a + c - e
        y_coef = b - d
        z_coef = f

        latex = f"\\text{{Simplify: }} {a}x + {b}y + {c}x - {d}y + {f}z - {e}x + {g}"
        if y_coef >= 0:
            solution = f"{x_coef}x + {y_coef}y + {z_coef}z + {g}"
        else:
            solution = f"{x_coef}x - {abs(y_coef)}y + {z_coef}z + {g}"
        steps = [f"Combine x: {a}x + {c}x - {e}x = {x_coef}x", f"Combine y: {b}y - {d}y = {y_coef}y", f"z term: {z_coef}z", f"Constant: {g}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CombiningLikeTermsMultipleVariablesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
