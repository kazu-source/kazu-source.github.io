"""
Combining Like Terms First Power Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CombiningLikeTermsFirstPowerGenerator:
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
        result = a + b
        var = random.choice(['x', 'y', 'n'])

        latex = f"\\text{{Simplify: }} {a}{var} + {b}{var}"
        solution = f"{result}{var}"
        steps = [f"Both terms have variable {var}", f"{a} + {b} = {result}", f"Answer: {result}{var}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(3, 9)
        b = random.randint(1, 7)
        c = random.randint(1, 10)
        result = a + b
        var = random.choice(['x', 'y', 'm'])

        latex = f"\\text{{Simplify: }} {a}{var} + {c} + {b}{var}"
        solution = f"{result}{var} + {c}"
        steps = [f"Combine like terms: {a}{var} + {b}{var}", f"{a} + {b} = {result}", f"Keep constant: + {c}", f"Answer: {result}{var} + {c}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(4, 9)
        b = random.randint(2, 7)
        c = random.randint(1, 6)
        result = a - b
        var = random.choice(['x', 'y', 'a'])

        if result > 0:
            latex = f"\\text{{Simplify: }} {a}{var} - {b}{var} + {c}"
            solution = f"{result}{var} + {c}"
            steps = [f"Combine: {a}{var} - {b}{var}", f"{a} - {b} = {result}", f"Answer: {result}{var} + {c}"]
        else:
            result = abs(result)
            latex = f"\\text{{Simplify: }} {a}{var} - {b}{var} + {c}"
            solution = f"-{result}{var} + {c}"
            steps = [f"Combine: {a}{var} - {b}{var}", f"{a} - {b} = -{result}", f"Answer: -{result}{var} + {c}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(3, 8)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(1, 9)
        e = random.randint(1, 7)
        result_x = a + b - c
        result_const = d - e
        var = random.choice(['x', 'y', 'n'])

        latex = f"\\text{{Simplify: }} {a}{var} + {d} + {b}{var} - {c}{var} - {e}"
        solution = f"{result_x}{var} + {result_const}" if result_const >= 0 else f"{result_x}{var} - {abs(result_const)}"
        steps = [f"Combine {var} terms: {a}{var} + {b}{var} - {c}{var} = {result_x}{var}", f"Combine constants: {d} - {e} = {result_const}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CombiningLikeTermsFirstPowerGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
