"""
Perimeter Generator - Grade 3 Unit 11
Generates problems for finding perimeter by adding all sides
Example: Find the perimeter of a rectangle with sides 5, 3, 5, 3
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PerimeterGenerator:
    """Generates perimeter problems."""

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
        """Generate easy problems: squares and simple rectangles (1-5 units)."""
        shape_type = random.choice(['square', 'rectangle'])

        if shape_type == 'square':
            side = random.randint(2, 5)
            perimeter = 4 * side

            latex = f"\\text{{Find the perimeter of a square with side length {side} units.}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{All sides equal: {side} units}}",
                    f"\\text{{Perimeter = {side} + {side} + {side} + {side}}}",
                    f"\\text{{Perimeter = {perimeter} units}}"
                ],
                difficulty='easy'
            )
        else:
            length = random.randint(3, 5)
            width = random.randint(2, 4)
            perimeter = 2 * (length + width)

            latex = f"\\text{{Find the perimeter of a rectangle: length = {length} units, width = {width} units.}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Add all sides: {length} + {width} + {length} + {width}}}",
                    f"{length} + {width} + {length} + {width} = {perimeter}",
                    f"\\text{{Perimeter = {perimeter} units}}"
                ],
                difficulty='easy'
            )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: various shapes (2-10 units)."""
        shape_type = random.choice(['square', 'rectangle', 'triangle'])

        if shape_type == 'square':
            side = random.randint(4, 10)
            perimeter = 4 * side

            latex = f"\\text{{A square has sides of {side} units. Find the perimeter.}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter = 4 × side}}",
                    f"\\text{{Perimeter = 4 × {side}}}",
                    f"\\text{{Perimeter = {perimeter} units}}"
                ],
                difficulty='medium'
            )

        elif shape_type == 'rectangle':
            length = random.randint(5, 10)
            width = random.randint(3, 8)
            perimeter = 2 * (length + width)

            latex = f"\\text{{A rectangle measures {length} units by {width} units. Find the perimeter.}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter = 2 × (length + width)}}",
                    f"\\text{{Perimeter = 2 × ({length} + {width})}}",
                    f"\\text{{Perimeter = 2 × {length + width} = {perimeter} units}}"
                ],
                difficulty='medium'
            )

        else:  # triangle
            side1 = random.randint(3, 10)
            side2 = random.randint(3, 10)
            side3 = random.randint(3, 10)
            perimeter = side1 + side2 + side3

            latex = f"\\text{{A triangle has sides {side1}, {side2}, and {side3} units. Find the perimeter.}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Add all three sides}}",
                    f"{side1} + {side2} + {side3} = {perimeter}",
                    f"\\text{{Perimeter = {perimeter} units}}"
                ],
                difficulty='medium'
            )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with real-world contexts."""
        shape_type = random.choice(['square', 'rectangle', 'triangle', 'polygon'])

        if shape_type == 'square':
            side = random.randint(5, 12)
            perimeter = 4 * side

            contexts = [
                f"A square garden has sides of {side} feet",
                f"A square tile measures {side} inches on each side",
                f"A square playground is {side} meters per side"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}. What is the perimeter?}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter = 4 × {side}}}",
                    f"\\text{{Perimeter = {perimeter} units}}"
                ],
                difficulty='hard'
            )

        elif shape_type == 'rectangle':
            length = random.randint(6, 12)
            width = random.randint(4, 10)
            perimeter = 2 * (length + width)

            contexts = [
                f"A rectangular room is {length} feet long and {width} feet wide",
                f"A picture frame measures {length} inches by {width} inches",
                f"A rectangular pool is {length} meters by {width} meters",
                f"A fence surrounds a yard that is {length} yards long and {width} yards wide"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}. Find the perimeter.}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter = 2 × ({length} + {width})}}",
                    f"\\text{{Perimeter = 2 × {length + width} = {perimeter} units}}"
                ],
                difficulty='hard'
            )

        elif shape_type == 'triangle':
            side1 = random.randint(5, 12)
            side2 = random.randint(5, 12)
            side3 = random.randint(5, 12)
            perimeter = side1 + side2 + side3

            contexts = [
                f"A triangular garden has sides of {side1} ft, {side2} ft, and {side3} ft",
                f"A triangular flag has sides measuring {side1}, {side2}, and {side3} inches"
            ]

            context = random.choice(contexts)
            latex = f"\\text{{{context}. What is the perimeter?}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"{side1} + {side2} + {side3} = {perimeter}",
                    f"\\text{{Perimeter = {perimeter} units}}"
                ],
                difficulty='hard'
            )

        else:  # polygon
            num_sides = random.randint(5, 6)
            side_length = random.randint(4, 10)
            perimeter = num_sides * side_length

            shape_name = "pentagon" if num_sides == 5 else "hexagon"

            latex = f"\\text{{A regular {shape_name} has sides of {side_length} units. Find the perimeter.}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter = {num_sides} × {side_length}}}",
                    f"\\text{{Perimeter = {perimeter} units}}"
                ],
                difficulty='hard'
            )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: missing side, composite shapes, or comparisons."""
        problem_type = random.choice(['missing_side', 'composite', 'comparison'])

        if problem_type == 'missing_side':
            # Given perimeter and some sides, find missing side
            shape_type = random.choice(['rectangle', 'triangle'])

            if shape_type == 'rectangle':
                length = random.randint(6, 12)
                width = random.randint(4, 10)
                perimeter = 2 * (length + width)

                given_dimension = random.choice(['length', 'width'])
                known_side = length if given_dimension == 'length' else width
                missing_side = width if given_dimension == 'length' else length

                latex = f"\\text{{A rectangle has a perimeter of {perimeter} units. The {given_dimension} is {known_side} units. }}" + \
                        f"\\text{{Find the other dimension.}}"
                solution = f"{missing_side} units"

                return Equation(
                    latex=latex,
                    solution=solution,
                    steps=[
                        f"\\text{{Perimeter = 2 × (length + width)}}",
                        f"{perimeter} = 2 × ({known_side} + \\text{{missing}})}}",
                        f"{perimeter // 2} = {known_side} + \\text{{missing}}",
                        f"\\text{{Missing dimension = {perimeter // 2} - {known_side} = {missing_side} units}}"
                    ],
                    difficulty='challenge'
                )

            else:  # triangle
                side1 = random.randint(5, 10)
                side2 = random.randint(5, 10)
                side3 = random.randint(5, 10)
                perimeter = side1 + side2 + side3

                latex = f"\\text{{A triangle has a perimeter of {perimeter} units. Two sides are {side1} and {side2} units. }}" + \
                        f"\\text{{Find the third side.}}"
                solution = f"{side3} units"

                return Equation(
                    latex=latex,
                    solution=solution,
                    steps=[
                        f"\\text{{Perimeter = side1 + side2 + side3}}",
                        f"{perimeter} = {side1} + {side2} + \\text{{side3}}",
                        f"\\text{{Side3 = {perimeter} - {side1} - {side2} = {side3} units}}"
                    ],
                    difficulty='challenge'
                )

        elif problem_type == 'composite':
            # L-shaped or other composite figure
            # Horizontal part
            h_length = random.randint(8, 12)
            h_width = random.randint(3, 5)

            # Vertical extension
            v_height = random.randint(4, 8)
            v_width = random.randint(3, 5)

            # Calculate perimeter (going around the outside)
            # This is simplified - actual perimeter depends on configuration
            perimeter = h_length + h_width + v_height + v_width + (h_length - v_width) + (h_width + v_height)

            latex = f"\\text{{An L-shaped figure has a horizontal part ({h_length} by {h_width}) }}" + \
                    f"\\text{{and a vertical part ({v_width} by {v_height}). Find the perimeter.}}"
            solution = f"{perimeter} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Count all outside edges}}",
                    f"\\text{{Add: {h_length} + {h_width} + {v_height} + {v_width} + {h_length - v_width} + {h_width + v_height}}}",
                    f"\\text{{Perimeter = {perimeter} units}}"
                ],
                difficulty='challenge'
            )

        else:  # comparison
            # Compare perimeters
            length1 = random.randint(6, 10)
            width1 = random.randint(4, 8)
            perimeter1 = 2 * (length1 + width1)

            length2 = random.randint(6, 10)
            width2 = random.randint(4, 8)
            perimeter2 = 2 * (length2 + width2)

            # Ensure they're different
            while perimeter1 == perimeter2:
                width2 = random.randint(4, 8)
                perimeter2 = 2 * (length2 + width2)

            difference = abs(perimeter1 - perimeter2)

            latex = f"\\text{{Field A: {length1} by {width1} units. Field B: {length2} by {width2} units. }}" + \
                    f"\\text{{How much more fence is needed for the larger field?}}"
            solution = f"{difference} units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Perimeter A: 2 × ({length1} + {width1}) = {perimeter1}}}",
                    f"\\text{{Perimeter B: 2 × ({length2} + {width2}) = {perimeter2}}}",
                    f"\\text{{Difference: {max(perimeter1, perimeter2)} - {min(perimeter1, perimeter2)} = {difference} units}}"
                ],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = PerimeterGenerator()

    print("Perimeter Generator - Grade 3 Unit 11\n")

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
