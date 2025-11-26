"""
Modeling with Sequences Generator
Creates real-world problems using arithmetic and geometric sequences
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class ModelingWithSequencesGenerator:
    """Generates problems about modeling real-world situations with sequences."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
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
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy: Simple linear growth/savings (arithmetic)"""
        problem_types = ['savings', 'growth', 'debt_payment']
        problem_type = random.choice(problem_types)

        if problem_type == 'savings':
            initial = random.choice([50, 100, 150])
            weekly = random.choice([10, 15, 20, 25])
            weeks = random.randint(4, 6)

            latex = f"\\text{{Sarah saves }} \\${initial} \\text{{ initially and adds }} \\${weekly} \\text{{ each week. "
            latex += f"\\text{{How much after }} {weeks} \\text{{ weeks?}}"

            # This is arithmetic: a_n = a_1 + (n-1)d
            # But for week n, she has initial + n*weekly
            total = initial + weeks * weekly
            solution = total

            steps = [
                f"\\text{{Initial: }} \\${initial}",
                f"\\text{{Added: }} {weeks} \\times \\${weekly} = \\${weeks * weekly}",
                f"\\text{{Total: }} \\${initial} + \\${weeks * weekly} = \\${total}"
            ]

        elif problem_type == 'growth':
            initial = random.choice([100, 150, 200])
            daily = random.choice([5, 10, 15])
            days = random.randint(5, 8)

            latex = f"\\text{{A plant is }} {initial}\\text{{mm tall and grows }} {daily}\\text{{mm per day. "
            latex += f"\\text{{Height after }} {days} \\text{{ days?}}"

            total = initial + days * daily
            solution = total

            steps = [
                f"\\text{{Initial height: }} {initial}\\text{{mm}}",
                f"\\text{{Growth: }} {days} \\times {daily} = {days * daily}\\text{{mm}}",
                f"\\text{{Final height: }} {total}\\text{{mm}}"
            ]

        else:  # debt_payment
            initial = random.choice([500, 600, 800, 1000])
            monthly = random.choice([50, 75, 100])
            months = random.randint(3, 5)

            latex = f"\\text{{A debt of }} \\${initial} \\text{{ decreases by }} \\${monthly} \\text{{ per month. "
            latex += f"\\text{{Amount remaining after }} {months} \\text{{ months?}}"

            remaining = initial - months * monthly
            solution = remaining

            steps = [
                f"\\text{{Initial debt: }} \\${initial}",
                f"\\text{{Paid: }} {months} \\times \\${monthly} = \\${months * monthly}",
                f"\\text{{Remaining: }} \\${initial} - \\${months * monthly} = \\${remaining}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Exponential growth/decay (geometric)"""
        problem_types = ['population', 'depreciation', 'bacteria', 'investment']
        problem_type = random.choice(problem_types)

        if problem_type == 'population':
            initial = random.choice([1000, 2000, 5000])
            rate = random.choice([2, 3])
            periods = random.randint(3, 5)

            if rate == 2:
                description = "doubles"
            else:
                description = "triples"

            latex = f"\\text{{A population of }} {initial} \\text{{ }} {description} \\text{{ every period. "
            latex += f"\\text{{Population after }} {periods} \\text{{ periods?}}"

            final = initial * (rate ** periods)
            solution = final

            steps = [
                f"\\text{{This is geometric with }} r = {rate}",
                f"a_n = {initial} \\times {rate}^{{{periods}}}",
                f"a_n = {final}"
            ]

        elif problem_type == 'depreciation':
            initial = random.choice([10000, 15000, 20000])
            rate = 0.8  # 20% depreciation = 80% remaining
            years = random.randint(2, 4)

            latex = f"\\text{{A car worth }} \\${initial} \\text{{ depreciates 20\\% per year. "
            latex += f"\\text{{Value after }} {years} \\text{{ years?}}"

            final = initial * (rate ** years)
            solution = int(final)

            steps = [
                f"\\text{{Each year, value is 80\\% of previous}}",
                f"\\text{{Ratio: }} r = 0.8",
                f"\\text{{Value: }} \\${initial} \\times 0.8^{years} = \\${solution}"
            ]

        elif problem_type == 'bacteria':
            initial = random.choice([100, 200, 500])
            rate = 2
            hours = random.randint(4, 6)

            latex = f"\\text{{Bacteria count starts at }} {initial} \\text{{ and doubles each hour. "
            latex += f"\\text{{Count after }} {hours} \\text{{ hours?}}"

            final = initial * (rate ** hours)
            solution = final

            steps = [
                f"\\text{{Geometric sequence with }} r = 2",
                f"a_n = {initial} \\times 2^{hours}",
                f"a_n = {final}"
            ]

        else:  # investment
            initial = random.choice([1000, 2000, 5000])
            rate = 1.05  # 5% growth
            years = random.randint(3, 5)

            latex = f"\\text{{An investment of }} \\${initial} \\text{{ grows 5\\% annually. "
            latex += f"\\text{{Value after }} {years} \\text{{ years (to nearest dollar)?}}"

            final = initial * (rate ** years)
            solution = int(final)

            steps = [
                f"\\text{{Each year: new value = 1.05 }} \\times \\text{{ old value}}",
                f"\\text{{Value: }} \\${initial} \\times 1.05^{years}",
                f"\\text{{Value: }} \\${solution}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: More complex scenarios, finding patterns"""
        problem_types = ['compound_growth', 'mixed_model', 'find_term', 'compare']
        problem_type = random.choice(problem_types)

        if problem_type == 'compound_growth':
            # Population with migration (arithmetic) and birth rate (geometric)
            initial = random.choice([1000, 2000])
            immigrants = random.choice([50, 100])
            birth_rate = 1.1  # 10% increase
            years = 3

            latex = f"\\text{{A town has }} {initial} \\text{{ people. Each year }} {immigrants} \\text{{ immigrate "
            latex += f"\\text{{and population grows 10\\%. Find population after }} {years} \\text{{ years.}}"

            # Year 1: (1000 + 50) * 1.1
            # Year 2: (result + 50) * 1.1
            # Year 3: (result + 50) * 1.1
            pop = initial
            for _ in range(years):
                pop = (pop + immigrants) * birth_rate

            solution = int(pop)

            steps = [
                f"\\text{{Each year: add }} {immigrants}\\text{{, then multiply by 1.1}}",
                f"\\text{{Year 1: }} ({initial} + {immigrants}) \\times 1.1",
                f"\\text{{Continue pattern...}}",
                f"\\text{{Final: }} {solution}"
            ]

        elif problem_type == 'mixed_model':
            # Decide if situation is arithmetic or geometric
            savings = random.choice([100, 200])
            add_monthly = random.choice([25, 50])
            months = 6

            latex = f"\\text{{Model: }} \\${savings} \\text{{ initial, }} \\${add_monthly} \\text{{ added monthly. "
            latex += f"\\text{{Is this arithmetic or geometric? Amount after }} {months} \\text{{ months?}}"

            total = savings + months * add_monthly
            solution = f"Arithmetic, ${total}"

            steps = [
                f"\\text{{Constant addition → Arithmetic sequence}}",
                f"\\text{{Amount: }} \\${savings} + {months} \\times \\${add_monthly} = \\${total}"
            ]

        elif problem_type == 'find_term':
            # When does value reach target?
            initial = 50
            weekly = 15
            target = random.choice([200, 250, 300])

            latex = f"\\text{{Savings start at }} \\${initial}\\text{{, }} \\${weekly} \\text{{ added weekly. "
            latex += f"\\text{{After how many weeks will savings exceed }} \\${target}\\text{{?}}"

            # initial + n * weekly > target
            # n > (target - initial) / weekly
            n = ((target - initial) // weekly) + 1
            solution = n

            steps = [
                f"{initial} + n \\times {weekly} > {target}",
                f"n \\times {weekly} > {target - initial}",
                f"n > {(target - initial) / weekly:.1f}",
                f"n = {n} \\text{{ weeks}}"
            ]

        else:  # compare
            # Compare two models
            plan_a_initial = 100
            plan_a_weekly = 20
            plan_b_initial = 50
            plan_b_weekly = 30
            weeks = 5

            latex = f"\\text{{Plan A: }} \\${plan_a_initial} \\text{{ + }} \\${plan_a_weekly}\\text{{/week. "
            latex += f"\\text{{Plan B: }} \\${plan_b_initial} \\text{{ + }} \\${plan_b_weekly}\\text{{/week. "
            latex += f"\\text{{Which has more after }} {weeks} \\text{{ weeks?}}"

            total_a = plan_a_initial + weeks * plan_a_weekly
            total_b = plan_b_initial + weeks * plan_b_weekly

            if total_a > total_b:
                solution = f"Plan A (${total_a})"
            else:
                solution = f"Plan B (${total_b})"

            steps = [
                f"\\text{{Plan A: }} \\${plan_a_initial} + {weeks} \\times \\${plan_a_weekly} = \\${total_a}",
                f"\\text{{Plan B: }} \\${plan_b_initial} + {weeks} \\times \\${plan_b_weekly} = \\${total_b}",
                f"\\text{{Answer: }} {solution}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex multi-step problems"""
        problem_types = ['optimization', 'break_even', 'compound_interest', 'decay_half_life']
        problem_type = random.choice(problem_types)

        if problem_type == 'optimization':
            # Find optimal strategy
            initial = 1000
            option_a_rate = 1.1  # 10% growth
            option_b_add = 150  # $150 per period
            periods = 5

            latex = f"\\text{{Option A: }} \\${initial} \\text{{ growing 10\\%/period. "
            latex += f"\\text{{Option B: }} \\${initial} \\text{{ + }} \\${option_b_add}\\text{{/period. "
            latex += f"\\text{{Which is better after }} {periods} \\text{{ periods?}}"

            # Option A: geometric
            final_a = int(initial * (option_a_rate ** periods))
            # Option B: arithmetic
            final_b = initial + periods * option_b_add

            if final_a > final_b:
                solution = f"Option A (${final_a})"
            else:
                solution = f"Option B (${final_b})"

            steps = [
                f"\\text{{Option A (geometric): }} \\${initial} \\times 1.1^{periods} = \\${final_a}",
                f"\\text{{Option B (arithmetic): }} \\${initial} + {periods} \\times \\${option_b_add} = \\${final_b}",
                f"\\text{{Better option: }} {solution}"
            ]

        elif problem_type == 'break_even':
            # When do two models become equal?
            plan_a_initial = 200
            plan_a_monthly = 10
            plan_b_initial = 100
            plan_b_monthly = 30

            latex = f"\\text{{Plan A: }} \\${plan_a_initial} \\text{{ + }} \\${plan_a_monthly}\\text{{/month. "
            latex += f"\\text{{Plan B: }} \\${plan_b_initial} \\text{{ + }} \\${plan_b_monthly}\\text{{/month. "
            latex += f"\\text{{After how many months are they equal?}}"

            # plan_a_initial + n * plan_a_monthly = plan_b_initial + n * plan_b_monthly
            # n * (plan_b_monthly - plan_a_monthly) = plan_a_initial - plan_b_initial
            n = (plan_a_initial - plan_b_initial) // (plan_b_monthly - plan_a_monthly)
            solution = n

            steps = [
                f"{plan_a_initial} + {plan_a_monthly}n = {plan_b_initial} + {plan_b_monthly}n",
                f"{plan_b_monthly - plan_a_monthly}n = {plan_a_initial - plan_b_initial}",
                f"n = {n} \\text{{ months}}"
            ]

        elif problem_type == 'compound_interest':
            # Compound interest as geometric sequence
            principal = random.choice([5000, 10000])
            rate = 0.06  # 6%
            years = 4

            latex = f"\\text{{Investment: }} \\${principal} \\text{{ at 6\\% annual compound interest. "
            latex += f"\\text{{Value after }} {years} \\text{{ years?}}"

            final = int(principal * ((1 + rate) ** years))
            solution = final

            steps = [
                f"\\text{{Compound interest: }} A = P(1 + r)^t",
                f"A = \\${principal} \\times 1.06^{years}",
                f"A = \\${final}"
            ]

        else:  # decay_half_life
            # Radioactive decay / half-life
            initial = random.choice([800, 1600, 3200])
            half_lives = random.randint(2, 4)

            latex = f"\\text{{Substance starts at }} {initial}\\text{{g, half-life is 1 year. "
            latex += f"\\text{{Amount after }} {half_lives} \\text{{ years?}}"

            final = initial // (2 ** half_lives)
            solution = final

            steps = [
                f"\\text{{Each year: amount is halved}}",
                f"\\text{{Geometric with }} r = 0.5",
                f"\\text{{Amount: }} {initial} \\times 0.5^{half_lives} = {final}\\text{{g}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )

