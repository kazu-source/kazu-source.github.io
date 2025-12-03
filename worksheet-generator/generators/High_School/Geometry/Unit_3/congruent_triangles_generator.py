"""
Congruent Triangles Generator
Creates problems about triangle congruence criteria (SSS, SAS, ASA, AAS, HL)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class CongruentTrianglesGenerator:
    """Generates problems about triangle congruence."""

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
        """Identify which congruence criterion applies"""
        criteria = [
            ("Three pairs of congruent sides", "SSS",
             "When all three sides of one triangle are congruent to three sides of another, use SSS."),
            ("Two sides and the included angle are congruent", "SAS",
             "When two sides and the angle between them are congruent, use SAS."),
            ("Two angles and the included side are congruent", "ASA",
             "When two angles and the side between them are congruent, use ASA."),
            ("Two angles and a non-included side are congruent", "AAS",
             "When two angles and a side not between them are congruent, use AAS."),
            ("The hypotenuse and a leg of two right triangles are congruent", "HL",
             "For right triangles, if the hypotenuse and one leg are congruent, use HL.")
        ]

        given, answer, explanation = random.choice(criteria)

        latex = f"\\text{{Which congruence criterion applies? }} {given}"
        solution = answer

        steps = [
            f"\\text{{{explanation}}}",
            f"\\text{{Answer: {answer}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Determine if triangles can be proven congruent and by which criterion"""
        scenarios = [
            ("AB \\cong DE, BC \\cong EF, CA \\cong FD", "Yes, by SSS",
             "All three pairs of corresponding sides are congruent."),
            ("AB \\cong DE, \\angle B \\cong \\angle E, BC \\cong EF", "Yes, by SAS",
             "Two sides and the included angle are congruent."),
            ("\\angle A \\cong \\angle D, AB \\cong DE, \\angle B \\cong \\angle E", "Yes, by ASA",
             "Two angles and the included side are congruent."),
            ("\\angle A \\cong \\angle D, \\angle B \\cong \\angle E, BC \\cong EF", "Yes, by AAS",
             "Two angles and a non-included side are congruent."),
            ("AB \\cong DE, AC \\cong DF, \\angle B \\cong \\angle E", "No (SSA)",
             "SSA is not a valid congruence criterion."),
            ("\\angle A \\cong \\angle D, \\angle B \\cong \\angle E, \\angle C \\cong \\angle F", "No (AAA)",
             "AAA proves similarity, not congruence."),
        ]

        given, answer, explanation = random.choice(scenarios)

        latex = f"\\text{{Can }} \\triangle ABC \\cong \\triangle DEF \\text{{ be proven? Given: }} {given}"
        solution = answer

        steps = [
            f"\\text{{Analyze the given information:}}",
            f"\\text{{{explanation}}}",
            f"\\text{{{answer}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Find missing values using congruent triangles"""
        problem_type = random.choice(['find_side', 'find_angle'])

        if problem_type == 'find_side':
            # Given congruent triangles, find unknown side
            a = random.randint(2, 4)
            x = random.randint(3, 8)
            b = random.randint(1, 10)
            side = a * x + b

            other_side = random.randint(5, 15)

            latex = f"\\triangle ABC \\cong \\triangle DEF. \\text{{ If }} AB = {a}x + {b} \\text{{ and }} DE = {side}, \\text{{ find }} x."
            solution = str(x)

            steps = [
                f"\\text{{Since the triangles are congruent, corresponding sides are equal.}}",
                f"AB = DE",
                f"{a}x + {b} = {side}",
                f"{a}x = {side - b}",
                f"x = {x}"
            ]
        else:
            # Given congruent triangles, find unknown angle
            a = random.randint(2, 5)
            x = random.randint(5, 20)
            b = random.randint(0, 20)
            angle = a * x + b

            latex = f"\\triangle PQR \\cong \\triangle STU. \\text{{ If }} m\\angle P = {a}x + {b} \\text{{ and }} m\\angle S = {angle}°, \\text{{ find }} x."
            solution = str(x)

            steps = [
                f"\\text{{Since the triangles are congruent, corresponding angles are equal.}}",
                f"m\\angle P = m\\angle S",
                f"{a}x + {b} = {angle}",
                f"{a}x = {angle - b}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Prove triangles congruent or find multiple values"""
        problem_type = random.choice(['proof_setup', 'multiple_values', 'cpctc'])

        if problem_type == 'proof_setup':
            scenarios = [
                (
                    "In parallelogram ABCD, diagonal AC is drawn.",
                    "\\triangle ABC \\cong \\triangle CDA by ASA (or SAS)",
                    "Opposite sides of a parallelogram are congruent, and alternate interior angles are congruent."
                ),
                (
                    "M is the midpoint of both \\overline{AB} and \\overline{CD}.",
                    "\\triangle AMC \\cong \\triangle BMD by SAS",
                    "AM = BM, CM = DM (midpoint), and vertical angles AMC and BMD are congruent."
                ),
                (
                    "Isosceles triangle ABC with AB = AC. D is the midpoint of BC.",
                    "\\triangle ABD \\cong \\triangle ACD by SSS",
                    "AB = AC (given), BD = CD (midpoint), AD = AD (reflexive)."
                )
            ]

            given, answer, explanation = random.choice(scenarios)

            latex = f"\\text{{{given} Which triangles are congruent and why?}}"
            solution = answer

            steps = [
                f"\\text{{{explanation}}}",
                f"\\text{{Therefore: {answer}}}"
            ]

        elif problem_type == 'multiple_values':
            # Find both x and y
            x = random.randint(3, 8)
            y = random.randint(2, 6)

            a1, b1 = random.randint(2, 4), random.randint(1, 5)
            a2, b2 = random.randint(2, 4), random.randint(1, 5)

            side1 = a1 * x + b1
            side2 = a2 * y + b2

            latex = f"\\triangle ABC \\cong \\triangle DEF. \\text{{ If }} AB = {a1}x + {b1}, DE = {side1}, BC = {a2}y + {b2}, EF = {side2}, \\text{{ find }} x \\text{{ and }} y."
            solution = f"x = {x}, y = {y}"

            steps = [
                f"\\text{{From }} AB = DE: {a1}x + {b1} = {side1} \\Rightarrow x = {x}",
                f"\\text{{From }} BC = EF: {a2}y + {b2} = {side2} \\Rightarrow y = {y}"
            ]

        else:
            # CPCTC application
            x = random.randint(4, 10)
            a = random.randint(2, 4)
            b = random.randint(1, 8)
            given_value = a * x + b

            latex = f"\\triangle RST \\cong \\triangle XYZ \\text{{ by SAS. If }} RS = {a}x + {b} \\text{{ and }} XY = {given_value}, \\text{{ find }} x \\text{{ and }} RT \\text{{ if }} RT = 2x + 3."
            solution = f"x = {x}, RT = {2*x + 3}"

            steps = [
                f"\\text{{By CPCTC (Corresponding Parts of Congruent Triangles are Congruent):}}",
                f"RS = XY",
                f"{a}x + {b} = {given_value}",
                f"x = {x}",
                f"RT = 2({x}) + 3 = {2*x + 3}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = CongruentTrianglesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
