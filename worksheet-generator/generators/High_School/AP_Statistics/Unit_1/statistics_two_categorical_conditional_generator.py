"""
Statistics in Two Categorical Variables - Conditional Distribution Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class StatisticsTwoCategoricalConditionalGenerator:
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
        male_sport = random.randint(40, 60)
        male_music = random.randint(20, 35)
        female_sport = random.randint(25, 40)
        female_music = random.randint(35, 55)

        question = f"\\text{{Extracurricular preference by gender:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|}} \\hline"\
                   f" & \\text{{Sports}} & \\text{{Music}} \\\\ \\hline"\
                   f"\\text{{Male}} & {male_sport} & {male_music} \\\\ \\hline"\
                   f"\\text{{Female}} & {female_sport} & {female_music} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{What percent of males prefer sports?}}"

        male_total = male_sport + male_music
        percent = round((male_sport / male_total) * 100, 1)

        solution = f"{percent}\\%"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        fresh_bus = random.randint(30, 50)
        fresh_walk = random.randint(20, 35)
        fresh_car = random.randint(10, 25)
        senior_bus = random.randint(15, 30)
        senior_walk = random.randint(25, 40)
        senior_car = random.randint(40, 60)

        question = f"\\text{{Transportation method by grade level:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|c|}} \\hline"\
                   f" & \\text{{Bus}} & \\text{{Walk}} & \\text{{Car}} \\\\ \\hline"\
                   f"\\text{{Freshman}} & {fresh_bus} & {fresh_walk} & {fresh_car} \\\\ \\hline"\
                   f"\\text{{Senior}} & {senior_bus} & {senior_walk} & {senior_car} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{(a) Calculate the conditional distribution for freshmen}}\\\\"\
                   f"\\text{{(b) Calculate the conditional distribution for seniors}}"

        fresh_total = fresh_bus + fresh_walk + fresh_car
        senior_total = senior_bus + senior_walk + senior_car

        fresh_bus_pct = round((fresh_bus / fresh_total) * 100, 1)
        fresh_walk_pct = round((fresh_walk / fresh_total) * 100, 1)
        fresh_car_pct = round((fresh_car / fresh_total) * 100, 1)

        senior_bus_pct = round((senior_bus / senior_total) * 100, 1)
        senior_walk_pct = round((senior_walk / senior_total) * 100, 1)
        senior_car_pct = round((senior_car / senior_total) * 100, 1)

        solution = f"(a) Freshmen: Bus {fresh_bus_pct}\\%, Walk {fresh_walk_pct}\\%, Car {fresh_car_pct}\\%, "\
                   f"(b) Seniors: Bus {senior_bus_pct}\\%, Walk {senior_walk_pct}\\%, Car {senior_car_pct}\\%"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        treat_mild = random.randint(20, 35)
        treat_moderate = random.randint(40, 60)
        treat_severe = random.randint(10, 25)
        placebo_mild = random.randint(15, 30)
        placebo_moderate = random.randint(30, 50)
        placebo_severe = random.randint(25, 45)

        question = f"\\text{{Symptom severity by treatment:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|c|}} \\hline"\
                   f" & \\text{{Mild}} & \\text{{Moderate}} & \\text{{Severe}} \\\\ \\hline"\
                   f"\\text{{Treatment}} & {treat_mild} & {treat_moderate} & {treat_severe} \\\\ \\hline"\
                   f"\\text{{Placebo}} & {placebo_mild} & {placebo_moderate} & {placebo_severe} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{(a) Find conditional distributions for both groups}}\\\\"\
                   f"\\text{{(b) Compare the distributions. Which group had better outcomes?}}\\\\"\
                   f"\\text{{(c) Support your answer with specific percentages.}}"

        treat_total = treat_mild + treat_moderate + treat_severe
        placebo_total = placebo_mild + placebo_moderate + placebo_severe

        treat_mild_pct = round((treat_mild / treat_total) * 100, 1)
        treat_mod_pct = round((treat_moderate / treat_total) * 100, 1)
        treat_sev_pct = round((treat_severe / treat_total) * 100, 1)

        placebo_mild_pct = round((placebo_mild / placebo_total) * 100, 1)
        placebo_mod_pct = round((placebo_moderate / placebo_total) * 100, 1)
        placebo_sev_pct = round((placebo_severe / placebo_total) * 100, 1)

        solution = f"(a) Treatment: Mild {treat_mild_pct}\\%, Mod {treat_mod_pct}\\%, Sev {treat_sev_pct}\\%; "\
                   f"Placebo: Mild {placebo_mild_pct}\\%, Mod {placebo_mod_pct}\\%, Sev {placebo_sev_pct}\\%, "\
                   f"(b) Treatment group better, (c) Treatment has {treat_mild_pct}\\% mild vs placebo {placebo_mild_pct}\\% "\
                   f"and {treat_sev_pct}\\% severe vs {placebo_sev_pct}\\%"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Marginal vs conditional
        male_yes = 45
        male_no = 55
        female_yes = 65
        female_no = 35

        question = f"\\text{{Survey responses by gender:}}\\\\"\
                   f"\\begin{{array}}{{|c|c|c|}} \\hline"\
                   f" & \\text{{Yes}} & \\text{{No}} \\\\ \\hline"\
                   f"\\text{{Male}} & {male_yes} & {male_no} \\\\ \\hline"\
                   f"\\text{{Female}} & {female_yes} & {female_no} \\\\ \\hline"\
                   f"\\end{{array}}\\\\"\
                   f"\\text{{(a) Calculate the marginal distribution of responses}}\\\\"\
                   f"\\text{{(b) Calculate conditional distributions for each gender}}\\\\"\
                   f"\\text{{(c) Explain the difference between marginal and conditional distributions}}\\\\"\
                   f"\\text{{(d) Which is more useful for detecting association? Why?}}"

        male_total = male_yes + male_no
        female_total = female_yes + female_no
        yes_total = male_yes + female_yes
        no_total = male_no + female_no
        grand_total = yes_total + no_total

        # Marginal
        marg_yes = round((yes_total / grand_total) * 100, 1)
        marg_no = round((no_total / grand_total) * 100, 1)

        # Conditional
        male_yes_pct = round((male_yes / male_total) * 100, 1)
        male_no_pct = round((male_no / male_total) * 100, 1)
        female_yes_pct = round((female_yes / female_total) * 100, 1)
        female_no_pct = round((female_no / female_total) * 100, 1)

        solution = f"(a) Marginal: Yes {marg_yes}\\%, No {marg_no}\\%, "\
                   f"(b) Male: Yes {male_yes_pct}\\%, No {male_no_pct}\\%; Female: Yes {female_yes_pct}\\%, No {female_no_pct}\\%, "\
                   f"(c) Marginal shows overall distribution; conditional shows distribution within subgroups, "\
                   f"(d) Conditional is more useful - allows comparison between groups to detect association"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = StatisticsTwoCategoricalConditionalGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
