"""
Percent Word Problems Generator - Grade 6 Unit 3
Generates word problems involving percents
Example: A store has a 25% off sale. If a shirt costs $40, what is the sale price?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PercentWordProblemsGenerator:
    """Generates percent word problems."""

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
        """Generate easy problems: finding percent of a quantity."""
        contexts = [
            ("students in a class", "are girls"),
            ("books in a library", "are fiction"),
            ("cars in a lot", "are red"),
            ("flowers in a garden", "are roses")
        ]

        item, description = random.choice(contexts)
        total = random.choice([20, 25, 40, 50, 100])
        percent = random.choice([20, 25, 40, 50, 60, 75, 80])
        result = (percent * total) / 100

        latex = f"\\text{{There are {total} {item}. If {percent}\\% {description}, how many {description}?}}"
        solution = f"{int(result)}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"{percent}\\% \\times {total} = \\frac{{{percent}}}{{100}} \\times {total} = {int(result)}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: discount and tax problems."""
        if random.choice([True, False]):
            # Discount problem
            original_price = random.choice([20, 40, 60, 80, 100, 120, 150])
            discount_percent = random.choice([10, 15, 20, 25, 30])
            discount = (discount_percent * original_price) / 100
            sale_price = original_price - discount

            latex = f"\\text{{A store offers a {discount_percent}\\% discount on a \\${original_price} item. What is the sale price?}}"
            solution = f"\\${sale_price:.2f}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Discount}} = {discount_percent}\\% \\times \\${original_price} = \\${discount:.2f}",
                    f"\\text{{Sale price}} = \\${original_price} - \\${discount:.2f} = \\${sale_price:.2f}"
                ],
                difficulty='medium'
            )
        else:
            # Tax problem
            price = random.choice([25, 50, 75, 100, 125, 150])
            tax_rate = random.choice([5, 6, 7, 8, 10])
            tax = (tax_rate * price) / 100
            total = price + tax

            latex = f"\\text{{An item costs \\${price}. With {tax_rate}\\% sales tax, what is the total cost?}}"
            solution = f"\\${total:.2f}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Tax}} = {tax_rate}\\% \\times \\${price} = \\${tax:.2f}",
                    f"\\text{{Total}} = \\${price} + \\${tax:.2f} = \\${total:.2f}"
                ],
                difficulty='medium'
            )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: finding original price or percent."""
        if random.choice([True, False]):
            # Find original price
            discount_percent = random.choice([20, 25, 30, 40])
            sale_price = random.choice([30, 40, 60, 75, 90])
            original_price = sale_price / (1 - discount_percent/100)

            latex = f"\\text{{After a {discount_percent}\\% discount, an item costs \\${sale_price}. What was the original price?}}"
            solution = f"\\${original_price:.2f}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Sale price}} = \\text{{Original}} \\times (1 - {discount_percent/100})",
                    f"\\${sale_price} = \\text{{Original}} \\times {1 - discount_percent/100}",
                    f"\\text{{Original}} = \\${sale_price} \\div {1 - discount_percent/100} = \\${original_price:.2f}"
                ],
                difficulty='hard'
            )
        else:
            # Find the percent
            original = random.choice([50, 80, 100, 120, 150])
            part = random.randint(int(original * 0.2), int(original * 0.8))
            percent = (part * 100) / original

            latex = f"\\text{{In a class of {original} students, {part} passed a test. What percent passed?}}"
            solution = f"{percent:.0f}\\%" if percent.is_integer() else f"{percent:.1f}\\%"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Percent}} = \\frac{{{part}}}{{{original}}} \\times 100 = {percent:.1f}\\%"
                ],
                difficulty='hard'
            )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: successive percent changes."""
        original = random.choice([100, 150, 200, 250])
        increase_percent = random.choice([10, 20, 25, 30])
        decrease_percent = random.choice([10, 15, 20, 25])

        after_increase = original * (1 + increase_percent/100)
        final = after_increase * (1 - decrease_percent/100)

        latex = f"\\text{{A price of \\${original} increases by {increase_percent}\\%, then decreases by {decrease_percent}\\%. What is the final price?}}"
        solution = f"\\${final:.2f}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{After increase}} = \\${original} \\times {1 + increase_percent/100} = \\${after_increase:.2f}",
                f"\\text{{After decrease}} = \\${after_increase:.2f} \\times {1 - decrease_percent/100} = \\${final:.2f}"
            ],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = PercentWordProblemsGenerator()

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
