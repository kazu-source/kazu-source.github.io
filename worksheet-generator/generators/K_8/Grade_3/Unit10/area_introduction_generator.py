"""
Area Introduction Generator - Grade 3 Unit 10
Generates problems focused on understanding the concept of area
Example: Visual representation of area with shaded regions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AreaIntroductionGenerator:
    """Generates area introduction problems."""

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
        """Generate easy problems: simple shapes with small dimensions (1-3 units)."""
        length = random.randint(1, 3)
        width = random.randint(1, 3)
        area = length * width

        shapes = [
            f"a rectangle that is {length} units long and {width} units wide",
            f"a shape with {length} rows and {width} squares in each row"
        ]

        shape = random.choice(shapes)
        latex = f"\\text{{What is the area of {shape}?}}"
        solution = f"{area} square units"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Length: {length} units}}",
                f"\\text{{Width: {width} units}}",
                f"\\text{{Area: {length} × {width} = {area} square units}}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: larger shapes (1-5 units)."""
        length = random.randint(2, 5)
        width = random.randint(2, 5)
        area = length * width

        shapes = [
            f"a rectangle with length {length} units and width {width} units",
            f"a rug that measures {length} units by {width} units",
            f"a poster that is {length} units tall and {width} units wide"
        ]

        shape = random.choice(shapes)
        latex = f"\\text{{Find the area of {shape}.}}"
        solution = f"{area} square units"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Multiply length × width}}",
                f"{length} \\times {width} = {area}",
                f"\\text{{Area: {area} square units}}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with real-world contexts (1-8 units)."""
        length = random.randint(3, 8)
        width = random.randint(3, 8)
        area = length * width

        contexts = [
            (f"A garden is {length} feet long and {width} feet wide", "feet"),
            (f"A classroom floor measures {length} meters by {width} meters", "meters"),
            (f"A painting is {length} inches long and {width} inches wide", "inches"),
            (f"A sandbox is {length} feet by {width} feet", "feet"),
            (f"A table top is {length} feet long and {width} feet wide", "feet")
        ]

        context, unit = random.choice(contexts)
        latex = f"\\text{{{context}. What is its area?}}"
        solution = f"{area} square {unit}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Find length × width}}",
                f"{length} \\times {width} = {area}",
                f"\\text{{Area: {area} square {unit}}}"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: comparing areas or finding missing dimensions."""
        problem_type = random.choice(['compare', 'missing_dimension'])

        if problem_type == 'compare':
            # Compare two rectangles
            length1 = random.randint(4, 8)
            width1 = random.randint(3, 6)
            area1 = length1 * width1

            length2 = random.randint(4, 8)
            width2 = random.randint(3, 6)
            area2 = length2 * width2

            difference = abs(area1 - area2)

            latex = f"\\text{{Rectangle A: {length1} by {width1} units. Rectangle B: {length2} by {width2} units. }}" + \
                    f"\\text{{How much larger is the bigger rectangle's area?}}"
            solution = f"{difference} square units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Area A: {length1} × {width1} = {area1} square units}}",
                    f"\\text{{Area B: {length2} × {width2} = {area2} square units}}",
                    f"\\text{{Difference: {max(area1, area2)} - {min(area1, area2)} = {difference} square units}}"
                ],
                difficulty='challenge'
            )
        else:
            # Missing dimension
            area = random.randint(12, 48)
            known_side = random.choice([i for i in range(2, 13) if area % i == 0])
            missing_side = area // known_side

            dimension = random.choice(['length', 'width'])
            other_dimension = 'width' if dimension == 'length' else 'length'

            latex = f"\\text{{A rectangle has an area of {area} square units. Its {other_dimension} is {known_side} units. }}" + \
                    f"\\text{{What is its {dimension}?}}"
            solution = f"{missing_side} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Area = {dimension} × {other_dimension}}}",
                    f"{area} = {dimension} \\times {known_side}",
                    f"\\text{{{dimension.capitalize()} = {area} ÷ {known_side} = {missing_side} units}}"
                ],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = AreaIntroductionGenerator()

    print("Area Introduction Generator - Grade 3 Unit 10\n")

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
