"""
Exponential Growth and Decay Generator - Unit 8
Generates word problems and applications involving exponential growth and decay
"""

import random
import math
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class GrowthDecayProblem:
    """Represents an exponential growth or decay problem."""
    latex: str  # LaTeX formatted problem
    solution: str  # The answer
    difficulty: str
    problem_type: str  # 'growth' or 'decay'
    context: str  # Context of the problem (population, investment, etc.)


class ExponentialGrowthDecayGenerator:
    """Generates problems about exponential growth and decay."""

    def __init__(self, seed=None):
        """Initialize the exponential growth/decay generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[GrowthDecayProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of GrowthDecayProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> GrowthDecayProblem:
        """Generate a single growth/decay problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> GrowthDecayProblem:
        """Generate easy growth/decay problems (simple doubling/halving)."""
        problem_type = random.choice(['simple_growth', 'simple_decay', 'identify_type'])

        if problem_type == 'simple_growth':
            # Population doubling
            initial = random.choice([100, 200, 500, 1000])
            doublings = random.randint(1, 3)
            final = initial * (2 ** doublings)
            time_period = random.choice(["year", "month", "day"])

            latex = f"\\text{{A bacteria population of {initial} doubles every {time_period}. "
            latex += f"What is the population after {doublings} {time_period}{'s' if doublings > 1 else ''}?}}"
            solution = str(final)
            context = "bacteria_growth"

        elif problem_type == 'simple_decay':
            # Radioactive half-life
            initial = random.choice([100, 200, 400, 800])
            halvings = random.randint(1, 3)
            final = initial / (2 ** halvings)

            latex = f"\\text{{A radioactive sample has {initial}g initially. "
            latex += f"After {halvings} half-life period{'s' if halvings > 1 else ''}, how much remains?}}"
            solution = f"{final}g"
            context = "radioactive_decay"

        else:  # identify_type
            # Identify growth or decay from description
            scenarios = [
                ("A population increases by 20% each year", "growth", "exponential growth"),
                ("A car loses 15% of its value each year", "decay", "exponential decay"),
                ("Bacteria triple every hour", "growth", "exponential growth"),
                ("Medicine concentration halves every 4 hours", "decay", "exponential decay")
            ]
            scenario, answer, full_answer = random.choice(scenarios)

            latex = f"\\text{{Identify as growth or decay: {scenario}}}"
            solution = full_answer
            context = "identification"

        return GrowthDecayProblem(
            latex=latex,
            solution=solution,
            difficulty='easy',
            problem_type=problem_type if problem_type != 'identify_type' else answer,
            context=context if 'context' in locals() else 'general'
        )

    def _generate_medium(self) -> GrowthDecayProblem:
        """Generate medium growth/decay problems (percentage growth/decay)."""
        problem_type = random.choice(['percent_growth', 'percent_decay', 'find_percent'])

        if problem_type == 'percent_growth':
            # Population or investment growth
            initial = random.choice([1000, 2000, 5000, 10000])
            percent = random.choice([5, 10, 15, 20, 25])
            years = random.randint(2, 5)
            rate = 1 + percent/100
            final = initial * (rate ** years)

            contexts = [
                ("population", "people"),
                ("investment", "dollars"),
                ("bacteria culture", "cells")
            ]
            context_name, unit = random.choice(contexts)

            latex = f"\\text{{A {context_name} of {initial:,} {unit} grows at {percent}\\% per year. "
            latex += f"Find the amount after {years} years.}}"
            solution = f"{final:,.0f} {unit}"
            context = context_name

        elif problem_type == 'percent_decay':
            # Depreciation or decay
            initial = random.choice([10000, 20000, 50000])
            percent = random.choice([10, 15, 20, 25])
            years = random.randint(2, 4)
            rate = 1 - percent/100
            final = initial * (rate ** years)

            contexts = [
                ("car", "value"),
                ("computer", "value"),
                ("equipment", "value")
            ]
            item, measure = random.choice(contexts)

            latex = f"\\text{{A {item} worth \\${initial:,} depreciates at {percent}\\% per year. "
            latex += f"Find its {measure} after {years} years.}}"
            solution = f"\\${final:,.2f}"
            context = f"{item}_depreciation"

        else:  # find_percent
            # Find growth/decay rate from data
            initial = random.choice([1000, 2000, 5000])
            percent = random.choice([5, 10, 15, 20])
            is_growth = random.choice([True, False])

            if is_growth:
                rate = 1 + percent/100
                final = initial * rate
                problem_word = "grew to"
            else:
                rate = 1 - percent/100
                final = initial * rate
                problem_word = "decreased to"

            latex = f"\\text{{A quantity of {initial} {problem_word} {final:.0f} in one year. "
            latex += f"Find the percent {'increase' if is_growth else 'decrease'}.}}"
            solution = f"{percent}\\%"
            context = "find_rate"

        return GrowthDecayProblem(
            latex=latex,
            solution=solution,
            difficulty='medium',
            problem_type='growth' if 'growth' in problem_type or (problem_type == 'find_percent' and is_growth) else 'decay',
            context=context
        )

    def _generate_hard(self) -> GrowthDecayProblem:
        """Generate hard growth/decay problems (finding time, comparing models)."""
        problem_type = random.choice(['find_time', 'compare_models', 'real_world'])

        if problem_type == 'find_time':
            # Find when population reaches target
            initial = random.choice([1000, 2000, 5000])
            percent = random.choice([10, 15, 20])
            rate = 1 + percent/100
            multiplier = random.choice([2, 3, 4])  # Double, triple, quadruple
            target = initial * multiplier

            # t = log(multiplier) / log(rate)
            time = math.log(multiplier) / math.log(rate)

            word_map = {2: "double", 3: "triple", 4: "quadruple"}
            latex = f"\\text{{A population of {initial:,} grows at {percent}\\% per year. "
            latex += f"How long until it will {word_map[multiplier]}?}}"
            solution = f"{time:.1f} years"
            context = "population_time"

        elif problem_type == 'compare_models':
            # Compare two growth scenarios
            init1 = random.choice([1000, 2000])
            rate1 = random.choice([1.08, 1.10, 1.12])
            init2 = random.choice([1500, 2500])
            rate2 = random.choice([1.05, 1.06, 1.07])

            # Find when they're equal: init1 * rate1^t = init2 * rate2^t
            # This requires numerical solution, so we'll ask for values at specific time
            time = random.randint(5, 15)
            val1 = init1 * (rate1 ** time)
            val2 = init2 * (rate2 ** time)

            latex = f"\\text{{City A: {init1:,} people growing at {int((rate1-1)*100)}\\% per year. "
            latex += f"City B: {init2:,} people growing at {int((rate2-1)*100)}\\% per year. "
            latex += f"Compare populations after {time} years.}}"
            solution = f"City A: {val1:,.0f}, City B: {val2:,.0f}"
            context = "city_comparison"

        else:  # real_world
            # Carbon dating or medicine concentration
            if random.choice([True, False]):
                # Carbon dating
                half_life = 5730  # C-14 half-life in years
                percent_remaining = random.choice([75, 50, 25, 12.5])
                age = -half_life * math.log(percent_remaining/100) / math.log(2)

                latex = f"\\text{{A fossil has {percent_remaining}\\% of its original C-14. "
                latex += f"If C-14 half-life is {half_life} years, find the fossil's age.}}"
                solution = f"{age:,.0f} years"
                context = "carbon_dating"
            else:
                # Medicine concentration
                initial_dose = random.choice([100, 200, 500])
                half_life_hours = random.choice([4, 6, 8])
                hours = random.choice([8, 12, 16, 24])
                remaining = initial_dose * (0.5 ** (hours / half_life_hours))

                latex = f"\\text{{A {initial_dose}mg dose of medicine has a half-life of {half_life_hours} hours. "
                latex += f"How much remains after {hours} hours?}}"
                solution = f"{remaining:.1f}mg"
                context = "medicine_decay"

        return GrowthDecayProblem(
            latex=latex,
            solution=solution,
            difficulty='hard',
            problem_type='growth' if 'growth' in context or 'comparison' in context else 'decay',
            context=context
        )

    def _generate_challenge(self) -> GrowthDecayProblem:
        """Generate challenge growth/decay problems (continuous growth, complex applications)."""
        problem_type = random.choice(['continuous_compound', 'newton_cooling', 'logistic_growth'])

        if problem_type == 'continuous_compound':
            # Continuous compound interest A = Pe^(rt)
            principal = random.choice([5000, 10000, 20000])
            rate = random.choice([0.03, 0.04, 0.05, 0.06])
            time = random.randint(5, 20)
            amount = principal * math.exp(rate * time)

            latex = f"\\text{{\\${principal:,} is invested at {rate*100:.0f}\\% annual interest, "
            latex += f"compounded continuously for {time} years. Find the amount.}}"
            solution = f"\\${amount:,.2f}"
            context = "continuous_interest"

        elif problem_type == 'newton_cooling':
            # Newton's Law of Cooling
            room_temp = random.choice([20, 22, 25])
            initial_temp = random.choice([80, 90, 100])
            cooling_const = random.choice([0.1, 0.15, 0.2])
            time = random.randint(10, 30)

            # T(t) = room_temp + (initial_temp - room_temp) * e^(-kt)
            temp = room_temp + (initial_temp - room_temp) * math.exp(-cooling_const * time)

            latex = f"\\text{{Coffee at {initial_temp}°C cools in a {room_temp}°C room. "
            latex += f"With cooling constant k = {cooling_const}, find temperature after {time} minutes.}}"
            solution = f"{temp:.1f}°C"
            context = "newton_cooling"

        else:  # logistic_growth
            # Simplified logistic growth problem
            carrying_capacity = random.choice([10000, 20000, 50000])
            initial = random.choice([1000, 2000, 5000])
            growth_rate = random.choice([0.5, 0.8, 1.0])
            time = random.randint(2, 5)

            # Simplified: just check if approaching carrying capacity
            if initial < carrying_capacity * 0.1:
                # Early stage - approximately exponential
                approx_pop = initial * math.exp(growth_rate * time)
                if approx_pop > carrying_capacity:
                    approx_pop = carrying_capacity * 0.9
            else:
                # Later stage - slowing down
                remaining_capacity = carrying_capacity - initial
                growth = remaining_capacity * (1 - math.exp(-growth_rate * time))
                approx_pop = initial + growth * 0.5

            latex = f"\\text{{A population starts at {initial:,} with carrying capacity {carrying_capacity:,}. "
            latex += f"With growth rate r = {growth_rate}, estimate population after {time} years.}}"
            solution = f"Approximately {approx_pop:,.0f}"
            context = "logistic_growth"

        return GrowthDecayProblem(
            latex=latex,
            solution=solution,
            difficulty='challenge',
            problem_type='growth' if 'growth' in context or 'interest' in context else 'decay',
            context=context
        )


if __name__ == "__main__":
    # Test the generator
    gen = ExponentialGrowthDecayGenerator()

    print("Testing Exponential Growth and Decay Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Type: {problem.problem_type}")
            print(f"   Context: {problem.context}")