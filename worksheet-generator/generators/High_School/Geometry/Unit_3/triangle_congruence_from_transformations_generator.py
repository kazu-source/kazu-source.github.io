"""
Triangle Congruence from Transformations Generator
Creates problems about triangle congruence criteria derived from transformations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class TriangleCongruenceFromTransformationsGenerator:
    """Generates problems about triangle congruence using transformations."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

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
        """Basic congruence criteria identification"""
        problem_type = random.choice(['sss', 'sas', 'asa', 'aas'])

        if problem_type == 'sss':
            s1, s2, s3 = random.randint(5, 12), random.randint(5, 12), random.randint(5, 12)

            latex = f"\\text{{{{Triangle ABC has sides }}}} {s1}, {s2}, {s3}. \\text{{{{ Triangle DEF has sides }}}} {s1}, {s2}, {s3}."
            latex += " \\text{{Are the triangles congruent?}}"
            solution = "Yes, by SSS"
            steps = [
                f"\\text{{{{All three pairs of corresponding sides are equal}}}}",
                "\\text{{By SSS (Side-Side-Side) congruence criterion}}",
                "\\triangle ABC \\cong \\triangle DEF"
            ]

        elif problem_type == 'sas':
            s1, s2 = random.randint(6, 12), random.randint(6, 12)
            angle = random.randint(40, 120)

            latex = f"\\text{{{{In }}}} \\triangle ABC \\text{{{{ and }}}} \\triangle DEF: AB = DE = {s1}, AC = DF = {s2}, \\angle A = \\angle D = {angle}^\\circ."
            latex += " \\text{{Are they congruent?}}"
            solution = "Yes, by SAS"
            steps = [
                f"\\text{{{{Two sides are equal: }}}} {s1} \\text{{{{ and }}}} {s2}",
                f"\\text{{{{Included angle is equal: }}}} {angle}^\\circ",
                "\\text{{By SAS (Side-Angle-Side) congruence criterion}}",
                "\\triangle ABC \\cong \\triangle DEF"
            ]

        elif problem_type == 'asa':
            side = random.randint(8, 15)
            a1, a2 = random.randint(40, 70), random.randint(40, 70)

            latex = f"\\text{{{{In }}}} \\triangle ABC \\text{{{{ and }}}} \\triangle DEF: \\angle A = \\angle D = {a1}^\\circ, AB = DE = {side}, \\angle B = \\angle E = {a2}^\\circ."
            latex += " \\text{{Are they congruent?}}"
            solution = "Yes, by ASA"
            steps = [
                f"\\text{{{{Two angles are equal: }}}} {a1}^\\circ \\text{{{{ and }}}} {a2}^\\circ",
                f"\\text{{{{Included side is equal: }}}} {side}",
                "\\text{{By ASA (Angle-Side-Angle) congruence criterion}}",
                "\\triangle ABC \\cong \\triangle DEF"
            ]

        else:  # aas
            side = random.randint(8, 15)
            a1, a2 = random.randint(40, 70), random.randint(40, 70)

            latex = f"\\text{{{{In }}}} \\triangle ABC \\text{{{{ and }}}} \\triangle DEF: \\angle A = \\angle D = {a1}^\\circ, \\angle B = \\angle E = {a2}^\\circ, BC = EF = {side}."
            latex += " \\text{{Are they congruent?}}"
            solution = "Yes, by AAS"
            steps = [
                f"\\text{{{{Two angles are equal: }}}} {a1}^\\circ \\text{{{{ and }}}} {a2}^\\circ",
                f"\\text{{{{Non-included side is equal: }}}} {side}",
                "\\text{{By AAS (Angle-Angle-Side) congruence criterion}}",
                "\\triangle ABC \\cong \\triangle DEF"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Identify which congruence criterion applies"""
        problem_type = random.choice(['identify_criterion', 'not_congruent', 'missing_info'])

        if problem_type == 'identify_criterion':
            criterion = random.choice(['SSS', 'SAS', 'ASA', 'AAS'])

            if criterion == 'SSS':
                latex = "\\text{{What congruence criterion states that if all three sides of one triangle equal the three sides of another, the triangles are congruent?}}"
                solution = "SSS (Side-Side-Side)"
            elif criterion == 'SAS':
                latex = "\\text{{What congruence criterion uses two sides and the angle between them?}}"
                solution = "SAS (Side-Angle-Side)"
            elif criterion == 'ASA':
                latex = "\\text{{What congruence criterion uses two angles and the side between them?}}"
                solution = "ASA (Angle-Side-Angle)"
            else:
                latex = "\\text{{What congruence criterion uses two angles and a non-included side?}}"
                solution = "AAS (Angle-Angle-Side)"

            steps = [
                f"\\text{{{{The criterion is {criterion}}}}}",
                f"\\text{{{{This can be proven using rigid transformations}}}}"
            ]

        elif problem_type == 'not_congruent':
            a1, a2 = random.randint(40, 60), random.randint(50, 70)
            s1, s2 = random.randint(6, 10), random.randint(8, 12)

            latex = f"\\text{{{{Two triangles have }}}} \\angle A = \\angle D = {a1}^\\circ, \\angle B = \\angle E = {a2}^\\circ, AC = {s1}, DF = {s2}."
            latex += " \\text{{Can we conclude they are congruent?}}"
            solution = "No, we don't know which sides correspond"
            steps = [
                "\\text{{We have two angles equal (AA)}}",
                f"\\text{{{{But the sides are different: }}}} {s1} \\neq {s2}",
                "\\text{{The triangles are similar but not congruent}}",
                "\\text{{We cannot conclude congruence}}"
            ]

        else:  # missing_info
            given = random.choice(['two_sides', 'two_angles', 'one_side_one_angle'])

            if given == 'two_sides':
                s1, s2 = random.randint(6, 10), random.randint(7, 11)
                latex = f"\\text{{{{Two triangles have AB = DE = {s1} and BC = EF = {s2}. }}}}"
                latex += "\\text{{What additional information would prove congruence by SAS?}}"
                solution = f"The included angles: angle B = angle E"
                steps = [
                    "\\text{{For SAS, we need two sides and the included angle}}",
                    f"\\text{{{{We have sides }}}} {s1} \\text{{{{ and }}}} {s2}",
                    "\\text{{We need the angle between them: }} \\angle B = \\angle E"
                ]
            elif given == 'two_angles':
                a1, a2 = random.randint(45, 65), random.randint(50, 70)
                latex = f"\\text{{{{Two triangles have }}}} \\angle A = \\angle D = {a1}^\\circ \\text{{{{ and }}}} \\angle B = \\angle E = {a2}^\\circ. "
                latex += "\\text{{What additional information would prove congruence by ASA?}}"
                solution = "The included side: AB = DE"
                steps = [
                    "\\text{{For ASA, we need two angles and the included side}}",
                    f"\\text{{{{We have angles }}}} {a1}^\\circ \\text{{{{ and }}}} {a2}^\\circ",
                    "\\text{{We need the side between them: }} AB = DE"
                ]
            else:
                s = random.randint(7, 12)
                a = random.randint(50, 80)
                latex = f"\\text{{{{Two triangles have AB = DE = {s} and }}}} \\angle C = \\angle F = {a}^\\circ. "
                latex += "\\text{{What would prove congruence?}}"
                solution = "Need more information - not enough for any criterion"
                steps = [
                    "\\text{{We have one side and one non-included angle}}",
                    "\\text{{This is not enough for SAS, ASA, AAS, or SSS}}",
                    "\\text{{We need additional corresponding parts}}"
                ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Apply congruence criteria with variables"""
        problem_type = random.choice(['solve_for_x', 'prove_using_criterion', 'hl_theorem'])

        if problem_type == 'solve_for_x':
            a = random.randint(2, 5)
            b = random.randint(3, 8)
            c = random.randint(10, 20)

            latex = f"\\text{{{{If }}}} \\triangle ABC \\cong \\triangle DEF \\text{{{{ by SAS, AB = {a}x + {b}, DE = {c}, "
            latex += f"\\text{{{{and the angles at A and D are included angles, find x.}}}}}}"

            x = (c - b) / a
            solution = f"x = {x}"
            steps = [
                "\\text{{By congruence, corresponding sides are equal}}",
                f"AB = DE \\Rightarrow {a}x + {b} = {c}",
                f"{a}x = {c - b}",
                f"x = {x}"
            ]

        elif problem_type == 'prove_using_criterion':
            s = random.randint(8, 15)

            latex = f"\\text{{{{In isosceles triangle ABC with AB = AC = {s}, prove that }}}} \\angle B = \\angle C \\text{{{{ using congruence.}}}}"
            solution = "By SAS, triangle ABD ≅ triangle ACD (D is midpoint of BC)"
            steps = [
                f"\\text{{{{Let D be the midpoint of BC}}}}",
                f"\\text{{{{Then BD = DC}}}}",
                f"AB = AC = {s} \\text{{{{ (given)}}}}",
                "AD = AD \\text{{(reflexive)}}",
                "\\text{{By SSS, }} \\triangle ABD \\cong \\triangle ACD",
                "\\text{{Therefore, }} \\angle B = \\angle C \\text{{(CPCTC)}}"
            ]

        else:  # hl_theorem
            leg = random.randint(6, 12)
            hyp = random.randint(leg + 3, leg + 8)

            latex = f"\\text{{{{Two right triangles have legs of length {leg} and hypotenuses of length {hyp}. }}}}"
            latex += "\\text{{Prove they are congruent.}}"
            solution = "By HL (Hypotenuse-Leg) theorem"
            steps = [
                "\\text{{Both triangles are right triangles}}",
                f"\\text{{{{Both have hypotenuse }}}} {hyp}",
                f"\\text{{{{Both have one leg }}}} {leg}",
                "\\text{{By Pythagorean theorem, the other legs are equal}}",
                "\\text{{Therefore, by HL theorem (or SSS), the triangles are congruent}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Complex congruence proofs and applications"""
        problem_type = random.choice(['prove_criterion', 'counterexample', 'cpctc'])

        if problem_type == 'prove_criterion':
            latex = "\\text{{Prove that SAS congruence criterion is valid using rigid transformations.}}"
            solution = "Can map one triangle to other using translation, rotation"
            steps = [
                "\\text{{Given: Two triangles with two sides and included angle equal}}",
                "\\text{{Step 1: Translate first triangle so corresponding vertices coincide}}",
                "\\text{{Step 2: Rotate about that vertex to align the first sides}}",
                "\\text{{Step 3: Since angles are equal, second sides now align too}}",
                "\\text{{Step 4: Since side lengths are equal, endpoints coincide}}",
                "\\text{{Conclusion: Translation + rotation maps one to other, so congruent}}"
            ]

        elif problem_type == 'counterexample':
            s1, s2, s3 = 5, 7, 9
            a1, a2 = 50, 60

            latex = "\\text{{Give an example showing that SSA (Side-Side-Angle) is NOT a valid congruence criterion.}}"
            solution = "Ambiguous case: two different triangles can have same SSA"
            steps = [
                "\\text{{Consider two sides and a non-included angle}}",
                "\\text{{Example: sides 5 and 7, with angle 30° opposite the side of length 5}}",
                "\\text{{The side of length 7 can swing to two different positions}}",
                "\\text{{This creates two non-congruent triangles with same SSA}}",
                "\\text{{Therefore, SSA is not a valid congruence criterion}}"
            ]

        else:  # cpctc
            angle = random.randint(45, 75)

            latex = f"\\text{{{{Given }}}} \\triangle ABC \\cong \\triangle DEF \\text{{{{ by ASA with }}}} \\angle A = {angle}^\\circ. "
            latex += f"\\text{{{{If BC = 10, what is EF?}}}}"
            solution = "EF = 10"
            steps = [
                "\\text{{Since }} \\triangle ABC \\cong \\triangle DEF",
                "\\text{{All corresponding parts are congruent (CPCTC)}}",
                "\\text{{BC corresponds to EF}}",
                "\\text{{Therefore, EF = BC = 10}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = TriangleCongruenceFromTransformationsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")


if __name__ == '__main__':
    main()
