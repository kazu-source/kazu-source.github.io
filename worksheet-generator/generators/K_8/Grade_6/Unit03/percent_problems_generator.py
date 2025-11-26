"""
Percent Problems Generator - Grade 6 Unit 3
Generates basic percent calculation problems
Example: What is 30% of 80?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PercentProblemsGenerator:
    """Generates percent problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
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
        """Generate easy problems: simple percents of nice numbers."""
        percents = [10, 20, 25, 50, 75]
        numbers = [20, 40, 60, 80, 100]

        percent = random.choice(percents)
        number = random.choice(numbers)
        result = (percent * number) / 100

        latex = f"\\text{{What is {percent}\\% of {number}?}}"
        solution = str(int(result)) if result.is_integer() else str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{percent}\\% \\times {number} = \\frac{{{percent}}}{{100}} \\times {number} = {solution}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: various percents."""
        percent = random.choice([15, 30, 35, 40, 60, 65, 70, 80, 85, 90])
        number = random.choice([50, 60, 80, 100, 120, 150, 200])
        result = (percent * number) / 100

        latex = f"\\text{{Find {percent}\\% of {number}.}}"
        solution = str(int(result)) if result.is_integer() else str(result)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\frac{{{percent}}}{{100}} \\times {number} = {result}",
                f"\\text{{Answer: }} {solution}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: finding the percent or the whole."""
        if random.choice([True, False]):
            # Find the percent
            part = random.randint(10, 50)
            whole = random.choice([50, 100, 200, 250])
            while part >= whole:
                part = random.randint(10, 50)
            percent = (part * 100) / whole

            latex = f"\\text{{{part} is what percent of {whole}?}}"
            solution = f"{percent:.0f}\\%" if percent.is_integer() else f"{percent}\\%"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\frac{{{part}}}{{{whole}}} = \\frac{{x}}{{100}}",
                    f"x = \\frac{{{part} \\times 100}}{{{whole}}} = {percent:.0f}" if percent.is_integer() else f"x = {percent}",
                    f"\\text{{Answer: }} {solution}"
                ],
                difficulty='hard'
            )
        else:
            # Find the whole
            percent = random.choice([20, 25, 40, 50, 80])
            part = random.randint(10, 80)
            whole = (part * 100) / percent

            latex = f"\\text{{{part} is {percent}\\% of what number?}}"
            solution = str(int(whole)) if whole.is_integer() else str(whole)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"{percent}\\% \\times x = {part}",
                    f"x = {part} \\div \\frac{{{percent}}}{{100}} = {part} \\times \\frac{{100}}{{{percent}}} = {solution}"
                ],
                difficulty='hard'
            )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: percent increase/decrease."""
        original = random.randint(50, 200)
        percent_change = random.choice([10, 20, 25, 30, 40, 50])

        if random.choice([True, False]):
            # Increase
            change = (percent_change * original) / 100
            new_value = original + change

            latex = f"\\text{{A number is increased by {percent_change}\\%. If the original number is {original}, what is the new number?}}"
            solution = str(int(new_value)) if new_value.is_integer() else str(new_value)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Increase}} = {percent_change}\\% \\times {original} = {change}",
                    f"\\text{{New value}} = {original} + {change} = {solution}"
                ],
                difficulty='challenge'
            )
        else:
            # Decrease
            change = (percent_change * original) / 100
            new_value = original - change

            latex = f"\\text{{A number is decreased by {percent_change}\\%. If the original number is {original}, what is the new number?}}"
            solution = str(int(new_value)) if new_value.is_integer() else str(new_value)

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Decrease}} = {percent_change}\\% \\times {original} = {change}",
                    f"\\text{{New value}} = {original} - {change} = {solution}"
                ],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = PercentProblemsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
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
