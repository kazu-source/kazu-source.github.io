"""
Generator for Properties of Equality (Multiplication and Division) worksheets.
Creates problems that test understanding of multiplication and division properties of equality.
"""

import random
from typing import List, Tuple
from properties_generator import PropertyProblem  # Import from the main properties module


class PropertiesMultDivGenerator:
    """Generates problems testing properties of equality for multiplication and division."""

    def __init__(self):
        """Initialize the generator."""
        self.difficulty_ranges = {
            'easy': (1, 10),      # Numbers 1-10
            'medium': (1, 20),    # Numbers 1-20
            'hard': (1, 50),      # Numbers 1-50
            'challenge': (1, 100) # Numbers 1-100
        }
        # Common divisors/multipliers for cleaner problems
        self.easy_divisors = [2, 3, 4, 5]
        self.medium_divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.hard_divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20]
        self.challenge_divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30, 40, 50]

    def _generate_multiplication_property(self, difficulty: str) -> PropertyProblem:
        """
        Generate a multiplication property of equality problem.

        Format: x / b = c (student must multiply both sides by b to solve)
        Solution: x = c * b

        Args:
            difficulty: Difficulty level ('easy', 'medium', 'hard', 'challenge')

        Returns:
            PropertyProblem object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 10))

        # Select divisor based on difficulty
        if difficulty == 'easy':
            divisors = self.easy_divisors
        elif difficulty == 'medium':
            divisors = self.medium_divisors
        elif difficulty == 'hard':
            divisors = self.hard_divisors
        else:  # challenge
            divisors = self.challenge_divisors

        # Generate the divisor and the result
        b = random.choice(divisors)  # Number x is divided by
        c = random.randint(1, max_val)  # Right side of equation

        # Solution: x = c * b (must multiply b to both sides)
        solution = c * b

        # Create the equation: x / b = c
        # Use \frac for better display (raw string to avoid double escaping)
        equation = f"x / {b} = {c}"
        latex = rf"\frac{{x}}{{{b}}} = {c}"

        return PropertyProblem(
            equation=equation,
            latex=latex,
            solution=solution,
            property_type="multiplication"
        )

    def _generate_division_property(self, difficulty: str) -> PropertyProblem:
        """
        Generate a division property of equality problem.

        Format: b * x = c (student must divide both sides by b to solve)
        Solution: x = c / b

        Args:
            difficulty: Difficulty level ('easy', 'medium', 'hard', 'challenge')

        Returns:
            PropertyProblem object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 10))

        # Select multiplier based on difficulty
        if difficulty == 'easy':
            multipliers = self.easy_divisors
        elif difficulty == 'medium':
            multipliers = self.medium_divisors
        elif difficulty == 'hard':
            multipliers = self.hard_divisors
        else:  # challenge
            multipliers = self.challenge_divisors

        # Generate the multiplier and ensure c is divisible by b
        b = random.choice(multipliers)  # Number multiplying x
        x = random.randint(1, max_val)  # The solution
        c = b * x  # Right side (ensures clean division)

        # Solution: x = c / b (must divide both sides by b)
        solution = x

        # Create the equation: b * x = c
        equation = f"{b}x = {c}"
        latex = f"{b}x = {c}"

        return PropertyProblem(
            equation=equation,
            latex=latex,
            solution=solution,
            property_type="division"
        )

    def _generate_fraction_property(self, difficulty: str) -> PropertyProblem:
        """
        Generate a fraction-based property problem for challenge difficulty.

        Format: (a/b)x = c or x/(a/b) = c
        Solution involves working with fractional coefficients.

        Args:
            difficulty: Difficulty level (typically 'challenge')

        Returns:
            PropertyProblem object
        """
        # Generate fraction a/b as coefficient
        numerators = [2, 3, 4, 5]
        denominators = [2, 3, 4, 5]

        a = random.choice(numerators)
        b = random.choice(denominators)

        # Ensure a != b for non-trivial fractions
        while a == b:
            b = random.choice(denominators)

        # Generate solution that creates whole number when possible
        x = random.randint(5, 50)

        # Randomly choose multiplication or division with fractions
        if random.choice([True, False]):
            # Format: (a/b)x = c where c = (a/b) * x
            # This will involve dividing by a fraction
            c = (a * x) // b if (a * x) % b == 0 else round((a * x) / b, 2)
            equation = f"({a}/{b})x = {c}"
            latex = rf"\frac{{{a}}}{{{b}}}x = {c}"
            property_type = "division by fraction"
        else:
            # Format: x/(a/b) = c which is equivalent to (b/a)x = c
            c = (b * x) // a if (b * x) % a == 0 else round((b * x) / a, 2)
            equation = f"x/({a}/{b}) = {c}"
            latex = rf"\frac{{x}}{{\frac{{{a}}}{{{b}}}}} = {c}"
            property_type = "multiplication by reciprocal"

        return PropertyProblem(
            equation=equation,
            latex=latex,
            solution=x,
            property_type=property_type
        )

    def _generate_decimal_property(self, difficulty: str) -> PropertyProblem:
        """
        Generate a decimal-based property problem for challenge difficulty.

        Format: dx = c or x/d = c where d is a decimal
        Solution involves working with decimal coefficients.

        Args:
            difficulty: Difficulty level (typically 'challenge')

        Returns:
            PropertyProblem object
        """
        # Common decimal multipliers/divisors
        decimals = [0.5, 1.5, 2.5, 0.25, 0.75, 1.25, 0.2, 0.4, 0.6, 0.8]

        d = random.choice(decimals)
        x = random.randint(10, 100)

        # Randomly choose multiplication or division with decimals
        if random.choice([True, False]):
            # Format: dx = c
            c = round(d * x, 2)
            equation = f"{d}x = {c}"
            latex = f"{d}x = {c}"
            property_type = "division by decimal"
        else:
            # Format: x/d = c
            c = round(x / d, 2)
            equation = f"x/{d} = {c}"
            latex = rf"\frac{{x}}{{{d}}} = {c}"
            property_type = "multiplication by decimal"

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
            property_type: 'multiplication', 'division', or 'mixed'

        Returns:
            PropertyProblem object
        """
        # For challenge difficulty, use fractions, decimals, or standard problems
        if difficulty == 'challenge':
            challenge_type = random.choice(['fraction', 'decimal', 'standard'])
            if challenge_type == 'fraction':
                return self._generate_fraction_property(difficulty)
            elif challenge_type == 'decimal':
                return self._generate_decimal_property(difficulty)
            # Otherwise fall through to standard generation with larger numbers

        if property_type == 'mixed':
            # Randomly choose between multiplication and division
            property_type = random.choice(['multiplication', 'division'])

        if property_type == 'multiplication':
            return self._generate_multiplication_property(difficulty)
        else:  # division
            return self._generate_division_property(difficulty)

    def generate_worksheet(self, difficulty: str = 'medium',
                          num_problems: int = 10,
                          property_type: str = 'mixed') -> List[PropertyProblem]:
        """
        Generate a complete worksheet of property problems.

        Args:
            difficulty: 'easy', 'medium', 'hard', or 'challenge'
            num_problems: Number of problems to generate
            property_type: 'multiplication', 'division', or 'mixed'

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
    generator = PropertiesMultDivGenerator()

    print("=" * 60)
    print("Properties of Equality - Multiplication and Division")
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
    print("\nMEDIUM Problems (Multiplication Property only):")
    print("(These are x / b = c format, requiring multiplication to solve)")
    problems = generator.generate_worksheet('medium', 3, 'multiplication')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. Equation: {prob.equation}")
        print(f"   Property needed: Multiplication Property of Equality")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 60)
    print("\nHARD Problems (Division Property only):")
    print("(These are bx = c format, requiring division to solve)")
    problems = generator.generate_worksheet('hard', 3, 'division')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. Equation: {prob.equation}")
        print(f"   Property needed: Division Property of Equality")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 60)
    print("\nCHALLENGE Problems (Fractions, Decimals, and Large Divisors):")
    print("(These involve fractional/decimal coefficients or very large divisors)")
    problems = generator.generate_worksheet('challenge', 5, 'mixed')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. Equation: {prob.equation}")
        print(f"   Property needed: {prob.property_type.title()}")
        print(f"   Solution: x = {prob.solution}")
