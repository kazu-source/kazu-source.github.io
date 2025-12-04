"""
Word Problems Point Slope Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class WordProblemsPointSlopeGenerator:
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
        temp0 = random.randint(50, 80)
        rate = random.randint(2, 8)
        hours = random.randint(2, 5)

        latex = f"\\text{{Temperature is {temp0}°F at hour {hours}, rising {rate}°/hr. Write point-slope equation.}}"
        solution = f"T - {temp0} = {rate}(h - {hours})"
        steps = [f"Point: ({hours}, {temp0})", f"Slope: {rate}", f"T - {temp0} = {rate}(h - {hours})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        pop0 = random.randint(5000, 15000)
        year0 = random.randint(2010, 2020)
        rate = random.randint(200, 800)

        latex = f"\\text{{City population was {pop0} in {year0}, growing {rate}/year. Write equation.}}"
        solution = f"P - {pop0} = {rate}(t - {year0})"
        steps = [f"Point: ({year0}, {pop0})", f"Slope: {rate}", f"P - {pop0} = {rate}(t - {year0})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        cost1 = random.randint(100, 200)
        items1 = random.randint(10, 30)
        cost2 = cost1 + random.randint(50, 150)
        items2 = items1 + random.randint(10, 25)
        slope = (cost2 - cost1) / (items2 - items1)

        latex = f"\\text{{Cost is \\${cost1} for {items1} items, \\${cost2} for {items2} items. Write point-slope form.}}"
        solution = f"C - {cost1} = {slope:.1f}(n - {items1})"
        steps = [f"Slope: ({cost2}-{cost1})/({items2}-{items1}) = {slope:.1f}", f"Use point ({items1}, {cost1})", f"C - {cost1} = {slope:.1f}(n - {items1})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        depth1 = random.randint(500, 1000)
        time1 = random.randint(10, 30)
        rate = random.randint(-20, -5)
        time2 = random.randint(40, 60)
        depth2 = depth1 + rate * (time2 - time1)

        latex = f"\\text{{Submarine at {depth1}m at t={time1}min, descending {abs(rate)}m/min. Depth at t={time2}?}}"
        solution = f"{depth2} \\text{{ meters}}"
        steps = [f"Equation: d - {depth1} = {rate}(t - {time1})", f"Substitute t = {time2}", f"d - {depth1} = {rate}({time2 - time1})", f"d = {depth2}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = WordProblemsPointSlopeGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
