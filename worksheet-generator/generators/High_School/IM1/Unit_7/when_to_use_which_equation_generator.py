"""
When to Use Which Equation Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WhenToUseWhichEquationGenerator:
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
        m = random.randint(2, 7)
        b = random.randint(5, 20)

        latex = f"\\text{{You know slope is {m} and y-intercept is {b}. Which form to use?}}"
        solution = "Slope-intercept form (y = mx + b)"
        steps = ["Have m and b directly", "Use y = mx + b", "Answer: Slope-intercept form"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 6)
        x1 = random.randint(1, 5)
        y1 = random.randint(3, 10)

        latex = f"\\text{{You know slope {m} and point ({x1}, {y1}). Which form to use?}}"
        solution = "Point-slope form (y - y₁ = m(x - x₁))"
        steps = ["Have slope and one point", "Use y - y₁ = m(x - x₁)", "Answer: Point-slope form"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        price_a = random.randint(4, 10)
        price_b = random.randint(3, 8)
        total = random.randint(40, 80)

        latex = f"\\text{{Item A costs \\${price_a}, item B costs \\${price_b}, total \\${total}. Which form?}}"
        solution = "Standard form (Ax + By = C)"
        steps = ["Two variables with constraints", "Use Ax + By = C", f"{price_a}a + {price_b}b = {total}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        scenarios = [
            ("Given two points (2,5) and (4,9)", "Find slope first, then use point-slope form"),
            ("Given y-intercept 3 and slope 4", "Use slope-intercept: y = 4x + 3"),
            ("Budget problem: x items at $5, y items at $3, total $60", "Use standard form: 5x + 3y = 60"),
            ("Temperature at hour 3 is 72°, rising 5° per hour", "Use point-slope: T - 72 = 5(h - 3)")
        ]

        scenario, answer = random.choice(scenarios)

        latex = f"\\text{{{scenario}. Which form is best?}}"
        solution = answer
        steps = ["Identify what information is given", "Choose appropriate form", f"Answer: {answer}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WhenToUseWhichEquationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
