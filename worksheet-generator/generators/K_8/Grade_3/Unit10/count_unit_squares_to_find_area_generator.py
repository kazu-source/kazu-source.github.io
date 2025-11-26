"""
Count Unit Squares to Find Area Generator - Grade 3 Unit 10
Generates problems focused on counting unit squares to determine area
Example: Count the squares in a grid to find the area
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CountUnitSquaresToFindAreaGenerator:
    """Generates count unit squares to find area problems."""

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
        """Generate easy problems: small grids (2-4 units)."""
        length = random.randint(2, 4)
        width = random.randint(2, 4)
        area = length * width

        latex = f"\\text{{A rectangle has {length} rows and {width} unit squares in each row. }}" + \
                f"\\text{{How many unit squares in total?}}"
        solution = f"{area} square units"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Count the squares: {length} rows × {width} squares}}",
                f"{length} \\times {width} = {area}",
                f"\\text{{Area: {area} square units}}"
            ],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: larger grids (3-7 units)."""
        length = random.randint(3, 7)
        width = random.randint(3, 7)
        area = length * width

        descriptions = [
            f"a grid with {length} rows and {width} columns of unit squares",
            f"a rectangle divided into {length} by {width} unit squares",
            f"a shape containing {length} rows of {width} unit squares each"
        ]

        description = random.choice(descriptions)
        latex = f"\\text{{Find the area of {description}.}}"
        solution = f"{area} square units"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Count rows × columns}}",
                f"{length} \\times {width} = {area}",
                f"\\text{{Total: {area} square units}}"
            ],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with counting (4-10 units)."""
        length = random.randint(4, 10)
        width = random.randint(4, 10)
        area = length * width

        contexts = [
            f"A floor is covered with tiles arranged in {length} rows and {width} columns",
            f"A quilt has {length} rows with {width} square patches in each row",
            f"A chocolate bar has {length} rows and {width} squares in each row",
            f"A checkerboard section has {length} rows and {width} squares per row",
            f"A window has {length} rows of glass panes with {width} panes in each row"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}. How many unit squares are there?}}"
        solution = f"{area} square units"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Multiply rows × squares per row}}",
                f"{length} \\times {width} = {area}",
                f"\\text{{Total squares: {area}}}"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: partially filled grids or composite shapes."""
        problem_type = random.choice(['partial', 'L_shape'])

        if problem_type == 'partial':
            # Grid with some squares missing
            total_length = random.randint(6, 10)
            total_width = random.randint(6, 10)
            total_area = total_length * total_width

            missing_length = random.randint(2, 4)
            missing_width = random.randint(2, 4)
            missing_area = missing_length * missing_width

            actual_area = total_area - missing_area

            latex = f"\\text{{A {total_length} by {total_width} grid has a {missing_length} by {missing_width} section removed. }}" + \
                    f"\\text{{How many unit squares remain?}}"
            solution = f"{actual_area} square units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Total area: {total_length} × {total_width} = {total_area}}}",
                    f"\\text{{Removed area: {missing_length} × {missing_width} = {missing_area}}}",
                    f"\\text{{Remaining: {total_area} - {missing_area} = {actual_area} square units}}"
                ],
                difficulty='challenge'
            )
        else:
            # L-shaped figure
            # Horizontal part
            h_length = random.randint(6, 10)
            h_width = random.randint(3, 5)
            h_area = h_length * h_width

            # Vertical part (non-overlapping)
            v_length = random.randint(4, 7)
            v_width = random.randint(3, 5)
            v_area = v_length * v_width

            total_area = h_area + v_area

            latex = f"\\text{{An L-shaped figure has a horizontal section ({h_length} by {h_width}) }}" + \
                    f"\\text{{and a vertical section ({v_length} by {v_width}). Find the total area.}}"
            solution = f"{total_area} square units"

            return Equation(
                latex=latex,
                solution=solution,
                steps=[
                    f"\\text{{Horizontal area: {h_length} × {h_width} = {h_area}}}",
                    f"\\text{{Vertical area: {v_length} × {v_width} = {v_area}}}",
                    f"\\text{{Total area: {h_area} + {v_area} = {total_area} square units}}"
                ],
                difficulty='challenge'
            )


def main():
    """Test the generator."""
    generator = CountUnitSquaresToFindAreaGenerator()

    print("Count Unit Squares to Find Area Generator - Grade 3 Unit 10\n")

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
