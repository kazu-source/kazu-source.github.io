"""
Statistics in Two Categorical Variables - Association Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class StatisticsTwoCategoricalAssociationGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        # Create data with clear association
        group1_yes = random.randint(70, 90)
        group1_no = random.randint(10, 30)
        group2_yes = random.randint(20, 40)
        group2_no = random.randint(60, 80)

        question = f"\\text{{Segmented bar chart shows two groups:}}\\\\"\
                   f"\\text{{Group A: Yes={group1_yes}, No={group1_no}}}\\\\"\
                   f"\\text{{Group B: Yes={group2_yes}, No={group2_no}}}\\\\"\
                   f"\\text{{Is there evidence of association between group and response?}}"

        group1_total = group1_yes + group1_no
        group2_total = group2_yes + group2_no
        pct1 = round((group1_yes / group1_total) * 100, 1)
        pct2 = round((group2_yes / group2_no) * 100, 1)

        solution = f"Yes, clear association: Group A: {pct1}\\% yes vs Group B: {pct2}\\% yes"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Create data with moderate association
        online_satisfied = random.randint(80, 100)
        online_unsatisfied = random.randint(40, 60)
        store_satisfied = random.randint(50, 70)
        store_unsatisfied = random.randint(70, 90)

        question = f"\\text{{Customer satisfaction by purchase method:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|}} \\hline"\
                   f" & \\text{{Satisfied}} & \\text{{Unsatisfied}} \\\\ \\hline"\
                   f"\\text{{Online}} & {online_satisfied} & {online_unsatisfied} \\\\ \\hline"\
                   f"\\text{{In-store}} & {store_satisfied} & {store_unsatisfied} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{(a) Calculate conditional distributions}}\\\\"\
                   f"\\text{{(b) Is there association? Explain using the distributions.}}"

        online_total = online_satisfied + online_unsatisfied
        store_total = store_satisfied + store_unsatisfied

        online_sat_pct = round((online_satisfied / online_total) * 100, 1)
        store_sat_pct = round((store_satisfied / store_total) * 100, 1)

        diff = abs(online_sat_pct - store_sat_pct)

        solution = f"(a) Online satisfied: {online_sat_pct}\\%, In-store satisfied: {store_sat_pct}\\%, "\
                   f"(b) Yes, {diff} percentage point difference suggests association"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Three-way comparison
        cat1_a = random.randint(40, 60)
        cat1_b = random.randint(30, 50)
        cat2_a = random.randint(50, 70)
        cat2_b = random.randint(25, 45)
        cat3_a = random.randint(35, 55)
        cat3_b = random.randint(40, 60)

        question = f"\\text{{Three categories vs. two outcomes:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|}} \\hline"\
                   f" & \\text{{Outcome A}} & \\text{{Outcome B}} \\\\ \\hline"\
                   f"\\text{{Category 1}} & {cat1_a} & {cat1_b} \\\\ \\hline"\
                   f"\\text{{Category 2}} & {cat2_a} & {cat2_b} \\\\ \\hline"\
                   f"\\text{{Category 3}} & {cat3_a} & {cat3_b} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{(a) Compare conditional distributions of Outcome A}}\\\\"\
                   f"\\text{{(b) Which category shows strongest association with Outcome A?}}"

        cat1_total = cat1_a + cat1_b
        cat2_total = cat2_a + cat2_b
        cat3_total = cat3_a + cat3_b

        pct1 = round((cat1_a / cat1_total) * 100, 1)
        pct2 = round((cat2_a / cat2_total) * 100, 1)
        pct3 = round((cat3_a / cat3_total) * 100, 1)

        percentages = [(pct1, "Category 1"), (pct2, "Category 2"), (pct3, "Category 3")]
        max_pct, max_cat = max(percentages, key=lambda x: x[0])

        solution = f"(a) Cat1: {pct1}\\%, Cat2: {pct2}\\%, Cat3: {pct3}\\%, (b) {max_cat} ({max_pct}\\%)"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Simpson's paradox setup
        dept1_male_admit = 60
        dept1_male_reject = 40
        dept1_female_admit = 30
        dept1_female_reject = 20

        dept2_male_admit = 10
        dept2_male_reject = 90
        dept2_female_admit = 40
        dept2_female_reject = 60

        question = f"\\text{{College admissions by department and gender:}}\\\\"\
                   f"\\text{{Dept A: Male(Admit:{dept1_male_admit}, Reject:{dept1_male_reject}), }}"\
                   f"\\text{{Female(Admit:{dept1_female_admit}, Reject:{dept1_female_reject})}}\\\\"\
                   f"\\text{{Dept B: Male(Admit:{dept2_male_admit}, Reject:{dept2_male_reject}), }}"\
                   f"\\text{{Female(Admit:{dept2_female_admit}, Reject:{dept2_female_reject})}}\\\\"\
                   f"\\text{{(a) Calculate admission rates by gender within each department}}\\\\"\
                   f"\\text{{(b) Calculate overall admission rates by gender}}\\\\"\
                   f"\\text{{(c) Explain why the pattern reverses. What does this illustrate?}}"

        # Within departments
        dept1_male_rate = round((dept1_male_admit / (dept1_male_admit + dept1_male_reject)) * 100, 1)
        dept1_female_rate = round((dept1_female_admit / (dept1_female_admit + dept1_female_reject)) * 100, 1)
        dept2_male_rate = round((dept2_male_admit / (dept2_male_admit + dept2_male_reject)) * 100, 1)
        dept2_female_rate = round((dept2_female_admit / (dept2_female_admit + dept2_female_reject)) * 100, 1)

        # Overall
        total_male_admit = dept1_male_admit + dept2_male_admit
        total_male = dept1_male_admit + dept1_male_reject + dept2_male_admit + dept2_male_reject
        total_female_admit = dept1_female_admit + dept2_female_admit
        total_female = dept1_female_admit + dept1_female_reject + dept2_female_admit + dept2_female_reject

        overall_male_rate = round((total_male_admit / total_male) * 100, 1)
        overall_female_rate = round((total_female_admit / total_female) * 100, 1)

        solution = f"(a) DeptA: M:{dept1_male_rate}\\%, F:{dept1_female_rate}\\%; DeptB: M:{dept2_male_rate}\\%, F:{dept2_female_rate}\\%, "\
                   f"(b) Overall: M:{overall_male_rate}\\%, F:{overall_female_rate}\\%, "\
                   f"(c) Simpson's Paradox: females have higher rates within each dept but lower overall due to applying more to selective dept"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = StatisticsTwoCategoricalAssociationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
