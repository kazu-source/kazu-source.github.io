"""
Equivalent Expressions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EquivalentExpressionsGenerator:
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
        b = random.randint(1, 7)
        c = a + b

        latex = f"\\text{{Are }} {a}x + {b}x \\text{{ and }} {c}x \\text{{ equivalent?}}"
        solution = "Yes"
        steps = [f"Combine like terms: {a}x + {b}x", f"{a} + {b} = {c}", f"{c}x = {c}x", "Answer: Yes, equivalent"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(1, 7)
        result = a * b + a * c

        latex = f"\\text{{Are }} {a}({b}x + {c}) \\text{{ and }} {a*b}x + {a*c} \\text{{ equivalent?}}"
        solution = "Yes"
        steps = [f"Distribute: {a}({b}x + {c})", f"= {a}·{b}x + {a}·{c}", f"= {a*b}x + {a*c}", "Answer: Yes, equivalent"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 7)
        c = random.randint(1, 5)
        d = random.randint(1, 6)

        # Create two forms of same expression
        combined = a + b
        total_const = c + d

        latex = f"\\text{{Show }} {a}x + {c} + {b}x + {d} \\text{{ is equivalent to }} {combined}x + {total_const}"
        solution = "Yes, they are equivalent"
        steps = [f"Simplify left side:", f"Combine x: {a}x + {b}x = {combined}x", f"Combine constants: {c} + {d} = {total_const}", f"Result: {combined}x + {total_const}", "Both expressions are equal"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(1, 4)

        # a(bx + c) + dx = abx + ac + dx
        result_x = a * b + d
        result_const = a * c

        latex = f"\\text{{Show }} {a}({b}x + {c}) + {d}x \\text{{ is equivalent to }} {result_x}x + {result_const}"
        solution = "Yes, they are equivalent"
        steps = [f"Distribute: {a}({b}x + {c}) = {a*b}x + {a*c}", f"Add {d}x: {a*b}x + {d}x = {result_x}x", f"Final: {result_x}x + {result_const}", "Both expressions are equal"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = EquivalentExpressionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
