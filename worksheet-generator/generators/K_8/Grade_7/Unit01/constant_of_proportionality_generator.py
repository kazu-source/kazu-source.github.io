"""
Constant Of Proportionality Generator - Grade 7 Unit 01
Generates problems for constant of proportionality (k) from tables and scenarios
"""

import random
from typing import List
from fractions import Fraction
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ConstantOfProportionalityGenerator:
    """Generates constant of proportionality (k) from tables and scenarios problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy problems: Simple tables with integer constants."""
        k = random.randint(2, 5)
        x_values = [1, 2, 3, 4]
        y_values = [k * x for x in x_values]
        
        table_str = " & ".join([f"{x}" for x in x_values])
        table_str2 = " & ".join([f"{y}" for y in y_values])
        
        latex = f"\text{{Find the constant of proportionality: }} \\\begin{{array}}{{|c|c|c|c|c|}}\hline x & {table_str} \\\hline y & {table_str2} \\\hline\end{{array}}"
        solution = str(k)
        steps = [f"k = \frac{{y}}{{x}} = \frac{{{y_values[0]}}}{{{x_values[0]}}} = {k}"]
        
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: Tables with fraction constants."""
        numerator = random.randint(1, 4)
        denominator = random.choice([2, 3, 4, 5])
        k = Fraction(numerator, denominator)
        
        x_values = [denominator * i for i in range(1, 5)]
        y_values = [int(k * x) for x in x_values]
        
        table_str = " & ".join([f"{x}" for x in x_values])
        table_str2 = " & ".join([f"{y}" for y in y_values]

)        
        latex = f"\text{{Find the constant of proportionality: }} \\\begin{{array}}{{|c|c|c|c|c|}}\hline x & {table_str} \\\hline y & {table_str2} \\\hline\end{{array}}"
        
        if k.denominator == 1:
            solution = str(k.numerator)
        else:
            solution = f"\frac{{{k.numerator}}}{{{k.denominator}}}"
        
        steps = [f"k = \frac{{y}}{{x}} = \frac{{{y_values[0]}}}{{{x_values[0]}}} = {solution}"]
        
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: Word problems."""
        k = random.randint(3, 12)
        x_val = random.randint(5, 15)
        y_val = k * x_val
        
        contexts = [
            f"A car travels {y_val} miles in {x_val} hours. Find the constant speed (miles per hour).",
            f"{x_val} books cost ${y_val}. Find the cost per book.",
            f"A recipe uses {y_val} cups of flour for {x_val} batches. Find cups per batch.",
        ]
        
        context = random.choice(contexts)
        latex = f"\text{{{context}}}"
        solution = str(k)
        steps = [f"k = \frac{{{y_val}}}{{{x_val}}} = {k}"]
        
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: Multiple steps or complex scenarios."""
        k = Fraction(random.randint(2, 5), random.randint(2, 4))
        x1 = random.randint(4, 8)
        y1 = float(k * x1)
        x2 = random.randint(10, 20)
        y2 = float(k * x2)
        
        latex = f"\text{{If }} y = {y1:.1f} \text{{ when }} x = {x1}, \text{{ find }} y \text{{ when }} x = {x2}."
        solution = f"{y2:.1f}"
        
        if k.denominator == 1:
            k_str = str(k.numerator)
        else:
            k_str = f"\frac{{{k.numerator}}}{{{k.denominator}}}"
        
        steps = [
            f"\text{{Find k: }} k = \frac{{y}}{{x}} = \frac{{{y1:.1f}}}{{{x1}}} = {k_str}",
            f"\text{{Use k to find y: }} y = {k_str} \times {x2} = {y2:.1f}"
        ]
        
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = ConstantOfProportionalityGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
