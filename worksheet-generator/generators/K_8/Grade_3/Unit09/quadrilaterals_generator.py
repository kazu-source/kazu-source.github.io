"""
Quadrilaterals Generator - Grade 3 Unit 09
Generates problems focused on identification, analysis, and classification of quadrilaterals
Covers: squares, rectangles, rhombuses, parallelograms, trapezoids
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class QuadrilateralsGenerator:
    """Generates quadrilateral identification and classification problems."""

    QUADRILATERALS = {
        'square': {
            'sides': '4 equal sides',
            'angles': '4 right angles (90°)',
            'properties': ['All sides are equal', 'All angles are 90°', 'Opposite sides are parallel'],
            'is_rectangle': True,
            'is_rhombus': True,
            'is_parallelogram': True
        },
        'rectangle': {
            'sides': '2 pairs of equal sides',
            'angles': '4 right angles (90°)',
            'properties': ['Opposite sides are equal', 'All angles are 90°', 'Opposite sides are parallel'],
            'is_rectangle': True,
            'is_rhombus': False,
            'is_parallelogram': True
        },
        'rhombus': {
            'sides': '4 equal sides',
            'angles': '2 pairs of equal angles',
            'properties': ['All sides are equal', 'Opposite angles are equal', 'Opposite sides are parallel'],
            'is_rectangle': False,
            'is_rhombus': True,
            'is_parallelogram': True
        },
        'parallelogram': {
            'sides': '2 pairs of equal sides',
            'angles': '2 pairs of equal angles',
            'properties': ['Opposite sides are equal', 'Opposite angles are equal', 'Opposite sides are parallel'],
            'is_rectangle': False,
            'is_rhombus': False,
            'is_parallelogram': True
        },
        'trapezoid': {
            'sides': '4 sides (may be different lengths)',
            'angles': '4 angles',
            'properties': ['Exactly one pair of parallel sides', 'Non-parallel sides are called legs'],
            'is_rectangle': False,
            'is_rhombus': False,
            'is_parallelogram': False
        }
    }

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
        """Generate easy problems: basic identification of common quadrilaterals."""
        problem_type = random.choice(['identify', 'sides', 'angles'])
        shape = random.choice(['square', 'rectangle'])
        info = self.QUADRILATERALS[shape]

        if problem_type == 'identify':
            if shape == 'square':
                latex = "\\text{I have 4 equal sides and 4 right angles. What shape am I?}"
            else:
                latex = "\\text{I have 2 pairs of equal sides and 4 right angles. What shape am I?}"
            solution = shape.capitalize()
            steps = [f"\\text{{A {shape} has {info['sides']} and {info['angles']}}}"]

        elif problem_type == 'sides':
            latex = f"\\text{{How many sides does a {shape} have?}}"
            solution = "4"
            steps = [f"\\text{{All quadrilaterals have 4 sides}}"]

        else:  # angles
            latex = f"\\text{{A {shape} has how many right angles?}}"
            solution = "4"
            steps = [f"\\text{{A {shape} has 4 right angles (90° each)}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: properties and more quadrilateral types."""
        problem_type = random.choice(['identify', 'property', 'true_false'])
        shape = random.choice(['square', 'rectangle', 'rhombus', 'parallelogram'])
        info = self.QUADRILATERALS[shape]

        if problem_type == 'identify':
            descriptions = {
                'square': "4 equal sides and 4 right angles",
                'rectangle': "opposite sides equal and 4 right angles, but sides are not all equal",
                'rhombus': "4 equal sides but the angles are not all right angles",
                'parallelogram': "opposite sides equal and parallel, but no right angles"
            }
            latex = f"\\text{{What quadrilateral has {descriptions[shape]}?}}"
            solution = shape.capitalize()
            steps = [f"\\text{{A {shape} has these properties: {info['sides']}, {info['angles']}}}"]

        elif problem_type == 'property':
            prop = random.choice(info['properties'])
            latex = f"\\text{{Name a property of a {shape}.}}"
            solution = prop
            steps = [f"\\text{{Properties of a {shape}:}}"] + [f"\\text{{- {p}}}" for p in info['properties']]

        else:  # true_false
            shape2 = random.choice(['square', 'rectangle', 'rhombus', 'parallelogram'])
            info2 = self.QUADRILATERALS[shape2]

            statements = [
                (f"A {shape2} has 4 sides", "True"),
                (f"A square has 4 equal sides", "True"),
                (f"A rectangle always has 4 equal sides", "False"),
                (f"A rhombus has 4 equal sides", "True"),
                (f"All angles in a rectangle are right angles", "True"),
                (f"A parallelogram always has right angles", "False")
            ]
            statement, answer = random.choice(statements)
            latex = f"\\text{{True or False: {statement}}}"
            solution = answer
            steps = [f"\\text{{This statement is {answer.lower()}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: classification and relationships between shapes."""
        problem_type = random.choice(['classify', 'compare', 'relationship'])

        if problem_type == 'classify':
            shape = random.choice(list(self.QUADRILATERALS.keys()))
            info = self.QUADRILATERALS[shape]

            questions = [
                (f"Is a {shape} a parallelogram?", "Yes" if info['is_parallelogram'] else "No"),
                (f"Is a {shape} a type of rectangle?", "Yes" if info['is_rectangle'] else "No"),
                (f"Is a {shape} a type of rhombus?", "Yes" if info['is_rhombus'] else "No"),
            ]
            question, answer = random.choice(questions)
            latex = f"\\text{{{question}}}"
            solution = answer

            if answer == "Yes":
                steps = [f"\\text{{Yes, a {shape} has all the properties needed}}"]
            else:
                steps = [f"\\text{{No, a {shape} does not have all required properties}}"]

        elif problem_type == 'compare':
            shape1, shape2 = random.sample(['square', 'rectangle', 'rhombus', 'parallelogram'], 2)

            latex = f"\\text{{What do a {shape1} and a {shape2} have in common?}}"

            common = []
            if self.QUADRILATERALS[shape1]['is_parallelogram'] and self.QUADRILATERALS[shape2]['is_parallelogram']:
                common.append("Both have opposite sides parallel")
                common.append("Both have opposite sides equal")
            common.append("Both have 4 sides")
            common.append("Both are quadrilaterals")

            solution = random.choice(common)
            steps = [f"\\text{{Common properties:}}"] + [f"\\text{{- {c}}}" for c in common]

        else:  # relationship
            relationships = [
                ("Every square is a rectangle", "True", "A square has all properties of a rectangle plus equal sides"),
                ("Every rectangle is a square", "False", "A rectangle doesn't need all sides equal"),
                ("Every square is a rhombus", "True", "A square has 4 equal sides like a rhombus"),
                ("Every rhombus is a square", "False", "A rhombus doesn't need right angles"),
                ("Every rectangle is a parallelogram", "True", "A rectangle has parallel opposite sides"),
                ("Every parallelogram is a rectangle", "False", "A parallelogram doesn't need right angles")
            ]
            statement, answer, explanation = random.choice(relationships)
            latex = f"\\text{{True or False: {statement}}}"
            solution = answer
            steps = [f"\\text{{{explanation}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex classification and analysis."""
        problem_type = random.choice(['hierarchy', 'counterexample', 'all_that_apply'])

        if problem_type == 'hierarchy':
            latex = "\\text{Which shape is the most specific: quadrilateral, parallelogram, rectangle, or square?}"
            solution = "Square"
            steps = [
                "\\text{Quadrilateral: any 4-sided shape}",
                "\\text{Parallelogram: quadrilateral with parallel opposite sides}",
                "\\text{Rectangle: parallelogram with right angles}",
                "\\text{Square: rectangle with all sides equal (most specific)}"
            ]

        elif problem_type == 'counterexample':
            statements = [
                ("If a shape has 4 right angles, it must be a square",
                 "False - a rectangle has 4 right angles but isn't always a square",
                 "Rectangle (that isn't a square)"),
                ("If a shape has 4 equal sides, it must be a square",
                 "False - a rhombus has 4 equal sides but isn't always a square",
                 "Rhombus (that isn't a square)"),
                ("All parallelograms have right angles",
                 "False - a rhombus is a parallelogram without right angles",
                 "Rhombus or general parallelogram")
            ]
            statement, answer, counterexample = random.choice(statements)
            latex = f"\\text{{{statement}. If false, give a counterexample.}}"
            solution = f"False. Counterexample: {counterexample}"
            steps = [f"\\text{{{answer}}}"]

        else:  # all_that_apply
            shape = random.choice(['square', 'rectangle', 'rhombus'])
            categories = []
            info = self.QUADRILATERALS[shape]

            if info['is_parallelogram']:
                categories.append('parallelogram')
            if info['is_rectangle']:
                categories.append('rectangle')
            if info['is_rhombus']:
                categories.append('rhombus')
            categories.append('quadrilateral')

            latex = f"\\text{{A {shape} is also a: (select all that apply)}}" + \
                    "\\text{{ quadrilateral, parallelogram, rectangle, rhombus}}"
            solution = ", ".join(categories)
            steps = [f"\\text{{A {shape} belongs to these categories: {', '.join(categories)}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = QuadrilateralsGenerator()

    print("Quadrilaterals Generator - Grade 3 Unit 09\n")

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
