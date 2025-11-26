"""
Equations Word Problems Generator - Grade 8 Unit 3
Generates word problems that require setting up and solving equations
Example: Maria has $50 and saves $10 per week. How many weeks until she has $100?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EquationsWordProblemsGenerator:
    """Generates equations word problems."""

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
        """Generate easy problems: simple one-step or two-step equations."""
        contexts = [
            {
                "problem": "Maria saves $${rate} per week. After {weeks} weeks, she has $${total}. Write and solve an equation.",
                "equation": "{rate} \\cdot {weeks} = {total}",
                "var": "weeks"
            },
            {
                "problem": "A shirt costs $${price}. With a $${discount} discount, the final price is $${final}. Write and solve an equation.",
                "equation": "{price} - {discount} = {final}",
                "var": "discount"
            },
            {
                "problem": "John has {initial} marbles and gets {more} more. He now has {total} marbles. Write and solve an equation.",
                "equation": "{initial} + {more} = {total}",
                "var": "more"
            }
        ]

        context = random.choice(contexts)

        if "rate" in context["problem"]:
            weeks = random.randint(3, 8)
            rate = random.randint(5, 15)
            total = rate * weeks

            problem_text = context["problem"].format(rate=rate, weeks=weeks, total=total)
            latex = f"\\text{{{problem_text}}}"
            solution = f"{weeks} \\text{{ weeks}}"
            steps = [
                f"{rate}w = {total}",
                f"w = {weeks}"
            ]
        elif "discount" in context["problem"]:
            price = random.randint(20, 50)
            discount = random.randint(5, 15)
            final = price - discount

            problem_text = context["problem"].format(price=price, discount=discount, final=final)
            latex = f"\\text{{{problem_text}}}"
            solution = f"\\${discount}"
            steps = [
                f"{price} - d = {final}",
                f"d = {discount}"
            ]
        else:
            initial = random.randint(10, 30)
            more = random.randint(5, 15)
            total = initial + more

            problem_text = context["problem"].format(initial=initial, more=more, total=total)
            latex = f"\\text{{{problem_text}}}"
            solution = f"{more} \\text{{ marbles}}"
            steps = [
                f"{initial} + m = {total}",
                f"m = {more}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: two-step equations."""
        contexts = [
            "A phone plan costs $${base} per month plus $${rate} per GB. The total bill is $${total}. How many GB were used?",
            "A taxi charges $${base} plus $${rate} per mile. A {miles}-mile trip costs $${total}. Verify the equation.",
            "A gym membership costs $${base} to join and $${rate} per month. After {months} months, the total cost is $${total}."
        ]

        context = random.choice(contexts)

        if "GB" in context:
            base = random.randint(20, 40)
            rate = random.randint(3, 8)
            gb = random.randint(2, 8)
            total = base + rate * gb

            problem_text = context.format(base=base, rate=rate, total=total)
            latex = f"\\text{{{problem_text}}}"
            solution = f"{gb} \\text{{ GB}}"
            steps = [
                f"{base} + {rate}x = {total}",
                f"{rate}x = {total - base}",
                f"x = {gb}"
            ]
        elif "taxi" in context:
            base = random.randint(3, 7)
            rate = random.randint(2, 5)
            miles = random.randint(5, 15)
            total = base + rate * miles

            problem_text = context.format(base=base, rate=rate, miles=miles, total=total)
            latex = f"\\text{{{problem_text}}}"
            solution = f"\\text{{Equation: }} {base} + {rate} \\times {miles} = {total}"
            steps = [
                f"\\text{{Cost}} = {base} + {rate}x",
                f"{base} + {rate}({miles}) = {total}",
                f"\\text{{Verified}}"
            ]
        else:
            base = random.randint(30, 60)
            rate = random.randint(15, 30)
            months = random.randint(4, 12)
            total = base + rate * months

            problem_text = context.format(base=base, rate=rate, months=months, total=total)
            latex = f"\\text{{{problem_text}}}"
            solution = f"{months} \\text{{ months}}"
            steps = [
                f"{base} + {rate}x = {total}",
                f"{rate}x = {total - base}",
                f"x = {months}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: equations with variables on both sides or distributions."""
        contexts = [
            {
                "problem": "Store A sells phones for $${price_a}. Store B sells them for $${price_b} plus $${rate_b} per accessory. For how many accessories is the total cost equal?",
                "var": "accessories"
            },
            {
                "problem": "Two trains start {distance} km apart and travel toward each other. One goes {speed1} km/h, the other {speed2} km/h. When do they meet?",
                "var": "time"
            }
        ]

        context = random.choice(contexts)

        if "Store" in context["problem"]:
            accessories = random.randint(2, 8)
            rate_b = random.randint(10, 30)
            price_b = random.randint(100, 200)
            price_a = price_b + rate_b * accessories

            problem_text = context["problem"].format(price_a=price_a, price_b=price_b, rate_b=rate_b)
            latex = f"\\text{{{problem_text}}}"
            solution = f"{accessories} \\text{{ accessories}}"
            steps = [
                f"{price_a} = {price_b} + {rate_b}x",
                f"{price_a - price_b} = {rate_b}x",
                f"x = {accessories}"
            ]
        else:
            speed1 = random.randint(40, 70)
            speed2 = random.randint(50, 80)
            time = random.randint(2, 5)
            distance = (speed1 + speed2) * time

            problem_text = context["problem"].format(distance=distance, speed1=speed1, speed2=speed2)
            latex = f"\\text{{{problem_text}}}"
            solution = f"{time} \\text{{ hours}}"
            steps = [
                f"{speed1}t + {speed2}t = {distance}",
                f"{speed1 + speed2}t = {distance}",
                f"t = {time}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex multi-step word problems."""
        contexts = [
            "A rectangle's length is {factor} times its width. The perimeter is {perimeter} cm. Find the dimensions.",
            "The sum of three consecutive integers is {sum}. Find the integers.",
            "A number is increased by {percent}%. The result is {result}. Find the original number."
        ]

        context = random.choice(contexts)

        if "rectangle" in context:
            width = random.randint(5, 15)
            factor = random.randint(2, 4)
            length = factor * width
            perimeter = 2 * (length + width)

            problem_text = context.format(factor=factor, perimeter=perimeter)
            latex = f"\\text{{{problem_text}}}"
            solution = f"\\text{{Width: }} {width}\\text{{ cm, Length: }} {length}\\text{{ cm}}"
            steps = [
                f"2(w + {factor}w) = {perimeter}",
                f"2({factor + 1}w) = {perimeter}",
                f"{2 * (factor + 1)}w = {perimeter}",
                f"w = {width}, l = {length}"
            ]
        elif "consecutive" in context:
            first = random.randint(10, 30)
            sum_val = first + (first + 1) + (first + 2)

            problem_text = context.format(sum=sum_val)
            latex = f"\\text{{{problem_text}}}"
            solution = f"{first}, {first + 1}, {first + 2}"
            steps = [
                f"n + (n+1) + (n+2) = {sum_val}",
                f"3n + 3 = {sum_val}",
                f"3n = {sum_val - 3}",
                f"n = {first}"
            ]
        else:
            original = random.randint(40, 100)
            percent = random.choice([20, 25, 50])
            result = original + (original * percent // 100)

            problem_text = context.format(percent=percent, result=result)
            latex = f"\\text{{{problem_text}}}"
            solution = f"{original}"
            steps = [
                f"x + \\frac{{{percent}}}{{100}}x = {result}",
                f"\\frac{{{100 + percent}}}{{100}}x = {result}",
                f"x = {original}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = EquationsWordProblemsGenerator()

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
