"""
Proofs with Irrational Numbers Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ProofsIrrationalNumbersGenerator:
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
        latex = "\\text{{Prove that }} \\sqrt{2} \\text{{ is irrational (outline the proof method)}}"
        solution = "Use proof by contradiction"
        steps = [
            "Assume √2 = p/q in lowest terms",
            "Then 2 = p²/q², so 2q² = p²",
            "This means p² is even, so p is even",
            "Let p = 2k, then 2q² = 4k², so q² = 2k²",
            "This means q is also even",
            "Contradiction: p and q both even, not in lowest terms",
            "Therefore √2 is irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        n = random.choice([3, 5, 6, 7])
        latex = f"\\text{{Prove that }} \\sqrt{{{n}}} \\text{{ is irrational}}"
        solution = f"√{n} is irrational (proof by contradiction)"
        steps = [
            f"Assume √{n} = p/q in lowest terms",
            f"Then {n} = p²/q², so {n}q² = p²",
            f"This means p² is divisible by {n}",
            f"Therefore p is divisible by {n}",
            f"Substituting shows q is also divisible by {n}",
            "Contradiction: not in lowest terms",
            f"Therefore √{n} is irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        latex = f"\\text{{Prove that }} {a} + \\sqrt{{2}} \\text{{ is irrational}}"
        solution = f"{a} + √2 is irrational"
        steps = [
            f"Assume {a} + √2 = r (rational)",
            f"Then √2 = r - {a}",
            "r and {a} are both rational",
            "Difference of rationals is rational",
            "But √2 is irrational - contradiction!",
            f"Therefore {a} + √2 is irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{{Prove that the sum of a rational and an irrational number is irrational}}"
        solution = "Proof by contradiction"
        steps = [
            "Let r be rational and i be irrational",
            "Assume r + i = q (rational)",
            "Then i = q - r",
            "q and r are both rational",
            "Difference of rationals is rational",
            "But i is irrational - contradiction!",
            "Therefore r + i must be irrational"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ProofsIrrationalNumbersGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
