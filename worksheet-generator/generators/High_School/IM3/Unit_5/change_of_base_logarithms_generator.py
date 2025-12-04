"""
Change of Base for Logarithms Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ChangeOfBaseLogarithmsGenerator:
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
        # Change to base 10
        base = random.choice([2, 3, 5, 7])
        value = random.randint(10, 50)

        latex = f"\\text{{Convert to base 10: }} \\log_{{{base}}} {value}"
        solution = f"\\frac{{\\log {value}}}{{\\log {base}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Change to natural log
        base = random.choice([2, 3, 5, 7])
        value = random.randint(10, 50)

        latex = f"\\text{{Convert to natural log: }} \\log_{{{base}}} {value}"
        solution = f"\\frac{{\\ln {value}}}{{\\ln {base}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Evaluate using change of base
        base = random.choice([2, 4, 8])
        exp = random.randint(2, 4)
        value = base ** exp

        latex = f"\\text{{Evaluate using change of base: }} \\log_{{{base}}} {value}"
        solution = f"{exp}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex change of base
        base1 = random.choice([2, 3, 5])
        base2 = random.choice([7, 11, 13])
        value = random.randint(20, 100)

        latex = f"\\text{{Express in terms of }} \\log_{{{base2}}}: \\log_{{{base1}}} {value}"
        solution = f"\\frac{{\\log_{{{base2}}} {value}}}{{\\log_{{{base2}}} {base1}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ChangeOfBaseLogarithmsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
