"""
Imaginary Unit i Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ImaginaryUnitIGenerator:
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
        power = random.choice([2, 3, 4])
        results = {2: "-1", 3: "-i", 4: "1"}
        latex = f"\\text{{Simplify: }} i^{{{power}}}"
        solution = results[power]
        steps = [
            "i² = -1",
            f"i³ = i² · i = -i" if power >= 3 else "",
            f"i⁴ = i² · i² = 1" if power == 4 else "",
            f"i^{power} = {results[power]}"
        ]
        steps = [s for s in steps if s]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        power = random.randint(5, 12)
        remainder = power % 4
        results = {0: "1", 1: "i", 2: "-1", 3: "-i"}
        latex = f"\\text{{Simplify: }} i^{{{power}}}"
        solution = results[remainder]
        steps = [
            f"i^{power} = i^{{4·{power//4} + {remainder}}}",
            f"= (i⁴)^{power//4} · i^{remainder}",
            f"= 1^{power//4} · i^{remainder}",
            f"= i^{remainder} = {results[remainder]}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        n = random.randint(1, 15)
        latex = f"\\text{{Simplify: }} \\sqrt{{-{n}}}"
        solution = f"i\\sqrt{{{n}}}"
        steps = [
            f"√(-{n}) = √({n} · (-1))",
            f"= √{n} · √(-1)",
            f"= √{n} · i",
            f"= i√{n}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 6)
        n = random.randint(1, 10)
        latex = f"\\text{{Simplify: }} {a}\\sqrt{{-{n}}}"
        solution = f"{a}i\\sqrt{{{n}}}"
        steps = [
            f"{a}√(-{n}) = {a}√({n} · (-1))",
            f"= {a}√{n} · √(-1)",
            f"= {a}√{n} · i",
            f"= {a}i√{n}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ImaginaryUnitIGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
