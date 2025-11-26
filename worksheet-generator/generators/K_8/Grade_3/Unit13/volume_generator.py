"""
Volume Generator - Grade 3 Unit 13
Generates problems for measuring volume in liters and milliliters
Focuses on conversions and comparing volumes
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class VolumeGenerator:
    """Generates volume measurement problems."""

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
        """Generate easy problems: reading volume measurements."""
        problem_type = random.choice(['identify', 'compare'])

        if problem_type == 'identify':
            # Choose appropriate unit for common liquids
            liquids_ml = ['medicine', 'eyedrops', 'perfume', 'food coloring']
            liquids_l = ['milk', 'water bottle', 'juice', 'soda', 'soup']

            if random.choice([True, False]):
                liquid = random.choice(liquids_ml)
                volume = random.randint(5, 100)
                unit = 'milliliters'
            else:
                liquid = random.choice(liquids_l)
                volume = random.randint(1, 5)
                unit = 'liters'

            latex = f"\\text{{A bottle of {liquid} contains {volume} {unit}. Write the volume with its unit.}}"
            solution = f"{volume} {unit}"

        else:  # compare
            volume1 = random.randint(100, 900)
            volume2 = random.randint(100, 900)
            while volume1 == volume2:
                volume2 = random.randint(100, 900)

            latex = f"\\text{{Which holds more: {volume1} milliliters or {volume2} milliliters?}}"
            solution = f"{max(volume1, volume2)} milliliters"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Answer: {solution}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: simple conversions and addition."""
        problem_type = random.choice(['convert', 'add'])

        if problem_type == 'convert':
            # Convert between liters and milliliters
            if random.choice([True, False]):
                # liters to ml
                liters = random.randint(1, 10)
                ml = liters * 1000
                latex = f"\\text{{Convert {liters} liters to milliliters.}}"
                solution = f"{ml} milliliters"
                steps = [f"\\text{{{liters} L = {liters} \\times 1000 = {ml} milliliters}}"]
            else:
                # ml to liters
                liters = random.randint(2, 9)
                ml = liters * 1000
                latex = f"\\text{{Convert {ml} milliliters to liters.}}"
                solution = f"{liters} liters"
                steps = [f"\\text{{{ml} mL = {ml} \\div 1000 = {liters} liters}}"]

        else:  # add
            volume1 = random.randint(100, 500)
            volume2 = random.randint(100, 500)
            total = volume1 + volume2

            containers = ['cup', 'glass', 'bottle', 'jar', 'container']
            container1 = random.choice(containers)
            container2 = random.choice([c for c in containers if c != container1])

            latex = f"\\text{{A {container1} holds {volume1} milliliters and a {container2} holds {volume2} milliliters. What is the total volume?}}"
            solution = f"{total} milliliters"
            steps = [f"\\text{{{volume1} + {volume2} = {total} milliliters}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: word problems with conversions or multi-step."""
        problem_type = random.choice(['conversion_word', 'multi_step'])

        if problem_type == 'conversion_word':
            liters = random.randint(2, 8)
            extra_ml = random.randint(100, 900)
            total_ml = liters * 1000 + extra_ml

            containers = ['juice pitcher', 'water jug', 'milk container', 'aquarium', 'bucket']
            container = random.choice(containers)

            latex = f"\\text{{A {container} holds {liters} liters and {extra_ml} milliliters. What is its volume in milliliters?}}"
            solution = f"{total_ml} milliliters"
            steps = [
                f"\\text{{{liters} L = {liters * 1000} milliliters}}",
                f"\\text{{{liters * 1000} + {extra_ml} = {total_ml} milliliters}}"
            ]

        else:  # multi_step
            volume1 = random.randint(200, 500)
            volume2 = random.randint(200, 500)
            volume3 = random.randint(200, 500)
            total = volume1 + volume2 + volume3

            latex = f"\\text{{A recipe uses {volume1} mL of water, {volume2} mL of milk, and {volume3} mL of juice. What is the total volume of liquid?}}"
            solution = f"{total} milliliters"
            steps = [f"\\text{{{volume1} + {volume2} + {volume3} = {total} milliliters}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex conversions or comparisons."""
        problem_type = random.choice(['mixed_conversion', 'comparison', 'subtraction'])

        if problem_type == 'mixed_conversion':
            # Multiple containers with different units
            container1_l = random.randint(2, 5)
            container2_ml = random.randint(500, 900)
            total_ml = container1_l * 1000 + container2_ml

            latex = f"\\text{{Container A holds {container1_l} liters and Container B holds {container2_ml} milliliters. What is their combined volume in milliliters?}}"
            solution = f"{total_ml} milliliters"
            steps = [
                f"\\text{{Container A: {container1_l} L = {container1_l * 1000} milliliters}}",
                f"\\text{{Total: {container1_l * 1000} + {container2_ml} = {total_ml} milliliters}}"
            ]

        elif problem_type == 'comparison':
            # Compare mixed units
            volume1_l = random.randint(3, 8)
            volume2_ml = random.randint(2000, 9000)

            volume1_ml = volume1_l * 1000

            if volume1_ml > volume2_ml:
                more = f"{volume1_l} liters"
                comparison = ">"
            elif volume1_ml < volume2_ml:
                more = f"{volume2_ml} milliliters"
                comparison = "<"
            else:
                more = "They are equal"
                comparison = "="

            latex = f"\\text{{Which holds more: {volume1_l} liters or {volume2_ml} milliliters?}}"
            solution = more
            steps = [
                f"\\text{{Convert to same units: {volume1_l} L = {volume1_ml} milliliters}}",
                f"\\text{{{volume1_ml} {comparison} {volume2_ml}}}",
                f"\\text{{More: {more}}}"
            ]

        else:  # subtraction
            total_ml = random.randint(3000, 8000)
            used_ml = random.randint(500, 2000)
            remaining_ml = total_ml - used_ml

            latex = f"\\text{{A tank contains {total_ml} milliliters of water. If {used_ml} milliliters are used, how much water remains?}}"
            solution = f"{remaining_ml} milliliters"
            steps = [f"\\text{{{total_ml} - {used_ml} = {remaining_ml} milliliters}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = VolumeGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
