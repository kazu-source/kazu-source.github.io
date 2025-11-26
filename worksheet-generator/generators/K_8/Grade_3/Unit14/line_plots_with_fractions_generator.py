"""
Line Plots with Fractions Generator - Grade 3 Unit 14
Generates problems for creating and interpreting line plots with fractional data
Focuses on fractions (halves, quarters) on number lines
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class LinePlotsWithFractionsGenerator:
    """Generates line plot with fractions problems."""

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

    def _fraction_to_string(self, numerator: int, denominator: int) -> str:
        """Convert fraction to string representation."""
        if numerator == 0:
            return "0"
        elif numerator == denominator:
            return str(numerator // denominator)
        elif numerator > denominator:
            whole = numerator // denominator
            remainder = numerator % denominator
            if remainder == 0:
                return str(whole)
            return f"{whole}\\frac{{{remainder}}}{{{denominator}}}"
        else:
            return f"\\frac{{{numerator}}}{{{denominator}}}"

    def _create_fractional_dataset(self, num_values: int, denominator: int, max_whole: int):
        """Create a dataset with fractional values."""
        values = []
        for _ in range(num_values):
            whole = random.randint(0, max_whole)
            fraction_part = random.randint(0, denominator - 1)
            total_numerator = whole * denominator + fraction_part
            values.append((total_numerator, denominator))
        return values

    def _generate_easy(self) -> Equation:
        """Generate easy problems: reading line plots with halves."""
        # Create dataset with halves
        num_values = random.randint(5, 8)
        dataset = self._create_fractional_dataset(num_values, 2, 2)

        # Count occurrences
        from collections import Counter
        counts = Counter(dataset)

        # Create line plot representation
        plot_text = "Line Plot (Measurements in inches):\\n"
        for (num, den) in sorted(set(dataset)):
            fraction_str = self._fraction_to_string(num, den)
            count = counts[(num, den)]
            plot_text += f"At {fraction_str}: {'X' * count}\\n"

        question_type = random.choice(['count', 'most_common'])

        if question_type == 'count':
            target = random.choice(list(set(dataset)))
            fraction_str = self._fraction_to_string(target[0], target[1])
            latex = f"\\text{{{plot_text}How many measurements are at {fraction_str} inches?}}"
            solution = str(counts[target])
            steps = [f"\\text{{Count X's at {fraction_str}: {counts[target]}}}"]
        else:
            most_common = counts.most_common(1)[0][0]
            fraction_str = self._fraction_to_string(most_common[0], most_common[1])
            latex = f"\\text{{{plot_text}Which measurement appears most often?}}"
            solution = fraction_str
            steps = [f"\\text{{Most common: {fraction_str} inches}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: line plots with quarters."""
        # Create dataset with quarters
        num_values = random.randint(6, 10)
        dataset = self._create_fractional_dataset(num_values, 4, 2)

        # Count occurrences
        from collections import Counter
        counts = Counter(dataset)

        # Create line plot representation
        plot_text = "Line Plot (Pencil lengths in inches):\\n"
        for (num, den) in sorted(set(dataset)):
            fraction_str = self._fraction_to_string(num, den)
            count = counts[(num, den)]
            plot_text += f"At {fraction_str}: {'X' * count}\\n"

        question_type = random.choice(['total_count', 'range'])

        if question_type == 'total_count':
            total = len(dataset)
            latex = f"\\text{{{plot_text}How many pencils were measured in total?}}"
            solution = str(total)
            steps = [f"\\text{{Count all X's: {total}}}"]
        else:
            # Find range
            min_val = min(dataset)
            max_val = max(dataset)
            min_str = self._fraction_to_string(min_val[0], min_val[1])
            max_str = self._fraction_to_string(max_val[0], max_val[1])

            latex = f"\\text{{{plot_text}What is the difference between the longest and shortest pencil?}}"
            diff_num = max_val[0] * min_val[1] - min_val[0] * max_val[1]
            diff_den = min_val[1] * max_val[1]
            # Simplify (for quarters to quarters)
            diff_num = (max_val[0] - min_val[0])
            diff_den = 4
            diff_str = self._fraction_to_string(diff_num, diff_den)
            solution = f"{diff_str} inches"
            steps = [f"\\text{{Difference: {max_str} - {min_str} = {diff_str} inches}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: creating line plots or analyzing data."""
        # Create dataset with halves or quarters
        denominator = random.choice([2, 4])
        num_values = random.randint(8, 12)
        dataset = self._create_fractional_dataset(num_values, denominator, 3)

        # Count occurrences
        from collections import Counter
        counts = Counter(dataset)

        # Create line plot representation
        unit = random.choice(['inches', 'feet', 'pounds'])
        plot_text = f"Line Plot (Measurements in {unit}):\\n"
        for (num, den) in sorted(set(dataset)):
            fraction_str = self._fraction_to_string(num, den)
            count = counts[(num, den)]
            plot_text += f"At {fraction_str}: {'X' * count}\\n"

        question_type = random.choice(['greater_than', 'sum_category'])

        if question_type == 'greater_than':
            # Count values greater than a threshold
            threshold = random.choice(sorted(set(dataset))[:-1])
            threshold_str = self._fraction_to_string(threshold[0], threshold[1])

            count_greater = sum(1 for (num, den) in dataset if num / den > threshold[0] / threshold[1])

            latex = f"\\text{{{plot_text}How many measurements are greater than {threshold_str} {unit}?}}"
            solution = str(count_greater)
            steps = [f"\\text{{Count values > {threshold_str}: {count_greater}}}"]
        else:
            # Sum all values of a specific measurement
            target = random.choice(list(set(dataset)))
            count = counts[target]
            fraction_str = self._fraction_to_string(target[0], target[1])

            latex = f"\\text{{{plot_text}If you add all measurements at {fraction_str} {unit}, what is the total?}}"
            total_num = target[0] * count
            total_den = target[1]
            total_str = self._fraction_to_string(total_num, total_den)
            solution = f"{total_str} {unit}"
            steps = [f"\\text{{{count} \\times {fraction_str} = {total_str} {unit}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: complex analysis of line plot data."""
        # Create dataset with quarters
        num_values = random.randint(10, 15)
        dataset = self._create_fractional_dataset(num_values, 4, 3)

        # Count occurrences
        from collections import Counter
        counts = Counter(dataset)

        # Create line plot representation
        plot_text = "Line Plot (Plant heights in feet):\\n"
        for (num, den) in sorted(set(dataset)):
            fraction_str = self._fraction_to_string(num, den)
            count = counts[(num, den)]
            plot_text += f"At {fraction_str}: {'X' * count}\\n"

        question_type = random.choice(['total_sum', 'mode_count'])

        if question_type == 'total_sum':
            # Sum all measurements
            total_num = sum(num for num, den in dataset)
            total_den = 4
            total_str = self._fraction_to_string(total_num, total_den)

            latex = f"\\text{{{plot_text}What is the total height of all plants combined?}}"
            solution = f"{total_str} feet"
            steps = [f"\\text{{Sum all measurements: {total_str} feet}}"]
        else:
            # Find mode and its count
            mode = counts.most_common(1)[0]
            mode_str = self._fraction_to_string(mode[0][0], mode[0][1])
            mode_count = mode[1]

            # Count how many are at mode
            latex = f"\\text{{{plot_text}The most common height is {mode_str} feet. How many plants have this height?}}"
            solution = str(mode_count)
            steps = [f"\\text{{Plants at {mode_str} feet: {mode_count}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = LinePlotsWithFractionsGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
