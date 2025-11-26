"""
Multiplication as Groups of Objects Generator - Grade 3 Unit 1
Generates problems focused on understanding multiplication through grouping physical objects
Example: 4 groups of 3 objects = 4 × 3 = 12 objects
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class MultiplicationAsGroupsOfObjectsGenerator:
    """Generates multiplication as groups of objects problems."""

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
        """Generate easy problems: 2-5 objects per group, 2-5 groups."""
        num_groups = random.randint(2, 5)
        objects_per_group = random.randint(2, 5)
        product = num_groups * objects_per_group

        latex = f"{num_groups} \\times {objects_per_group}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num_groups} \\text{{ groups of }} {objects_per_group} \\text{{ objects}} = {product}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: 2-10 objects per group, 2-10 groups."""
        num_groups = random.randint(2, 10)
        objects_per_group = random.randint(2, 10)
        product = num_groups * objects_per_group

        latex = f"{num_groups} \\times {objects_per_group}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num_groups} \\text{{ groups of }} {objects_per_group} \\text{{ objects}} = {product}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: include word problems with context (toys, pencils, crayons, etc.)."""
        num_groups = random.randint(3, 10)
        objects_per_group = random.randint(3, 10)
        product = num_groups * objects_per_group

        objects = [
            ("toys", "toy"),
            ("pencils", "pencil"),
            ("crayons", "crayon"),
            ("marbles", "marble"),
            ("stickers", "sticker"),
            ("blocks", "block"),
            ("cars", "car"),
            ("dolls", "doll")
        ]

        obj_plural, obj_singular = random.choice(objects)
        object_name = obj_plural if objects_per_group > 1 else obj_singular

        contexts = [
            f"There are {num_groups} boxes with {objects_per_group} {object_name} in each box",
            f"A student has {num_groups} groups of {objects_per_group} {object_name}",
            f"The store has {num_groups} packs with {objects_per_group} {object_name} in each pack",
            f"There are {num_groups} bags containing {objects_per_group} {object_name} each"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}. How many in total?}}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num_groups} \\times {objects_per_group} = {product}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: larger numbers (5-12) with word problems."""
        num_groups = random.randint(5, 12)
        objects_per_group = random.randint(5, 12)
        product = num_groups * objects_per_group

        objects = [
            ("toys", "toy"),
            ("pencils", "pencil"),
            ("crayons", "crayon"),
            ("marbles", "marble"),
            ("stickers", "sticker"),
            ("blocks", "block"),
            ("cards", "card"),
            ("coins", "coin"),
            ("buttons", "button"),
            ("beads", "bead")
        ]

        obj_plural, obj_singular = random.choice(objects)
        object_name = obj_plural if objects_per_group > 1 else obj_singular

        contexts = [
            f"A teacher bought {num_groups} containers with {objects_per_group} {object_name} in each container",
            f"There are {num_groups} classrooms with {objects_per_group} {object_name} in each classroom",
            f"A collector has {num_groups} albums with {objects_per_group} {object_name} in each album",
            f"The art room has {num_groups} bins with {objects_per_group} {object_name} in each bin",
            f"A store displays {num_groups} shelves with {objects_per_group} {object_name} on each shelf"
        ]

        context = random.choice(contexts)
        latex = f"\\text{{{context}. How many {obj_plural} are there in total?}}"
        solution = str(product)

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"{num_groups} \\times {objects_per_group} = {product}"],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = MultiplicationAsGroupsOfObjectsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
        print(f"  Steps: {problem.steps}")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")
        print(f"  Steps: {problem.steps}")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print(f"  Steps: {problem.steps}")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}")
        print(f"  Steps: {problem.steps}")


if __name__ == '__main__':
    main()
