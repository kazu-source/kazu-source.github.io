"""
Modeling Two Variable Inequalities Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ModelingTwoVariableInequalitiesGenerator:
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
        max_hours = random.randint(8, 15)

        latex = f"\\text{{You can work at most {max_hours} hours per week. Write inequality.}}"
        solution = f"h \\leq {max_hours}"
        steps = [f"h = hours worked", f"At most means ≤", f"h \\leq {max_hours}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        price_a = random.randint(5, 12)
        price_b = random.randint(3, 8)
        budget = random.randint(50, 100)

        latex = f"\\text{{Items cost \\${price_a} and \\${price_b}. Budget \\${budget}. Write inequality.}}"
        solution = f"{price_a}x + {price_b}y \\leq {budget}"
        steps = [f"Cost: {price_a}x + {price_b}y", f"Must be within budget", f"{price_a}x + {price_b}y \\leq {budget}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        calories_a = random.randint(150, 300)
        calories_b = random.randint(100, 250)
        max_cal = random.randint(800, 1500)
        min_servings = random.randint(3, 6)

        latex = f"\\text{{Food A: {calories_a} cal, Food B: {calories_b} cal. Max {max_cal} cal, min {min_servings} servings. Write system.}}"
        solution = f"{calories_a}a + {calories_b}b \\leq {max_cal}, a + b \\geq {min_servings}"
        steps = [f"Calories: {calories_a}a + {calories_b}b \\leq {max_cal}", f"Servings: a + b \\geq {min_servings}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        adult_tickets = random.randint(10, 20)
        child_tickets = random.randint(5, 10)
        min_revenue = random.randint(200, 400)
        max_capacity = random.randint(50, 80)

        latex = f"\\text{{Tickets: \\${adult_tickets} adult, \\${child_tickets} child. Need \\${min_revenue}, max {max_capacity} people. Write system.}}"
        solution = f"{adult_tickets}a + {child_tickets}c \\geq {min_revenue}, a + c \\leq {max_capacity}"
        steps = [f"Revenue: {adult_tickets}a + {child_tickets}c \\geq {min_revenue}", f"Capacity: a + c \\leq {max_capacity}", "Also: a ≥ 0, c ≥ 0"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ModelingTwoVariableInequalitiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
