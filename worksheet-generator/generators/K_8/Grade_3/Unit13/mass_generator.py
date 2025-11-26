"""
Mass Generator - Grade 3 Unit 13
Generates problems for measuring mass in grams and kilograms
Focuses on conversions and comparing masses
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MassGenerator:
    """Generates mass measurement problems."""

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
        """Generate easy problems: reading mass measurements."""
        problem_type = random.choice(['identify', 'compare'])

        if problem_type == 'identify':
            # Choose appropriate unit for common objects
            objects_grams = ['paper clip', 'pencil', 'eraser', 'crayon', 'marker']
            objects_kilograms = ['textbook', 'backpack', 'watermelon', 'cat', 'dog']

            if random.choice([True, False]):
                obj = random.choice(objects_grams)
                mass = random.randint(1, 50)
                unit = 'grams'
            else:
                obj = random.choice(objects_kilograms)
                mass = random.randint(1, 10)
                unit = 'kilograms'

            latex = f"\\text{{A {obj} has a mass of {mass} {unit}. Write the mass with its unit.}}"
            solution = f"{mass} {unit}"

        else:  # compare
            mass1 = random.randint(10, 100)
            mass2 = random.randint(10, 100)
            while mass1 == mass2:
                mass2 = random.randint(10, 100)

            latex = f"\\text{{Which is heavier: {mass1} grams or {mass2} grams?}}"
            solution = f"{max(mass1, mass2)} grams"

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
            # Convert between grams and kilograms
            if random.choice([True, False]):
                # kg to g
                kg = random.randint(1, 10)
                grams = kg * 1000
                latex = f"\\text{{Convert {kg} kilograms to grams.}}"
                solution = f"{grams} grams"
                steps = [f"\\text{{{kg} kg = {kg} \\times 1000 = {grams} grams}}"]
            else:
                # g to kg
                kg = random.randint(2, 9)
                grams = kg * 1000
                latex = f"\\text{{Convert {grams} grams to kilograms.}}"
                solution = f"{kg} kilograms"
                steps = [f"\\text{{{grams} g = {grams} \\div 1000 = {kg} kilograms}}"]

        else:  # add
            mass1 = random.randint(100, 500)
            mass2 = random.randint(100, 500)
            total = mass1 + mass2

            objects = ['apple', 'orange', 'book', 'toy', 'box']
            obj1 = random.choice(objects)
            obj2 = random.choice([o for o in objects if o != obj1])

            latex = f"\\text{{A {obj1} has a mass of {mass1} grams and a {obj2} has a mass of {mass2} grams. What is their total mass?}}"
            solution = f"{total} grams"
            steps = [f"\\text{{{mass1} + {mass2} = {total} grams}}"]

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
            kg = random.randint(2, 8)
            extra_grams = random.randint(100, 900)
            total_grams = kg * 1000 + extra_grams

            objects = ['watermelon', 'pumpkin', 'bag of flour', 'turkey', 'puppy']
            obj = random.choice(objects)

            latex = f"\\text{{A {obj} has a mass of {kg} kilograms and {extra_grams} grams. What is its mass in grams?}}"
            solution = f"{total_grams} grams"
            steps = [
                f"\\text{{{kg} kg = {kg * 1000} grams}}",
                f"\\text{{{kg * 1000} + {extra_grams} = {total_grams} grams}}"
            ]

        else:  # multi_step
            mass1 = random.randint(200, 500)
            mass2 = random.randint(200, 500)
            mass3 = random.randint(200, 500)
            total = mass1 + mass2 + mass3

            latex = f"\\text{{A basket contains three fruits. An apple is {mass1} grams, an orange is {mass2} grams, and a banana is {mass3} grams. What is the total mass?}}"
            solution = f"{total} grams"
            steps = [f"\\text{{{mass1} + {mass2} + {mass3} = {total} grams}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex conversions or comparisons."""
        problem_type = random.choice(['mixed_conversion', 'comparison'])

        if problem_type == 'mixed_conversion':
            # Multiple objects with different units
            obj1_kg = random.randint(2, 5)
            obj2_g = random.randint(500, 900)
            total_g = obj1_kg * 1000 + obj2_g

            latex = f"\\text{{Box A has a mass of {obj1_kg} kilograms and Box B has a mass of {obj2_g} grams. What is their combined mass in grams?}}"
            solution = f"{total_g} grams"
            steps = [
                f"\\text{{Box A: {obj1_kg} kg = {obj1_kg * 1000} grams}}",
                f"\\text{{Total: {obj1_kg * 1000} + {obj2_g} = {total_g} grams}}"
            ]

        else:  # comparison
            # Compare mixed units
            mass1_kg = random.randint(3, 8)
            mass2_g = random.randint(2000, 9000)

            mass1_g = mass1_kg * 1000

            if mass1_g > mass2_g:
                heavier = f"{mass1_kg} kilograms"
                comparison = ">"
            elif mass1_g < mass2_g:
                heavier = f"{mass2_g} grams"
                comparison = "<"
            else:
                heavier = "They are equal"
                comparison = "="

            latex = f"\\text{{Which is heavier: {mass1_kg} kilograms or {mass2_g} grams?}}"
            solution = heavier
            steps = [
                f"\\text{{Convert to same units: {mass1_kg} kg = {mass1_g} grams}}",
                f"\\text{{{mass1_g} {comparison} {mass2_g}}}",
                f"\\text{{Heavier: {heavier}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MassGenerator()

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
