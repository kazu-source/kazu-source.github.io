"""
Generator for Properties of Equality (Addition and Subtraction) worksheets.
Creates problems that test understanding of addition and subtraction properties of equality.
"""

import random
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class PropertyProblem:
    """Represents a property of equality problem."""
    equation: str  # The equation to solve (e.g., "x - 8 = 12")
    latex: str  # LaTeX format for display
    solution: int  # The solution value (e.g., 20)
    property_type: str  # "addition" or "subtraction" - which property is used to solve


class PropertiesOfEqualityGenerator:
    """Generates problems testing properties of equality for addition and subtraction."""

    def __init__(self):
        """Initialize the generator."""
        self.difficulty_ranges = {
            'easy': (1, 10),      # Numbers 1-10
            'medium': (1, 20),    # Numbers 1-20
            'hard': (1, 50),      # Numbers 1-50
            'challenge': (1, 100) # Numbers 1-100
        }

    def _generate_addition_property(self, difficulty: str) -> PropertyProblem:
        """
        Generate an addition property of equality problem.

        Format: x - b = c (student must add b to both sides to solve)
        Solution: x = c + b

        Args:
            difficulty: Difficulty level ('easy', 'medium', 'hard')

        Returns:
            PropertyProblem object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 10))

        # Generate the number being subtracted and the result
        b = random.randint(1, max_val)  # Number being subtracted from x
        c = random.randint(min_val, max_val)  # Right side of equation

        # Solution: x = c + b (must add b to both sides)
        solution = c + b

        # Create the equation: x - b = c
        equation = f"x - {b} = {c}"
        latex = f"x - {b} = {c}"

        return PropertyProblem(
            equation=equation,
            latex=latex,
            solution=solution,
            property_type="addition"
        )

    def _generate_subtraction_property(self, difficulty: str) -> PropertyProblem:
        """
        Generate a subtraction property of equality problem.

        Format: x + b = c (student must subtract b from both sides to solve)
        Solution: x = c - b

        Args:
            difficulty: Difficulty level ('easy', 'medium', 'hard', 'challenge')

        Returns:
            PropertyProblem object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 10))

        # Generate the number being added and the result
        b = random.randint(1, max_val)  # Number being added to x

        # For easy/medium: ensure solution is positive
        # For hard/challenge: allow negative solutions
        if difficulty in ['easy', 'medium']:
            c = random.randint(b + 1, max_val + b)  # Ensures c - b > 0
        else:  # hard or challenge
            c = random.randint(min_val, max_val + b)

        # Solution: x = c - b (must subtract b from both sides)
        solution = c - b

        # Create the equation: x + b = c
        equation = f"x + {b} = {c}"
        latex = f"x + {b} = {c}"

        return PropertyProblem(
            equation=equation,
            latex=latex,
            solution=solution,
            property_type="subtraction"
        )

    def _generate_combined_property(self, difficulty: str) -> PropertyProblem:
        """
        Generate a combined property problem for challenge difficulty.

        Format: ax + b = c or ax - b = c (requires both operations)
        This combines addition/subtraction with coefficient manipulation.

        Args:
            difficulty: Difficulty level (typically 'challenge')

        Returns:
            PropertyProblem object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 100))

        # Generate coefficient, constant, and solution
        a = random.randint(2, 5)  # Coefficient for x
        x = random.randint(min_val // 2, max_val // 2)  # Solution
        b = random.randint(10, max_val)  # Constant term

        # Randomly choose add or subtract
        if random.choice([True, False]):
            # Format: ax + b = c
            c = a * x + b
            equation = f"{a}x + {b} = {c}"
            latex = f"{a}x + {b} = {c}"
            property_type = "combined (subtraction then division)"
        else:
            # Format: ax - b = c
            c = a * x - b
            equation = f"{a}x - {b} = {c}"
            latex = f"{a}x - {b} = {c}"
            property_type = "combined (addition then division)"

        return PropertyProblem(
            equation=equation,
            latex=latex,
            solution=x,
            property_type=property_type
        )

    def generate_problem(self, difficulty: str = 'medium',
                        property_type: str = 'mixed') -> PropertyProblem:
        """
        Generate a single property of equality problem.

        Args:
            difficulty: 'easy', 'medium', 'hard', or 'challenge'
            property_type: 'addition', 'subtraction', or 'mixed'

        Returns:
            PropertyProblem object
        """
        # For challenge difficulty, use combined properties
        if difficulty == 'challenge':
            return self._generate_combined_property(difficulty)

        if property_type == 'mixed':
            # Randomly choose between addition and subtraction
            property_type = random.choice(['addition', 'subtraction'])

        if property_type == 'addition':
            return self._generate_addition_property(difficulty)
        else:  # subtraction
            return self._generate_subtraction_property(difficulty)

    def generate_worksheet(self, difficulty: str = 'medium',
                          num_problems: int = 10,
                          property_type: str = 'mixed') -> List[PropertyProblem]:
        """
        Generate a complete worksheet of property problems.

        Args:
            difficulty: 'easy', 'medium', 'hard', or 'challenge'
            num_problems: Number of problems to generate
            property_type: 'addition', 'subtraction', or 'mixed'

        Returns:
            List of PropertyProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty, property_type)
            problems.append(problem)

        return problems


# Example usage and testing
if __name__ == "__main__":
    generator = PropertiesOfEqualityGenerator()

    print("=" * 60)
    print("Properties of Equality - Addition and Subtraction")
    print("=" * 60)
    print()

    # Generate sample problems
    print("EASY Problems (Mixed):")
    problems = generator.generate_worksheet('easy', 5, 'mixed')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. Equation: {prob.equation}")
        print(f"   Property needed: {prob.property_type.title()} Property of Equality")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 60)
    print("\nMEDIUM Problems (Addition Property only):")
    print("(These are x - b = c format, requiring addition to solve)")
    problems = generator.generate_worksheet('medium', 3, 'addition')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. Equation: {prob.equation}")
        print(f"   Property needed: Addition Property of Equality")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 60)
    print("\nHARD Problems (Subtraction Property only):")
    print("(These are x + b = c format, requiring subtraction to solve)")
    problems = generator.generate_worksheet('hard', 3, 'subtraction')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. Equation: {prob.equation}")
        print(f"   Property needed: Subtraction Property of Equality")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 60)
    print("\nCHALLENGE Problems (Combined Properties):")
    print("(These are ax + b = c or ax - b = c format, requiring multiple steps)")
    problems = generator.generate_worksheet('challenge', 3, 'mixed')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. Equation: {prob.equation}")
        print(f"   Property needed: {prob.property_type.title()}")
        print(f"   Solution: x = {prob.solution}")
