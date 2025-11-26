"""
Adding with Regrouping Within 1000 Generator - Grade 3 Unit 3
Generates addition problems with regrouping (carrying) for numbers up to 999
Shows step-by-step regrouping process
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AddingWithRegroupingWithin1000Generator:
    """Generates addition with regrouping problems within 1000."""

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

    def _requires_regrouping_ones(self, num1: int, num2: int) -> bool:
        """Check if ones place requires regrouping."""
        return (num1 % 10) + (num2 % 10) >= 10

    def _requires_regrouping_tens(self, num1: int, num2: int) -> bool:
        """Check if tens place requires regrouping."""
        return ((num1 // 10) % 10) + ((num2 // 10) % 10) >= 10

    def _get_addition_steps(self, num1: int, num2: int) -> List[str]:
        """Generate detailed steps for addition with regrouping."""
        steps = []
        result = num1 + num2

        ones1 = num1 % 10
        ones2 = num2 % 10
        tens1 = (num1 // 10) % 10
        tens2 = (num2 // 10) % 10
        hundreds1 = num1 // 100
        hundreds2 = num2 // 100

        # Ones place
        ones_sum = ones1 + ones2
        if ones_sum >= 10:
            steps.append(f"\\text{{Ones: }} {ones1} + {ones2} = {ones_sum} \\text{{ (regroup 1 ten)}}")
            carry_to_tens = 1
        else:
            steps.append(f"\\text{{Ones: }} {ones1} + {ones2} = {ones_sum}")
            carry_to_tens = 0

        # Tens place
        tens_sum = tens1 + tens2 + carry_to_tens
        if tens_sum >= 10:
            steps.append(f"\\text{{Tens: }} {tens1} + {tens2} + {carry_to_tens} = {tens_sum} \\text{{ (regroup 1 hundred)}}")
            carry_to_hundreds = 1
        else:
            if carry_to_tens > 0:
                steps.append(f"\\text{{Tens: }} {tens1} + {tens2} + {carry_to_tens} = {tens_sum}")
            else:
                steps.append(f"\\text{{Tens: }} {tens1} + {tens2} = {tens_sum}")
            carry_to_hundreds = 0

        # Hundreds place
        if hundreds1 > 0 or hundreds2 > 0 or carry_to_hundreds > 0:
            hundreds_sum = hundreds1 + hundreds2 + carry_to_hundreds
            if carry_to_hundreds > 0:
                steps.append(f"\\text{{Hundreds: }} {hundreds1} + {hundreds2} + {carry_to_hundreds} = {hundreds_sum}")
            else:
                steps.append(f"\\text{{Hundreds: }} {hundreds1} + {hundreds2} = {hundreds_sum}")

        steps.append(f"\\text{{Answer: }} {result}")
        return steps

    def _generate_easy(self) -> Equation:
        """Generate easy problems: 2-digit + 2-digit with regrouping in ones only."""
        # Ensure regrouping in ones place only
        while True:
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            if self._requires_regrouping_ones(num1, num2) and not self._requires_regrouping_tens(num1, num2):
                break

        result = num1 + num2
        latex = f"{num1} + {num2}"
        solution = str(result)
        steps = self._get_addition_steps(num1, num2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 3-digit + 2-digit or 3-digit with regrouping."""
        # Mix of problems with different regrouping scenarios
        choice = random.randint(1, 3)

        if choice == 1:
            # 3-digit + 2-digit
            num1 = random.randint(100, 899)
            num2 = random.randint(20, 99)
        elif choice == 2:
            # 3-digit + 3-digit with one regrouping
            while True:
                num1 = random.randint(100, 899)
                num2 = random.randint(100, 899)
                if (self._requires_regrouping_ones(num1, num2) or
                    self._requires_regrouping_tens(num1, num2)) and num1 + num2 < 1000:
                    break
        else:
            # 2-digit + 2-digit with regrouping in tens
            while True:
                num1 = random.randint(50, 99)
                num2 = random.randint(50, 99)
                if self._requires_regrouping_tens(num1, num2):
                    break

        result = num1 + num2
        latex = f"{num1} + {num2}"
        solution = str(result)
        steps = self._get_addition_steps(num1, num2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 3-digit + 3-digit with multiple regroupings."""
        # Ensure at least two regroupings
        while True:
            num1 = random.randint(150, 899)
            num2 = random.randint(150, 899)
            regroups = sum([
                self._requires_regrouping_ones(num1, num2),
                self._requires_regrouping_tens(num1, num2)
            ])
            if regroups >= 2 and num1 + num2 < 1000:
                break

        result = num1 + num2
        latex = f"{num1} + {num2}"
        solution = str(result)
        steps = self._get_addition_steps(num1, num2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: word problems with regrouping."""
        num1 = random.randint(125, 675)
        num2 = random.randint(125, 300)

        # Ensure regrouping is needed
        while not (self._requires_regrouping_ones(num1, num2) or
                   self._requires_regrouping_tens(num1, num2)):
            num1 = random.randint(125, 675)
            num2 = random.randint(125, 300)

        contexts = [
            f"A store had {num1} books. They received {num2} more books",
            f"There are {num1} red marbles and {num2} blue marbles in a bag",
            f"A school has {num1} students in the lower grades and {num2} students in the upper grades",
            f"A farmer grew {num1} tomatoes and {num2} cucumbers",
            f"A library has {num1} fiction books and {num2} non-fiction books"
        ]

        context = random.choice(contexts)
        result = num1 + num2

        latex = f"\\text{{{context}. How many in total?}}"
        solution = str(result)
        steps = [f"{num1} + {num2}"] + self._get_addition_steps(num1, num2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = AddingWithRegroupingWithin1000Generator()

    print("Easy (2-digit + 2-digit, regrouping in ones):")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
        print(f"  Steps: {problem.steps[0]}")
        print()

    print("\nMedium (Mixed regrouping scenarios):")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")
        print()

    print("\nHard (Multiple regroupings):")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex} = {problem.solution}")
        for step in problem.steps:
            print(f"    {step}")
        print()

    print("\nChallenge (Word problems with regrouping):")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print()


if __name__ == '__main__':
    main()
