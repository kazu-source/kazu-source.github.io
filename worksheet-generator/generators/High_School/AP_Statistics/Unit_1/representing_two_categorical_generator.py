"""
Representing Two Categorical Variables Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class RepresentingTwoCategoricalGenerator:
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
        male_yes = random.randint(30, 50)
        male_no = random.randint(20, 40)
        female_yes = random.randint(35, 55)
        female_no = random.randint(15, 35)

        question = f"\\text{{Two-way table: Support for proposal by gender}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|}} \\hline"\
                   f" & \\text{{Yes}} & \\text{{No}} \\\\ \\hline"\
                   f"\\text{{Male}} & {male_yes} & {male_no} \\\\ \\hline"\
                   f"\\text{{Female}} & {female_yes} & {female_no} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{What is the total number of females surveyed?}}"

        total_female = female_yes + female_no
        solution = f"{total_female}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        freshman_yes = random.randint(25, 45)
        freshman_no = random.randint(15, 30)
        sophomore_yes = random.randint(30, 50)
        sophomore_no = random.randint(20, 35)

        total = freshman_yes + freshman_no + sophomore_yes + sophomore_no

        question = f"\\text{{Class year vs. participation:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|}} \\hline"\
                   f" & \\text{{Participate}} & \\text{{Don't}} \\\\ \\hline"\
                   f"\\text{{Freshman}} & {freshman_yes} & {freshman_no} \\\\ \\hline"\
                   f"\\text{{Sophomore}} & {sophomore_yes} & {sophomore_no} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{(a) What percent of all students are sophomores who participate?}}\\\\"\
                   f"\\text{{(b) How many total students said they participate?}}"

        percent_soph_yes = round((sophomore_yes / total) * 100, 1)
        total_yes = freshman_yes + sophomore_yes

        solution = f"(a) {percent_soph_yes}\\%, (b) {total_yes}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        urban_dem = random.randint(60, 90)
        urban_rep = random.randint(30, 50)
        rural_dem = random.randint(40, 60)
        rural_rep = random.randint(50, 80)

        question = f"\\text{{Political affiliation by location:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|}} \\hline"\
                   f" & \\text{{Democrat}} & \\text{{Republican}} \\\\ \\hline"\
                   f"\\text{{Urban}} & {urban_dem} & {urban_rep} \\\\ \\hline"\
                   f"\\text{{Rural}} & {rural_dem} & {rural_rep} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{(a) Create row totals and column totals}}\\\\"\
                   f"\\text{{(b) What percent of urban residents are Democrats?}}\\\\"\
                   f"\\text{{(c) What percent of Democrats are urban residents?}}"

        urban_total = urban_dem + urban_rep
        rural_total = rural_dem + rural_rep
        dem_total = urban_dem + rural_dem
        rep_total = urban_rep + rural_rep
        grand_total = urban_total + rural_total

        percent_urban_dem = round((urban_dem / urban_total) * 100, 1)
        percent_dem_urban = round((urban_dem / dem_total) * 100, 1)

        solution = f"(a) Urban: {urban_total}, Rural: {rural_total}, Dem: {dem_total}, Rep: {rep_total}, Total: {grand_total}, "\
                   f"(b) {percent_urban_dem}\\%, (c) {percent_dem_urban}\\%"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        treatment_success = random.randint(70, 90)
        treatment_fail = random.randint(20, 40)
        control_success = random.randint(40, 60)
        control_fail = random.randint(50, 70)

        question = f"\\text{{Medical study results:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|}} \\hline"\
                   f" & \\text{{Success}} & \\text{{Failure}} \\\\ \\hline"\
                   f"\\text{{Treatment}} & {treatment_success} & {treatment_fail} \\\\ \\hline"\
                   f"\\text{{Control}} & {control_success} & {control_fail} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{(a) Calculate marginal distribution of outcomes}}\\\\"\
                   f"\\text{{(b) Calculate conditional distribution of outcomes for treatment group}}\\\\"\
                   f"\\text{{(c) Does treatment appear effective? Support with data.}}"

        treatment_total = treatment_success + treatment_fail
        control_total = control_success + control_fail
        success_total = treatment_success + control_success
        fail_total = treatment_fail + control_fail
        grand_total = treatment_total + control_total

        marg_success = round((success_total / grand_total) * 100, 1)
        marg_fail = round((fail_total / grand_total) * 100, 1)

        cond_treatment_success = round((treatment_success / treatment_total) * 100, 1)
        cond_treatment_fail = round((treatment_fail / treatment_total) * 100, 1)

        cond_control_success = round((control_success / control_total) * 100, 1)

        solution = f"(a) Success: {marg_success}\\%, Failure: {marg_fail}\\%, "\
                   f"(b) Treatment Success: {cond_treatment_success}\\%, Failure: {cond_treatment_fail}\\%, "\
                   f"(c) Yes, {cond_treatment_success}\\% vs {cond_control_success}\\% success rate"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = RepresentingTwoCategoricalGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
