"""
Complex Plane Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ComplexPlaneGenerator:
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
        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
        latex = f"\\text{{Plot }} {a} + {b}i \\text{{ on the complex plane}}"
        solution = f"({a}, {b})"
        steps = [
            f"Real part: {a} (horizontal axis)",
            f"Imaginary part: {b} (vertical axis)",
            f"Point: ({a}, {b})"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(-6, 6)
        b = random.randint(-6, 6)
        import math
        modulus = math.sqrt(a**2 + b**2)
        latex = f"\\text{{Find the modulus of }} {a} + {b}i"
        solution = f"{modulus:.2f}"
        steps = [
            f"|a + bi| = √(a² + b²)",
            f"|{a} + {b}i| = √({a}² + {b}²)",
            f"= √({a**2} + {b**2})",
            f"= √{a**2 + b**2}",
            f"≈ {modulus:.2f}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
        latex = f"\\text{{Find the conjugate of }} {a} + {b}i"
        solution = f"{a} - {b}i"
        steps = [
            "Conjugate of a + bi is a - bi",
            f"Conjugate of {a} + {b}i",
            f"= {a} - {b}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        import math
        modulus = math.sqrt(a**2 + b**2)
        angle = math.atan2(b, a) * 180 / math.pi
        latex = f"\\text{{Convert to polar form: }} {a} + {b}i"
        solution = f"r = {modulus:.2f}, \\theta = {angle:.1f}°"
        steps = [
            f"r = √(a² + b²) = √({a}² + {b}²) = {modulus:.2f}",
            f"θ = arctan(b/a) = arctan({b}/{a}) ≈ {angle:.1f}°",
            f"Polar form: {modulus:.2f}(cos {angle:.1f}° + i sin {angle:.1f}°)"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ComplexPlaneGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
