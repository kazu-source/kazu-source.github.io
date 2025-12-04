"""
Equivalent Forms of Exponents Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EquivalentFormsExponentsGenerator:
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
                exp = random.randint(2, 6)
                latex = f"\\frac{{1}}{{{base}^{{{exp}}}}}"
                solution = f"{base}^{{-{exp}}}"
                steps = [f"Negative exponent rule", f"1/{base}^{exp} = {base}^{{-{exp}}}", f"Answer: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                base = random.choice(['x', 'y', 'z'])
                latex = f"\\sqrt{{{base}}}"
                solution = f"{base}^{{1/2}}"
                steps = [f"Square root as fractional exponent", f"\\sqrt{{{base}}} = {base}^{{1/2}}", f"Answer: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                base = random.choice(['a', 'b', 'x'])
                n = random.randint(3, 5)
                latex = f"\\sqrt[{n}]{{{base}^{{{n+1}}}}}"
                solution = f"{base} \\cdot {base}^{{1/{n}}}"
                steps = [f"Convert to fractional exponent", f"{base}^{{({n+1})/{n}}} = {base}^{{1 + 1/{n}}}", f"= {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                base = random.choice(['x', 'y'])
                m = random.randint(2, 4)
                n = random.randint(3, 5)
                latex = f"(\\sqrt[{n}]{{{base}}})^{{{m}}}"
                solution = f"{base}^{{{m}/{n}}}"
                steps = [f"Root as fractional exponent", f"(\\sqrt[{n}]{{{base}}})^{m} = ({base}^{{1/{n}}})^{m}", f"= {base}^{{{m}/{n}}}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = EquivalentFormsExponentsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
