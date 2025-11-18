"""
Generator for Multi-Step Equations.
Creates two-step equations that combine properties of equality.
"""

import random
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class MultiStepEquation:
    """Represents a multi-step equation problem."""
    equation: str  # The equation to solve (e.g., "2x + 5 = 13")
    latex: str  # LaTeX format for display
    solution: int  # The solution value
    steps: List[str]  # List of steps to solve (for answer key)


class MultiStepEquationGenerator:
    """Generates two-step equations combining properties of equality."""

    def __init__(self):
        """Initialize the generator."""
        self.difficulty_ranges = {
            'easy': (1, 10),      # Numbers 1-10
            'medium': (1, 20),    # Numbers 1-20
            'hard': (1, 50),      # Numbers 1-50
            'challenge': (1, 100) # Numbers 1-100
        }

    def _generate_two_step_equation(self, difficulty: str) -> MultiStepEquation:
        """
        Generate a two-step equation of the form ax + b = c or ax - b = c.

        Students must use both multiplication/division AND addition/subtraction properties.

        Format examples:
        - 2x + 5 = 13  (subtract 5, then divide by 2)
        - 3x - 4 = 11  (add 4, then divide by 3)
        - x/2 + 3 = 8  (subtract 3, then multiply by 2)
        - x/4 - 1 = 2  (add 1, then multiply by 4)

        Args:
            difficulty: Difficulty level ('easy', 'medium', 'hard')

        Returns:
            MultiStepEquation object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 10))

        # Randomly choose equation type
        equation_types = ['mult_add', 'mult_sub', 'div_add', 'div_sub']
        eq_type = random.choice(equation_types)

        # Generate solution (the value of x)
        x = random.randint(min_val, max_val)

        if eq_type == 'mult_add':
            # Format: ax + b = c
            # Example: 2x + 5 = 13 where x = 4
            a = random.randint(2, 10 if difficulty == 'easy' else 15)
            b = random.randint(1, max_val)
            c = a * x + b

            equation = f"{a}x + {b} = {c}"
            latex = f"{a}x + {b} = {c}"
            steps = [
                f"Subtract {b} from both sides: {a}x = {c - b}",
                f"Divide both sides by {a}: x = {x}"
            ]

        elif eq_type == 'mult_sub':
            # Format: ax - b = c
            # Example: 3x - 4 = 11 where x = 5
            a = random.randint(2, 10 if difficulty == 'easy' else 15)
            b = random.randint(1, max_val)
            c = a * x - b

            equation = f"{a}x - {b} = {c}"
            latex = f"{a}x - {b} = {c}"
            steps = [
                f"Add {b} to both sides: {a}x = {c + b}",
                f"Divide both sides by {a}: x = {x}"
            ]

        elif eq_type == 'div_add':
            # Format: x/a + b = c
            # Example: x/2 + 3 = 8 where x = 10
            a = random.choice([2, 3, 4, 5] if difficulty == 'easy' else [2, 3, 4, 5, 6, 8, 10])
            # Ensure x is divisible by a for clean solutions
            x = random.randint(1, max_val // a) * a
            b = random.randint(1, max_val)
            c = x // a + b

            equation = f"x/{a} + {b} = {c}"
            latex = rf"\frac{{x}}{{{a}}} + {b} = {c}"
            steps = [
                f"Subtract {b} from both sides: x/{a} = {c - b}",
                f"Multiply both sides by {a}: x = {x}"
            ]

        else:  # div_sub
            # Format: x/a - b = c
            # Example: x/4 - 1 = 2 where x = 12
            a = random.choice([2, 3, 4, 5] if difficulty == 'easy' else [2, 3, 4, 5, 6, 8, 10])
            # Ensure x is divisible by a for clean solutions
            x = random.randint(1, max_val // a) * a
            b = random.randint(1, max_val // 2)
            c = x // a - b

            # Make sure c is positive
            if c <= 0:
                b = 1
                c = x // a - b

            equation = f"x/{a} - {b} = {c}"
            latex = rf"\frac{{x}}{{{a}}} - {b} = {c}"
            steps = [
                f"Add {b} to both sides: x/{a} = {c + b}",
                f"Multiply both sides by {a}: x = {x}"
            ]

        return MultiStepEquation(
            equation=equation,
            latex=latex,
            solution=x,
            steps=steps
        )

    def _generate_challenge_equation(self, difficulty: str) -> MultiStepEquation:
        """
        Generate a complex multi-step equation for challenge difficulty.

        Formats include:
        - a(bx + c) = d (distributive property required)
        - a(bx - c) + d = e (distributive property + additional step)
        - ax + b = cx + d (variables on both sides)

        Args:
            difficulty: Difficulty level (typically 'challenge')

        Returns:
            MultiStepEquation object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 100))

        # Choose equation type
        eq_types = ['distributive', 'distributive_plus', 'variables_both_sides']
        eq_type = random.choice(eq_types)

        if eq_type == 'distributive':
            # Format: a(bx + c) = d or a(bx - c) = d
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            c = random.randint(5, 20)
            x = random.randint(5, max_val // (a * b))

            if random.choice([True, False]):
                # a(bx + c) = d
                d = a * (b * x + c)
                equation = f"{a}({b}x + {c}) = {d}"
                latex = f"{a}({b}x + {c}) = {d}"
                steps = [
                    f"Distribute {a}: {a * b}x + {a * c} = {d}",
                    f"Subtract {a * c} from both sides: {a * b}x = {d - a * c}",
                    f"Divide both sides by {a * b}: x = {x}"
                ]
            else:
                # a(bx - c) = d
                d = a * (b * x - c)
                equation = f"{a}({b}x - {c}) = {d}"
                latex = f"{a}({b}x - {c}) = {d}"
                steps = [
                    f"Distribute {a}: {a * b}x - {a * c} = {d}",
                    f"Add {a * c} to both sides: {a * b}x = {d + a * c}",
                    f"Divide both sides by {a * b}: x = {x}"
                ]

        elif eq_type == 'distributive_plus':
            # Format: a(bx + c) + d = e or a(bx - c) - d = e
            a = random.randint(2, 4)
            b = random.randint(2, 4)
            c = random.randint(5, 15)
            d = random.randint(10, 30)
            x = random.randint(5, max_val // (a * b))

            if random.choice([True, False]):
                # a(bx + c) + d = e
                e = a * (b * x + c) + d
                equation = f"{a}({b}x + {c}) + {d} = {e}"
                latex = f"{a}({b}x + {c}) + {d} = {e}"
                steps = [
                    f"Distribute {a}: {a * b}x + {a * c} + {d} = {e}",
                    f"Combine constants: {a * b}x + {a * c + d} = {e}",
                    f"Subtract {a * c + d} from both sides: {a * b}x = {e - (a * c + d)}",
                    f"Divide both sides by {a * b}: x = {x}"
                ]
            else:
                # a(bx - c) - d = e
                e = a * (b * x - c) - d
                equation = f"{a}({b}x - {c}) - {d} = {e}"
                latex = f"{a}({b}x - {c}) - {d} = {e}"
                steps = [
                    f"Distribute {a}: {a * b}x - {a * c} - {d} = {e}",
                    f"Combine constants: {a * b}x - {a * c + d} = {e}",
                    f"Add {a * c + d} to both sides: {a * b}x = {e + (a * c + d)}",
                    f"Divide both sides by {a * b}: x = {x}"
                ]

        else:  # variables_both_sides
            # Format: ax + b = cx + d
            a = random.randint(3, 8)
            c = random.randint(2, a - 1)  # Ensure a > c for positive coefficient
            x = random.randint(5, 50)
            # Calculate b and d such that equation is satisfied
            b = random.randint(10, 50)
            d = a * x + b - c * x

            equation = f"{a}x + {b} = {c}x + {d}"
            latex = f"{a}x + {b} = {c}x + {d}"
            steps = [
                f"Subtract {c}x from both sides: {a - c}x + {b} = {d}",
                f"Subtract {b} from both sides: {a - c}x = {d - b}",
                f"Divide both sides by {a - c}: x = {x}"
            ]

        return MultiStepEquation(
            equation=equation,
            latex=latex,
            solution=x,
            steps=steps
        )

    def generate_problem(self, difficulty: str = 'medium') -> MultiStepEquation:
        """
        Generate a single multi-step equation.

        Args:
            difficulty: 'easy', 'medium', 'hard', or 'challenge'

        Returns:
            MultiStepEquation object
        """
        if difficulty == 'challenge':
            return self._generate_challenge_equation(difficulty)
        return self._generate_two_step_equation(difficulty)

    def generate_worksheet(self, difficulty: str = 'medium',
                          num_problems: int = 10) -> List[MultiStepEquation]:
        """
        Generate a complete worksheet of multi-step equations.

        Args:
            difficulty: 'easy', 'medium', 'hard', or 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of MultiStepEquation objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)

        return problems


# Example usage and testing
if __name__ == "__main__":
    generator = MultiStepEquationGenerator()

    print("=" * 70)
    print("Multi-Step Equations (Two-Step)")
    print("=" * 70)
    print()

    # Generate sample problems
    print("EASY Problems:")
    problems = generator.generate_worksheet('easy', 5)
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. {prob.equation}")
        print(f"   Steps to solve:")
        for step in prob.steps:
            print(f"   - {step}")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 70)
    print("\nMEDIUM Problems:")
    problems = generator.generate_worksheet('medium', 3)
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. {prob.equation}")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 70)
    print("\nHARD Problems:")
    problems = generator.generate_worksheet('hard', 3)
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. {prob.equation}")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 70)
    print("\nCHALLENGE Problems:")
    print("(Distributive property, variables on both sides, 4+ steps)")
    problems = generator.generate_worksheet('challenge', 3)
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. {prob.equation}")
        print(f"   Steps to solve:")
        for step in prob.steps:
            print(f"   - {step}")
        print(f"   Solution: x = {prob.solution}")
