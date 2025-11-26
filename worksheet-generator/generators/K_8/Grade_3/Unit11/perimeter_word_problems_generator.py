"""
Perimeter Word Problems Generator - Grade 3 Unit 11
Generates real-world word problems involving perimeter
Example: Sarah wants to fence her garden. The garden is 12 feet long and 8 feet wide. How much fencing does she need?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PerimeterWordProblemsGenerator:
    """Generates perimeter word problems."""

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
        """Generate easy problems: simple contexts with small numbers (2-5 units)."""
        length = random.randint(3, 5)
        width = random.randint(2, 4)
        perimeter = 2 * (length + width)

        contexts = [
            (f"A picture frame is {length} inches long and {width} inches wide", "inches"),
            (f"A small rug is {length} feet long and {width} feet wide", "feet"),
            (f"A book cover is {length} inches by {width} inches", "inches"),
            (f"A placemat measures {length} inches by {width} inches", "inches")
        ]

        context, unit = random.choice(contexts)

        questions = [
            "What is the perimeter?",
            "How much border is needed to go around it?",
            "What is the distance around it?"
        ]

        question = random.choice(questions)
        latex = f"\\text{{{context}. {question}}}"
        solution = f"{perimeter} {unit}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Perimeter = 2 × (length + width)}}",
                f"\\text{{Perimeter = 2 × ({length} + {width})}}",
                f"\\text{{Perimeter = 2 × {length + width} = {perimeter} {unit}}}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: various real-world contexts (3-10 units)."""
        shape_type = random.choice(['rectangle', 'square', 'triangle'])

        if shape_type == 'rectangle':
            length = random.randint(5, 10)
            width = random.randint(3, 8)
            perimeter = 2 * (length + width)

            contexts = [
                (f"Sarah needs to frame a poster that is {length} inches by {width} inches", "inches", "frame"),
                (f"A garden bed measures {length} feet by {width} feet", "feet", "fence"),
                (f"A swimming pool is {length} meters long and {width} meters wide", "meters", "rope"),
                (f"A rectangular table is {length} feet by {width} feet", "feet", "trim")
            ]

            context, unit, item = random.choice(contexts)
            latex = f"\\text{{{context}. How much {item} is needed for the perimeter?}}"
            solution = f"{perimeter} {unit}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Find perimeter: 2 × (length + width)}}",
                    f"\\text{{Perimeter = 2 × ({length} + {width}) = {perimeter} {unit}}}"
                ],
                difficulty='medium'
            )

        elif shape_type == 'square':
            side = random.randint(4, 10)
            perimeter = 4 * side

            contexts = [
                (f"A square sandbox has sides of {side} feet", "feet", "wood border"),
                (f"A square tile measures {side} inches on each side", "inches", "metal edge"),
                (f"A square garden plot is {side} meters per side", "meters", "fencing")
            ]

            context, unit, item = random.choice(contexts)
            latex = f"\\text{{{context}. How much {item} is needed?}}"
            solution = f"{perimeter} {unit}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter = 4 × side}}",
                    f"\\text{{Perimeter = 4 × {side} = {perimeter} {unit}}}"
                ],
                difficulty='medium'
            )

        else:  # triangle
            side1 = random.randint(4, 10)
            side2 = random.randint(4, 10)
            side3 = random.randint(4, 10)
            perimeter = side1 + side2 + side3

            contexts = [
                (f"A triangular flag has sides of {side1}, {side2}, and {side3} inches", "inches", "ribbon"),
                (f"A triangular garden has sides measuring {side1}, {side2}, and {side3} feet", "feet", "border")
            ]

            context, unit, item = random.choice(contexts)
            latex = f"\\text{{{context}. How much {item} is needed for the perimeter?}}"
            solution = f"{perimeter} {unit}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Add all sides}}",
                    f"{side1} + {side2} + {side3} = {perimeter} \\text{{ {unit}}}"
                ],
                difficulty='medium'
            )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: multi-step or more complex contexts (5-12 units)."""
        problem_type = random.choice(['fence_cost', 'comparison', 'extension'])

        if problem_type == 'fence_cost':
            length = random.randint(8, 12)
            width = random.randint(6, 10)
            perimeter = 2 * (length + width)
            cost_per_unit = random.randint(2, 5)
            total_cost = perimeter * cost_per_unit

            latex = f"\\text{{A rectangular yard is {length} feet by {width} feet. Fencing costs \\${cost_per_unit} per foot. }}" + \
                    f"\\text{{What is the total cost to fence the yard?}}"
            solution = f"${total_cost}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter = 2 × ({length} + {width}) = {perimeter} feet}}",
                    f"\\text{{Cost = {perimeter} × \\${cost_per_unit} = \\${total_cost}}}"
                ],
                difficulty='hard'
            )

        elif problem_type == 'comparison':
            length1 = random.randint(7, 12)
            width1 = random.randint(5, 9)
            perimeter1 = 2 * (length1 + width1)

            length2 = random.randint(7, 12)
            width2 = random.randint(5, 9)
            perimeter2 = 2 * (length2 + width2)

            # Ensure different perimeters
            while perimeter1 == perimeter2:
                width2 = random.randint(5, 9)
                perimeter2 = 2 * (length2 + width2)

            difference = abs(perimeter1 - perimeter2)

            latex = f"\\text{{Room A is {length1} ft by {width1} ft. Room B is {length2} ft by {width2} ft. }}" + \
                    f"\\text{{How much more baseboard trim is needed for the larger room?}}"
            solution = f"{difference} feet"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter A: 2 × ({length1} + {width1}) = {perimeter1} ft}}",
                    f"\\text{{Perimeter B: 2 × ({length2} + {width2}) = {perimeter2} ft}}",
                    f"\\text{{Difference: {max(perimeter1, perimeter2)} - {min(perimeter1, perimeter2)} = {difference} ft}}"
                ],
                difficulty='hard'
            )

        else:  # extension
            original_side = random.randint(6, 10)
            original_perimeter = 4 * original_side

            extension = random.randint(2, 4)
            new_side = original_side + extension
            new_perimeter = 4 * new_side

            difference = new_perimeter - original_perimeter

            latex = f"\\text{{A square patio has sides of {original_side} feet. It will be extended by {extension} feet on each side. }}" + \
                    f"\\text{{How much more border will be needed?}}"
            solution = f"{difference} feet"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Original perimeter: 4 × {original_side} = {original_perimeter} ft}}",
                    f"\\text{{New side: {original_side} + {extension} = {new_side} ft}}",
                    f"\\text{{New perimeter: 4 × {new_side} = {new_perimeter} ft}}",
                    f"\\text{{Additional border: {new_perimeter} - {original_perimeter} = {difference} ft}}"
                ],
                difficulty='hard'
            )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex multi-step or missing information."""
        problem_type = random.choice(['missing_side', 'two_shapes', 'partial_fence'])

        if problem_type == 'missing_side':
            # Given perimeter and budget/material, find if possible
            length = random.randint(8, 12)
            width = random.randint(6, 10)
            perimeter = 2 * (length + width)

            # Give perimeter and one dimension
            latex = f"\\text{{A rectangular field has a perimeter of {perimeter} feet. The length is {length} feet. }}" + \
                    f"\\text{{What is the width?}}"
            solution = f"{width} feet"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter = 2 × (length + width)}}",
                    f"{perimeter} = 2 × ({length} + \\text{{width}})}}",
                    f"{perimeter // 2} = {length} + \\text{{width}}",
                    f"\\text{{Width = {perimeter // 2} - {length} = {width} feet}}"
                ],
                difficulty='challenge'
            )

        elif problem_type == 'two_shapes':
            # Two adjacent gardens sharing one side
            length1 = random.randint(8, 12)
            width1 = random.randint(6, 10)

            length2 = random.randint(8, 12)
            width2 = width1  # They share this side

            # Total fence needed (minus the shared side)
            total_perimeter = 2 * (length1 + width1) + 2 * (length2 + width2) - 2 * width1

            latex = f"\\text{{Two gardens share one side. Garden A is {length1} by {width1} feet. }}" + \
                    f"\\text{{Garden B is {length2} by {width2} feet. How much fencing is needed?}}"
            solution = f"{total_perimeter} feet"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter A: 2 × ({length1} + {width1}) = {2 * (length1 + width1)}}}",
                    f"\\text{{Perimeter B: 2 × ({length2} + {width2}) = {2 * (length2 + width2)}}}",
                    f"\\text{{Subtract shared side: {2 * (length1 + width1)} + {2 * (length2 + width2)} - 2 × {width1}}}",
                    f"\\text{{Total fencing: {total_perimeter} feet}}"
                ],
                difficulty='challenge'
            )

        else:  # partial_fence
            # Rectangular yard, one side is house (no fence needed)
            length = random.randint(10, 15)
            width = random.randint(8, 12)

            # Fence needed for 3 sides (not the side with house)
            fence_needed = length + 2 * width
            cost_per_foot = random.randint(3, 6)
            total_cost = fence_needed * cost_per_foot

            latex = f"\\text{{A backyard is {length} by {width} feet. One {length}-foot side is the house (no fence). }}" + \
                    f"\\text{{Fencing costs \\${cost_per_foot} per foot. What is the total cost?}}"
            solution = f"${total_cost}"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Need fence on 3 sides: {length} + {width} + {width}}}",
                    f"\\text{{Fence needed: {length} + 2 × {width} = {fence_needed} feet}}",
                    f"\\text{{Cost: {fence_needed} × \\${cost_per_foot} = \\${total_cost}}}"
                ],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = PerimeterWordProblemsGenerator()

    print("Perimeter Word Problems Generator - Grade 3 Unit 11\n")

    print("Easy Problems:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium Problems:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard Problems:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge Problems:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
