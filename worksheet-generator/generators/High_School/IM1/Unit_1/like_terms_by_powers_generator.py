"""
Like Terms by Powers Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LikeTermsByPowersGenerator:
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
        var = random.choice(['x', 'y', 'n'])

        latex = f"\\text{{Are }} {a}{var}^2 \\text{{ and }} {b}{var}^2 \\text{{ like terms?}}"
        solution = "Yes"
        steps = [f"Both terms have {var}^2", "Same variable and same power", "Answer: Yes, they are like terms"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 7)
        b = random.randint(1, 8)
        var = random.choice(['x', 'y', 'm'])

        latex = f"\\text{{Are }} {a}{var}^2 \\text{{ and }} {b}{var} \\text{{ like terms?}}"
        solution = "No"
        steps = [f"First term has {var}^2", f"Second term has {var}^1", "Different powers - not like terms", "Answer: No"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 7)
        b = random.randint(1, 8)
        c = random.randint(1, 6)

        latex = f"\\text{{Simplify: }} {a}x^2 + {b}x + {c}x^2"
        x2_coef = a + c
        solution = f"{x2_coef}x^2 + {b}x"
        steps = [f"Combine x^2 terms: {a}x^2 + {c}x^2 = {x2_coef}x^2", f"x term stays: {b}x", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 7)
        c = random.randint(1, 5)
        d = random.randint(1, 6)
        e = random.randint(1, 8)

        x2_coef = a + c
        x1_coef = b + d

        latex = f"\\text{{Simplify: }} {a}x^2 + {b}x + {c}x^2 + {d}x + {e}"
        solution = f"{x2_coef}x^2 + {x1_coef}x + {e}"
        steps = [f"Combine x^2: {a}x^2 + {c}x^2 = {x2_coef}x^2", f"Combine x: {b}x + {d}x = {x1_coef}x", f"Constant: {e}", f"Answer: {solution}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = LikeTermsByPowersGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
