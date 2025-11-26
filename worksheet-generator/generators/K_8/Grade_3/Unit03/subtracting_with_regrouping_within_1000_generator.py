"""
Subtracting with Regrouping Within 1000 Generator - Grade 3 Unit 3
Generates subtraction problems with regrouping (borrowing) for numbers up to 999
Shows step-by-step regrouping process
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SubtractingWithRegroupingWithin1000Generator:
    """Generates subtraction with regrouping problems within 1000."""

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
        return (num1 % 10) < (num2 % 10)

    def _requires_regrouping_tens(self, num1: int, num2: int) -> bool:
        """Check if tens place requires regrouping."""
        return ((num1 // 10) % 10) < ((num2 // 10) % 10)

    def _requires_regrouping_hundreds(self, num1: int, num2: int) -> bool:
        """Check if hundreds place requires regrouping."""
        return (num1 // 100) < (num2 // 100)

    def _get_subtraction_steps(self, num1: int, num2: int) -> List[str]:
        """Generate detailed steps for subtraction with regrouping."""
        steps = []
        result = num1 - num2

        # Break down numbers into place values
        ones1 = num1 % 10
        ones2 = num2 % 10
        tens1 = (num1 // 10) % 10
        tens2 = (num2 // 10) % 10
        hundreds1 = num1 // 100
        hundreds2 = num2 // 100

        # Ones place
        if ones1 < ones2:
            steps.append(f"\\text{{Ones: Can't subtract }} {ones2} \\text{{ from }} {ones1} \\text{{, regroup from tens}}")
            ones1 += 10
            tens1 -= 1
            steps.append(f"\\text{{Ones: }} {ones1} - {ones2} = {ones1 - ones2}")
        else:
            steps.append(f"\\text{{Ones: }} {ones1} - {ones2} = {ones1 - ones2}")

        # Tens place
        if tens1 < tens2:
            steps.append(f"\\text{{Tens: Can't subtract }} {tens2} \\text{{ from }} {tens1} \\text{{, regroup from hundreds}}")
            tens1 += 10
            hundreds1 -= 1
            steps.append(f"\\text{{Tens: }} {tens1} - {tens2} = {tens1 - tens2}")
        else:
            if tens2 > 0:
                steps.append(f"\\text{{Tens: }} {tens1} - {tens2} = {tens1 - tens2}")

        # Hundreds place
        if hundreds1 > 0 or hundreds2 > 0:
            steps.append(f"\\text{{Hundreds: }} {hundreds1} - {hundreds2} = {hundreds1 - hundreds2}")

        steps.append(f"\\text{{Answer: }} {result}")
        return steps

    def _generate_easy(self) -> Equation:
        """Generate easy problems: 2-digit - 2-digit with regrouping in ones only."""
        # Ensure regrouping in ones place only
        while True:
            num1 = random.randint(20, 99)
            num2 = random.randint(10, num1 - 5)
            if self._requires_regrouping_ones(num1, num2) and not self._requires_regrouping_tens(num1, num2):
                break

        result = num1 - num2
        latex = f"{num1} - {num2}"
        solution = str(result)
        steps = self._get_subtraction_steps(num1, num2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 3-digit - 2-digit or 3-digit with regrouping."""
        choice = random.randint(1, 3)

        if choice == 1:
            # 3-digit - 2-digit with regrouping
            attempts = 0
            while attempts < 100:
                num1 = random.randint(100, 900)
                num2 = random.randint(20, 99)
                if self._requires_regrouping_ones(num1, num2) or self._requires_regrouping_tens(num1, num2):
                    break
                attempts += 1
            if attempts >= 100:
                # Fallback: force regrouping
                num1 = 145
                num2 = 67
        elif choice == 2:
            # 3-digit - 3-digit with one regrouping
            attempts = 0
            while attempts < 100:
                num1 = random.randint(200, 900)
                num2 = random.randint(100, num1 - 20)
                if self._requires_regrouping_ones(num1, num2) or self._requires_regrouping_tens(num1, num2):
                    break
                attempts += 1
            if attempts >= 100:
                # Fallback: force regrouping
                num1 = 345
                num2 = 167
        else:
            # 2-digit - 2-digit with regrouping in tens
            attempts = 0
            while attempts < 100:
                num1 = random.randint(50, 99)
                num2 = random.randint(30, num1 - 5)
                if self._requires_regrouping_tens(num1, num2):
                    break
                attempts += 1
            if attempts >= 100:
                # Fallback: force regrouping in tens
                num1 = 82
                num2 = 57

        result = num1 - num2
        latex = f"{num1} - {num2}"
        solution = str(result)
        steps = self._get_subtraction_steps(num1, num2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: 3-digit - 3-digit with multiple regroupings."""
        # Ensure at least two regroupings
        attempts = 0
        while attempts < 100:
            num1 = random.randint(300, 900)
            num2 = random.randint(150, num1 - 50)
            regroups = sum([
                self._requires_regrouping_ones(num1, num2),
                self._requires_regrouping_tens(num1, num2)
            ])
            if regroups >= 2:
                break
            attempts += 1

        if attempts >= 100:
            # Fallback: force multiple regroupings
            num1 = 543
            num2 = 287

        result = num1 - num2
        latex = f"{num1} - {num2}"
        solution = str(result)
        steps = self._get_subtraction_steps(num1, num2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: word problems with regrouping, including zeros."""
        # Include problems with zeros that require regrouping
        choice = random.randint(1, 2)

        if choice == 1:
            # Regular 3-digit subtraction with regrouping
            attempts = 0
            while attempts < 100:
                num1 = random.randint(250, 800)
                num2 = random.randint(125, num1 - 50)
                if self._requires_regrouping_ones(num1, num2) or self._requires_regrouping_tens(num1, num2):
                    break
                attempts += 1
            if attempts >= 100:
                # Fallback
                num1 = 456
                num2 = 189
        else:
            # Numbers with zeros (e.g., 400, 500, 600)
            num1 = random.choice([300, 400, 500, 600, 700, 800])
            num2 = random.randint(125, 275)

        contexts = [
            f"A store had {num1} items in stock. They sold {num2} items",
            f"A school has {num1} students. {num2} students are on a field trip",
            f"A farmer had {num1} apples. He sold {num2} apples at the market",
            f"The library has {num1} books. {num2} books are checked out",
            f"A factory produced {num1} toys. They shipped {num2} toys to stores"
        ]

        context = random.choice(contexts)
        result = num1 - num2

        latex = f"\\text{{{context}. How many are left?}}"
        solution = str(result)
        steps = [f"{num1} - {num2}"] + self._get_subtraction_steps(num1, num2)

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = SubtractingWithRegroupingWithin1000Generator()

    print("Easy (2-digit - 2-digit, regrouping in ones):")
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
