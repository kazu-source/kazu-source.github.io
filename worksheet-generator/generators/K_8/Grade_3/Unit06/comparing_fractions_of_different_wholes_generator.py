"""
Comparing Fractions of Different Wholes Generator - Grade 3 Unit 6
Generates problems understanding that fractions need the same whole to compare
Example: 1/2 of a large pizza vs 1/2 of a small pizza
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingFractionsOfDifferentWholesGenerator:
    """Generates problems about comparing fractions with different wholes."""

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
        """Generate easy problems: simple recognition that wholes must be same."""
        fraction = random.choice(["\\frac{1}{2}", "\\frac{1}{4}", "\\frac{1}{3}"])

        contexts = [
            f"Can we compare {fraction} of a large pizza to {fraction} of a small pizza directly?",
            f"Is {fraction} of a big cake the same amount as {fraction} of a small cake?",
            f"Does {fraction} of a large apple equal {fraction} of a small apple?",
            f"Can we say {fraction} of 8 cookies equals {fraction} of 4 cookies?"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"
        solution = "No, the wholes are different"

        return Equation(
            latex=latex,
            solution=solution,
            steps=["\\text{{Fractions must have the same whole to be compared directly}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: identifying which situations can be compared."""
        fraction = random.choice(["\\frac{1}{2}", "\\frac{1}{4}", "\\frac{2}{3}", "\\frac{3}{4}"])

        # Mix of same whole and different whole scenarios
        scenarios = [
            {
                "text": f"Compare {fraction} of a 12-inch pizza to {fraction} of another 12-inch pizza",
                "can_compare": True,
                "reason": "same whole (both 12-inch pizzas)"
            },
            {
                "text": f"Compare {fraction} of a large watermelon to {fraction} of a small watermelon",
                "can_compare": False,
                "reason": "different wholes (different sized watermelons)"
            },
            {
                "text": f"Compare {fraction} of 10 apples to {fraction} of 10 apples",
                "can_compare": True,
                "reason": "same whole (both are 10 apples)"
            },
            {
                "text": f"Compare {fraction} of 8 cookies to {fraction} of 12 cookies",
                "can_compare": False,
                "reason": "different wholes (8 vs 12 cookies)"
            }
        ]

        scenario = random.choice(scenarios)
        latex = f"\\text{{{scenario['text']}. Can these be compared directly?}}"

        if scenario['can_compare']:
            solution = f"Yes, {scenario['reason']}"
        else:
            solution = f"No, {scenario['reason']}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{scenario['reason']}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: actual comparison with same wholes."""
        denominator = random.choice([2, 3, 4])
        num1 = random.randint(1, denominator - 1)
        num2 = random.randint(1, denominator - 1)

        while num1 == num2:
            num2 = random.randint(1, denominator - 1)

        total = random.choice([8, 10, 12, 16, 20])

        contexts = [
            f"Sarah has \\frac{{{num1}}}{{{denominator}}} of {total} marbles. Tom has \\frac{{{num2}}}{{{denominator}}} of {total} marbles. Who has more marbles?",
            f"One box has \\frac{{{num1}}}{{{denominator}}} of {total} cookies eaten. Another has \\frac{{{num2}}}{{{denominator}}} of {total} cookies eaten. Which box has more cookies eaten?",
            f"Class A completed \\frac{{{num1}}}{{{denominator}}} of {total} pages. Class B completed \\frac{{{num2}}}{{{denominator}}} of {total} pages. Which class completed more?",
            f"Garden A planted \\frac{{{num1}}}{{{denominator}}} of {total} rows. Garden B planted \\frac{{{num2}}}{{{denominator}}} of {total} rows. Which garden planted more rows?"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}}}"

        if num1 > num2:
            if "Sarah" in context:
                answer = "Sarah"
            elif "One box" in context:
                answer = "First box"
            elif "Class A" in context:
                answer = "Class A"
            else:
                answer = "Garden A"
        else:
            if "Sarah" in context:
                answer = "Tom"
            elif "One box" in context:
                answer = "Second box"
            elif "Class A" in context:
                answer = "Class B"
            else:
                answer = "Garden B"

        solution = answer
        steps = [f"\\text{{Same whole ({total}), so compare: }} \\frac{{{num1}}}{{{denominator}}} \\text{{ vs }} \\frac{{{num2}}}{{{denominator}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: explain why comparison works or doesn't work."""
        scenario_type = random.choice(['works', 'doesnt_work'])

        if scenario_type == 'works':
            total = random.choice([12, 16, 20, 24])
            denominator = random.choice([2, 3, 4])
            num1 = random.randint(1, denominator - 1)
            num2 = random.randint(1, denominator - 1)
            while num1 == num2:
                num2 = random.randint(1, denominator - 1)

            contexts = [
                f"Two identical boxes each contain {total} pencils. Box A has \\frac{{{num1}}}{{{denominator}}} of its pencils sharpened. Box B has \\frac{{{num2}}}{{{denominator}}} sharpened. Can we compare these fractions? Explain.",
                f"Two equal-sized gardens each have {total} plants. Garden A has \\frac{{{num1}}}{{{denominator}}} blooming. Garden B has \\frac{{{num2}}}{{{denominator}}} blooming. Can we compare these fractions? Explain.",
                f"Two friends each have {total} cards. Friend A used \\frac{{{num1}}}{{{denominator}}} of their cards. Friend B used \\frac{{{num2}}}{{{denominator}}} of their cards. Can we compare these fractions? Explain."
            ]

            context = random.choice(contexts)
            solution = f"Yes, same wholes ({total} each)"
        else:
            total1 = random.choice([12, 16, 20])
            total2 = random.choice([8, 10, 15])
            while total1 == total2:
                total2 = random.choice([8, 10, 15])

            denominator = random.choice([2, 3, 4])
            numerator = random.randint(1, denominator - 1)

            contexts = [
                f"Box A has {total1} pencils with \\frac{{{numerator}}}{{{denominator}}} sharpened. Box B has {total2} pencils with \\frac{{{numerator}}}{{{denominator}}} sharpened. Can we compare these fractions directly? Explain.",
                f"Garden A has {total1} plants with \\frac{{{numerator}}}{{{denominator}}} blooming. Garden B has {total2} plants with \\frac{{{numerator}}}{{{denominator}}} blooming. Can we compare these fractions directly? Explain.",
                f"Friend A has {total1} cards and used \\frac{{{numerator}}}{{{denominator}}}. Friend B has {total2} cards and used \\frac{{{numerator}}}{{{denominator}}}. Can we compare these fractions directly? Explain."
            ]

            context = random.choice(contexts)
            solution = f"No, different wholes ({total1} vs {total2})"

        latex = f"\\text{{{context}}}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=["\\text{{Fractions need the same whole to compare directly}}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ComparingFractionsOfDifferentWholesGenerator()

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
