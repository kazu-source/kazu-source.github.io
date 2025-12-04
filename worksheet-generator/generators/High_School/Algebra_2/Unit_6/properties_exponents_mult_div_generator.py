"""
Properties of Exponents - Multiplication and Division Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PropertiesExponentsMultDivGenerator:
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
                base = random.choice(['x', 'y', 'a'])
                exp1 = random.randint(2, 6)
                exp2 = random.randint(2, 6)
                latex = f"{base}^{{{exp1}}} \\cdot {base}^{{{exp2}}}"
                solution = f"{base}^{{{exp1 + exp2}}}"
                steps = [f"When multiplying same base, add exponents", f"{base}^{exp1} \\cdot {base}^{exp2} = {base}^{{{exp1}+{exp2}}}", f"= {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                base = random.choice(['x', 'y', 'z'])
                exp1 = random.randint(5, 10)
                exp2 = random.randint(2, 5)
                latex = f"\\frac{{{base}^{{{exp1}}}}}{{{base}^{{{exp2}}}}}"
                solution = f"{base}^{{{exp1 - exp2}}}"
                steps = [f"When dividing same base, subtract exponents", f"{base}^{exp1} \\div {base}^{exp2} = {base}^{{{exp1}-{exp2}}}", f"= {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                base = random.choice(['a', 'b', 'x'])
                exp1 = random.randint(2, 5)
                exp2 = random.randint(2, 4)
                latex = f"({base}^{{{exp1}}})^{{{exp2}}}"
                solution = f"{base}^{{{exp1 * exp2}}}"
                steps = [f"Power of a power: multiply exponents", f"({base}^{exp1})^{exp2} = {base}^{{{exp1} \\cdot {exp2}}}", f"= {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                a = random.randint(2, 4)
                b = random.randint(2, 4)
                n = random.randint(3, 5)
                latex = f"({a}{b})^{{{n}}} = ?"
                solution = f"{a}^{{{n}}} \\cdot {b}^{{{n}}}"
                steps = [f"Distribute exponent to each factor", f"({a} \\cdot {b})^{n} = {a}^{n} \\cdot {b}^{n}", f"= {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PropertiesExponentsMultDivGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
