"""
Dilation Preserved Properties Generator
Creates problems about which properties are preserved under dilations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class DilationPreservedPropertiesGenerator:
    """Generates problems about properties preserved under dilations."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Basic property recognition"""
        properties = [
            ("angle measures", "Yes", "Dilations preserve angle measures."),
            ("side lengths", "No", "Dilations change side lengths by the scale factor."),
            ("parallel lines", "Yes", "Dilations preserve parallelism."),
            ("collinearity", "Yes", "Dilations preserve collinearity (points on a line stay on a line)."),
            ("betweenness", "Yes", "If B is between A and C, it remains between after dilation."),
            ("orientation", "Yes", "Dilations preserve the orientation of figures."),
            ("perimeter", "No", "Perimeter is multiplied by the scale factor."),
            ("area", "No", "Area is multiplied by the square of the scale factor.")
        ]

        prop, answer, explanation = random.choice(properties)

        latex = f"\\text{{Are }} {prop} \\text{{ preserved under dilations?}}"
        solution = answer

        steps = [
            f"\\text{{{explanation}}}",
            f"\\text{{Answer: {answer}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Apply scale factor to lengths and areas"""
        problem_type = random.choice(['length', 'perimeter', 'area', 'angle'])

        if problem_type == 'length':
            k = random.choice([2, 3, 4, 1/2, 1/3, 1/4, 0.5])
            length = random.randint(4, 20)
            new_length = length * k

            latex = f"\\text{{A segment of length }} {length} \\text{{ is dilated with scale factor }} k = {k}. \\text{{ What is the new length?}}"
            solution = str(new_length)

            steps = [
                f"\\text{{Under dilation, lengths are multiplied by the scale factor}}",
                f"\\text{{New length}} = {length} \\times {k} = {new_length}"
            ]

        elif problem_type == 'perimeter':
            k = random.choice([2, 3, 4, 0.5])
            perimeter = random.randint(12, 36)
            new_perimeter = perimeter * k

            latex = f"\\text{{A triangle with perimeter }} {perimeter} \\text{{ is dilated with scale factor }} k = {k}. \\text{{ What is the new perimeter?}}"
            solution = str(new_perimeter)

            steps = [
                f"\\text{{Perimeter is multiplied by the scale factor}}",
                f"\\text{{New perimeter}} = {perimeter} \\times {k} = {new_perimeter}"
            ]

        elif problem_type == 'area':
            k = random.choice([2, 3, 0.5])
            area = random.randint(8, 48)
            new_area = area * k * k

            latex = f"\\text{{A rectangle with area }} {area} \\text{{ is dilated with scale factor }} k = {k}. \\text{{ What is the new area?}}"
            solution = str(new_area)

            steps = [
                f"\\text{{Area is multiplied by the square of the scale factor}}",
                f"\\text{{New area}} = {area} \\times {k}^2 = {area} \\times {k * k} = {new_area}"
            ]

        else:  # angle
            angle = random.randint(30, 150)

            latex = f"\\text{{An angle measuring }} {angle}^\\circ \\text{{ is part of a figure dilated with scale factor }} k = 3. \\text{{ What is the angle measure after dilation?}}"
            solution = f"{angle}°"

            steps = [
                f"\\text{{Angle measures are preserved under dilations}}",
                f"\\text{{The angle remains }} {angle}^\\circ"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Find scale factor given before and after measurements"""
        problem_type = random.choice(['find_k_length', 'find_k_area', 'ratio'])

        if problem_type == 'find_k_length':
            k = random.choice([2, 3, 4, 0.5])
            original = random.randint(5, 15)
            new = original * k

            latex = f"\\text{{A segment of length }} {original} \\text{{ is dilated to length }} {new}. \\text{{ What is the scale factor?}}"
            solution = str(k)

            steps = [
                f"\\text{{Scale factor}} = \\frac{{\\text{{new length}}}}{{\\text{{original length}}}}",
                f"k = \\frac{{{new}}}{{{original}}} = {k}"
            ]

        elif problem_type == 'find_k_area':
            k = random.choice([2, 3])
            original_area = random.randint(8, 24)
            new_area = original_area * k * k

            latex = f"\\text{{A triangle with area }} {original_area} \\text{{ is dilated to area }} {new_area}. \\text{{ What is the scale factor?}}"
            solution = str(k)

            steps = [
                f"\\text{{If area is multiplied by }} {k * k}, \\text{{ then }} k^2 = {k * k}",
                f"k = \\sqrt{{{k * k}}} = {k}"
            ]

        else:  # ratio
            k = random.choice([2, 3, 4])
            ratio = k

            latex = f"\\text{{After a dilation with scale factor }} k = {k}, \\text{{ what is the ratio of the new perimeter to the original perimeter?}}"
            solution = f"{ratio}:1"

            steps = [
                f"\\text{{Perimeter is multiplied by the scale factor}}",
                f"\\text{{Ratio}} = {ratio} : 1"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex problems involving multiple properties"""
        problem_type = random.choice(['volume', 'similarity', 'composition'])

        if problem_type == 'volume':
            k = random.choice([2, 3])
            volume = random.randint(8, 27)
            new_volume = volume * k * k * k

            latex = f"\\text{{A cube with volume }} {volume} \\text{{ cubic units is dilated with scale factor }} k = {k}. \\text{{ What is the new volume?}}"
            solution = f"{new_volume} cubic units"

            steps = [
                f"\\text{{Volume is multiplied by the cube of the scale factor}}",
                f"\\text{{New volume}} = {volume} \\times {k}^3 = {volume} \\times {k * k * k} = {new_volume} \\text{{ cubic units}}"
            ]

        elif problem_type == 'similarity':
            k = random.choice([2, 3, 4])

            latex = f"\\text{{A figure is dilated with scale factor }} k = {k}. \\text{{ Is the image similar to the original? Explain.}}"
            solution = "Yes, because dilations preserve angle measures and produce proportional side lengths."

            steps = [
                f"\\text{{Dilations always produce similar figures}}",
                f"\\text{{Angle measures are preserved}}",
                f"\\text{{Side lengths are proportional (all multiplied by }} {k})",
                f"\\text{{Therefore, the image is similar to the original}}"
            ]

        else:  # composition
            k1 = random.choice([2, 3])
            k2 = random.choice([2, 3])
            combined = k1 * k2

            latex = f"\\text{{A figure is dilated with scale factor }} {k1}, \\text{{ then dilated again with scale factor }} {k2}. \\text{{ What is the combined scale factor?}}"
            solution = str(combined)

            steps = [
                f"\\text{{Composition of dilations multiplies the scale factors}}",
                f"\\text{{Combined scale factor}} = {k1} \\times {k2} = {combined}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = DilationPreservedPropertiesGenerator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
