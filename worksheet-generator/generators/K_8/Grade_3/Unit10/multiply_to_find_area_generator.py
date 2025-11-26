"""
Multiply to Find Area Generator - Grade 3 Unit 10
Generates problems using the length × width formula to find area
Example: A rectangle is 8 units long and 5 units wide. Area = 8 × 5 = 40 square units
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplyToFindAreaGenerator:
    """Generates multiply to find area problems."""

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
        """Generate easy problems: small dimensions (1-5 units)."""
        length = random.randint(2, 5)
        width = random.randint(2, 5)
        area = length * width

        latex = f"\\text{{Find the area: length = {length} units, width = {width} units}}"
        solution = f"{area} square units"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Area = length × width}}",
                f"\\text{{Area = }}{length} \\times {width}",
                f"\\text{{Area = {area} square units}}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: larger dimensions (3-10 units)."""
        length = random.randint(3, 10)
        width = random.randint(3, 10)
        area = length * width

        shapes = [
            f"A rectangle has length {length} units and width {width} units",
            f"A square has sides of {length} units" if length == width else f"A rectangle measures {length} by {width} units",
            f"The dimensions are {length} units by {width} units"
        ]

        shape = random.choice(shapes)
        latex = f"\\text{{{shape}. Find the area.}}"
        solution = f"{area} square units"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Use formula: Area = length × width}}",
                f"{length} \\times {width} = {area}",
                f"\\text{{Area = {area} square units}}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with real-world contexts (4-12 units)."""
        length = random.randint(4, 12)
        width = random.randint(4, 12)
        area = length * width

        contexts = [
            (f"A rectangular garden is {length} feet long and {width} feet wide", "feet"),
            (f"A classroom carpet measures {length} meters by {width} meters", "meters"),
            (f"A parking space is {length} feet long and {width} feet wide", "feet"),
            (f"A rectangular poster is {length} inches long and {width} inches wide", "inches"),
            (f"A swimming pool is {length} meters long and {width} meters wide", "meters"),
            (f"A playground is {length} yards long and {width} yards wide", "yards"),
            (f"A picture frame is {length} inches by {width} inches", "inches")
        ]

        context, unit = random.choice(contexts)
        latex = f"\\text{{{context}. What is the area?}}"
        solution = f"{area} square {unit}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Area = length × width}}",
                f"\\text{{Area = }}{length} \\times {width}",
                f"\\text{{Area = {area} square {unit}}}"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: missing dimensions, comparisons, or multi-step."""
        problem_type = random.choice(['missing_dimension', 'comparison', 'multi_step'])

        if problem_type == 'missing_dimension':
            # Given area and one dimension, find the other
            area = random.randint(24, 96)
            known_side = random.choice([i for i in range(3, 13) if area % i == 0])
            missing_side = area // known_side

            dimension_known = random.choice(['length', 'width'])
            dimension_missing = 'width' if dimension_known == 'length' else 'length'

            latex = f"\\text{{A rectangle has an area of {area} square units. The {dimension_known} is {known_side} units. }}" + \
                    f"\\text{{Find the {dimension_missing}.}}"
            solution = f"{missing_side} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Area = {dimension_known} × {dimension_missing}}}",
                    f"{area} = {known_side} \\times \\text{{{dimension_missing}}}",
                    f"\\text{{{dimension_missing.capitalize()} = {area} ÷ {known_side} = {missing_side} units}}"
                ],
                difficulty='challenge'
            )

        elif problem_type == 'comparison':
            # Compare areas of two rectangles
            length1 = random.randint(5, 10)
            width1 = random.randint(4, 8)
            area1 = length1 * width1

            length2 = random.randint(5, 10)
            width2 = random.randint(4, 8)
            area2 = length2 * width2

            # Make sure they're different
            while area1 == area2:
                width2 = random.randint(4, 8)
                area2 = length2 * width2

            difference = abs(area1 - area2)

            latex = f"\\text{{Garden A: {length1} ft by {width1} ft. Garden B: {length2} ft by {width2} ft. }}" + \
                    f"\\text{{How much larger is the bigger garden?}}"
            solution = f"{difference} square feet"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Area A: {length1} × {width1} = {area1} sq ft}}",
                    f"\\text{{Area B: {length2} × {width2} = {area2} sq ft}}",
                    f"\\text{{Difference: {max(area1, area2)} - {min(area1, area2)} = {difference} sq ft}}"
                ],
                difficulty='challenge'
            )

        else:  # multi_step
            # Room with carpet and border
            room_length = random.randint(8, 12)
            room_width = random.randint(8, 12)
            room_area = room_length * room_width

            border = random.randint(1, 2)
            carpet_length = room_length - (2 * border)
            carpet_width = room_width - (2 * border)
            carpet_area = carpet_length * carpet_width

            latex = f"\\text{{A room is {room_length} ft by {room_width} ft. A carpet leaves a {border} ft border. }}" + \
                    f"\\text{{What is the carpet's area?}}"
            solution = f"{carpet_area} square feet"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Carpet length: {room_length} - (2 × {border}) = {carpet_length} ft}}",
                    f"\\text{{Carpet width: {room_width} - (2 × {border}) = {carpet_width} ft}}",
                    f"\\text{{Carpet area: {carpet_length} × {carpet_width} = {carpet_area} sq ft}}"
                ],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = MultiplyToFindAreaGenerator()

    print("Multiply to Find Area Generator - Grade 3 Unit 10\n")

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
