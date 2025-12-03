"""
One-Step Inequalities Generator
High School Algebra - Unit 3

Generates problems for solving and understanding one-step inequalities.
Covers:
- Addition/Subtraction inequalities
- Multiplication/Division with positive coefficients
- Multiplication/Division with negative coefficients (requiring sign flip)
- Word problems requiring one-step inequalities
- Understanding of number line graphing (open vs closed circles)
"""

import random
from typing import List
import sys
import os

# Add parent directory to path to import Equation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))
from equation_generator import Equation


class OneStepInequalitiesGenerator:
    """Generates one-step inequality problems with varying difficulty levels."""

    def __init__(self, seed=None):
        """
        Initialize the one-step inequalities generator.

        Args:
            seed: Random seed for reproducibility (optional)
        """
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
        """Generate a single inequality problem based on difficulty."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """
        Generate easy one-step inequalities using addition/subtraction.
        Examples: x + 5 > 12, x - 3 < 8
        """
        # Random inequality sign
        inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])

        # Choose between addition or subtraction
        operation = random.choice(['add', 'subtract'])

        # Generate values
        a = random.randint(1, 15)
        solution = random.randint(-10, 20)

        if operation == 'add':
            # x + a > b  =>  x > b - a
            b = solution + a
            latex = f"x + {a} {inequality_sign} {b}"
            steps = [
                f"Subtract {a} from both sides",
                f"x {inequality_sign} {b} - {a}",
                f"x {inequality_sign} {solution}"
            ]
            solution_str = f"x {inequality_sign} {solution}"

            # Determine circle type for graphing
            circle_type = "closed" if inequality_sign in ['\\leq', '\\geq'] else "open"
            direction = "right" if inequality_sign in ['>', '\\geq'] else "left"
            graph_note = f"Graph: {circle_type} circle at {solution}, shade {direction}"

        else:  # subtract
            # x - a > b  =>  x > b + a
            b = solution - a
            latex = f"x - {a} {inequality_sign} {b}"
            steps = [
                f"Add {a} to both sides",
                f"x {inequality_sign} {b} + {a}",
                f"x {inequality_sign} {solution}"
            ]
            solution_str = f"x {inequality_sign} {solution}"

            circle_type = "closed" if inequality_sign in ['\\leq', '\\geq'] else "open"
            direction = "right" if inequality_sign in ['>', '\\geq'] else "left"
            graph_note = f"Graph: {circle_type} circle at {solution}, shade {direction}"

        steps.append(graph_note)

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """
        Generate medium one-step inequalities using multiplication/division.
        Uses only positive coefficients (no sign flip required).
        Examples: 3x > 12, x/4 < 5
        """
        inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])

        # Choose between multiplication or division
        operation = random.choice(['multiply', 'divide'])

        if operation == 'multiply':
            # ax > b  =>  x > b/a
            a = random.randint(2, 12)
            solution = random.randint(-10, 15)
            b = a * solution

            latex = f"{a}x {inequality_sign} {b}"
            steps = [
                f"Divide both sides by {a}",
                f"x {inequality_sign} \\frac{{{b}}}{{{a}}}",
                f"x {inequality_sign} {solution}"
            ]
            solution_str = f"x {inequality_sign} {solution}"

        else:  # divide
            # x/a > b  =>  x > ab
            a = random.randint(2, 10)
            b = random.randint(-8, 12)
            solution = a * b

            latex = f"\\frac{{x}}{{{a}}} {inequality_sign} {b}"
            steps = [
                f"Multiply both sides by {a}",
                f"x {inequality_sign} {a} \\times {b}",
                f"x {inequality_sign} {solution}"
            ]
            solution_str = f"x {inequality_sign} {solution}"

        # Graph notation
        circle_type = "closed" if inequality_sign in ['\\leq', '\\geq'] else "open"
        direction = "right" if inequality_sign in ['>', '\\geq'] else "left"
        graph_note = f"Graph: {circle_type} circle at {solution}, shade {direction}"
        steps.append(graph_note)

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """
        Generate hard one-step inequalities with negative coefficients.
        REQUIRES FLIPPING THE INEQUALITY SIGN when dividing/multiplying by negative.
        Examples: -2x > 8  =>  x < -4
        """
        inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])

        # Negative coefficient
        a = random.randint(-10, -2)
        solution = random.randint(-12, 12)
        b = a * solution

        latex = f"{a}x {inequality_sign} {b}"

        # FLIP the inequality sign when dividing by negative
        flipped_sign = {
            '<': '>',
            '>': '<',
            '\\leq': '\\geq',
            '\\geq': '\\leq'
        }[inequality_sign]

        steps = [
            f"Divide both sides by {a}",
            f"IMPORTANT: Flip inequality sign when dividing by negative!",
            f"x {flipped_sign} \\frac{{{b}}}{{{a}}}",
            f"x {flipped_sign} {solution}"
        ]
        solution_str = f"x {flipped_sign} {solution}"

        # Graph notation with flipped sign
        circle_type = "closed" if flipped_sign in ['\\leq', '\\geq'] else "open"
        direction = "right" if flipped_sign in ['>', '\\geq'] else "left"
        graph_note = f"Graph: {circle_type} circle at {solution}, shade {direction}"
        steps.append(graph_note)

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """
        Generate challenge word problems requiring one-step inequalities.
        Students must translate real-world scenario into inequality and solve.
        """
        problem_type = random.choice(['money', 'score', 'temperature', 'weight', 'age'])

        if problem_type == 'money':
            name = random.choice(['Sarah', 'John', 'Maria', 'David', 'Emma'])
            current = random.randint(50, 200)
            needed = random.randint(current + 20, current + 100)

            latex = f"\\text{{{name} has \\${current}. She needs at least \\${needed}. How much more money (x) does she need?}}"
            solution_value = needed - current
            inequality = f"x + {current} \\geq {needed}"
            solution_str = f"x \\geq {solution_value}"

            steps = [
                f"Set up inequality: {inequality}",
                f"Subtract {current} from both sides",
                f"x \\geq {solution_value}",
                f"{name} needs at least \\${solution_value} more"
            ]

        elif problem_type == 'score':
            name = random.choice(['Alex', 'Jordan', 'Casey', 'Taylor', 'Morgan'])
            current = random.randint(70, 90)
            target = random.randint(current + 5, 100)

            latex = f"\\text{{{name} scored {current} points. To win, they need more than {target} points total. How many more points (x) are needed?}}"
            solution_value = target - current
            inequality = f"x + {current} > {target}"
            solution_str = f"x > {solution_value}"

            steps = [
                f"Set up inequality: {inequality}",
                f"Subtract {current} from both sides",
                f"x > {solution_value}",
                f"{name} needs more than {solution_value} additional points"
            ]

        elif problem_type == 'temperature':
            city = random.choice(['Denver', 'Seattle', 'Boston', 'Phoenix', 'Chicago'])
            current = random.randint(30, 70)
            target = random.randint(current + 10, current + 40)

            latex = f"\\text{{The temperature in {city} is {current}°F. It must rise to at least {target}°F. How many degrees (x) must it rise?}}"
            solution_value = target - current
            inequality = f"x + {current} \\geq {target}"
            solution_str = f"x \\geq {solution_value}"

            steps = [
                f"Set up inequality: {inequality}",
                f"Subtract {current} from both sides",
                f"x \\geq {solution_value}",
                f"Temperature must rise at least {solution_value}°F"
            ]

        elif problem_type == 'weight':
            multiplier = random.randint(3, 8)
            weight = random.randint(15, 40)
            total = multiplier * weight

            latex = f"\\text{{Each box weighs x pounds. {multiplier} boxes weigh less than {total} lbs total. Find the weight of each box.}}"
            inequality = f"{multiplier}x < {total}"
            solution_str = f"x < {weight}"

            steps = [
                f"Set up inequality: {inequality}",
                f"Divide both sides by {multiplier}",
                f"x < {weight}",
                f"Each box weighs less than {weight} pounds"
            ]

        else:  # age
            name1 = random.choice(['Lisa', 'Tom', 'Anna', 'Mike', 'Kate'])
            name2 = random.choice(['her brother', 'his sister', 'her friend', 'his cousin'])
            multiplier = random.randint(2, 5)
            age = random.randint(8, 20)
            total = multiplier * age

            latex = f"\\text{{{name1} is x years old. {multiplier} times her age is at most {total} years. How old is {name1}?}}"
            inequality = f"{multiplier}x \\leq {total}"
            solution_str = f"x \\leq {age}"

            steps = [
                f"Set up inequality: {inequality}",
                f"Divide both sides by {multiplier}",
                f"x \\leq {age}",
                f"{name1} is at most {age} years old"
            ]

        return Equation(
            latex=latex,
            solution=solution_str,
            steps=steps,
            difficulty='challenge'
        )


if __name__ == "__main__":
    # Test the generator
    gen = OneStepInequalitiesGenerator()

    print("One-Step Inequalities Generator Test")
    print("=" * 80)
    print("\nThis generator covers:")
    print("- Easy: Addition/Subtraction inequalities")
    print("- Medium: Multiplication/Division with positive coefficients")
    print("- Hard: Negative coefficients (with sign flip)")
    print("- Challenge: Word problems")
    print("=" * 80)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 80)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"\n{i}. Problem: {problem.latex}")
            print(f"   Solution: {problem.solution}")
            if problem.steps:
                print(f"   Steps:")
                for step in problem.steps:
                    print(f"     - {step}")
