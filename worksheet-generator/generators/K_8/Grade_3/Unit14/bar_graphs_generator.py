"""
Bar Graphs Generator - Grade 3 Unit 14
Generates problems for reading and interpreting bar graphs
Focuses on data interpretation with scaled bar graphs
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class BarGraphsGenerator:
    """Generates bar graph problems."""

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

    def _create_dataset(self, num_categories: int, min_val: int, max_val: int):
        """Create a dataset for graph problems."""
        category_sets = [
            ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            ['January', 'February', 'March', 'April', 'May'],
            ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Pears'],
            ['Red', 'Blue', 'Green', 'Yellow', 'Purple'],
            ['Soccer', 'Basketball', 'Baseball', 'Tennis', 'Swimming']
        ]

        category_set = random.choice(category_sets)
        categories = random.sample(category_set, min(num_categories, len(category_set)))
        values = [random.randint(min_val, max_val) for _ in range(len(categories))]
        return list(zip(categories, values))

    def _generate_easy(self) -> Equation:
        """Generate easy problems: reading bar heights with scale of 1."""
        dataset = self._create_dataset(3, 3, 10)
        scale = 1

        # Create graph representation
        graph_text = f"Bar Graph (Scale: Each unit = {scale}):\\n"
        for category, value in dataset:
            graph_text += f"{category}: Bar height = {value}\\n"

        # Ask simple reading question
        target_category = random.choice(dataset)

        latex = f"\\text{{{graph_text}What is the value for {target_category[0]}?}}"
        solution = str(target_category[1])

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Read the bar height for {target_category[0]}: {target_category[1]}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: reading with scales other than 1."""
        dataset = self._create_dataset(4, 10, 50)
        scale = random.choice([2, 5, 10])

        # Adjust values to be multiples of scale
        dataset = [(cat, (val // scale) * scale) for cat, val in dataset]

        # Create graph representation
        graph_text = f"Bar Graph (Scale: Each unit = {scale}):\\n"
        for category, value in dataset:
            bar_height = value // scale
            graph_text += f"{category}: Bar height = {bar_height} units\\n"

        question_type = random.choice(['read', 'compare'])

        if question_type == 'read':
            target_category = random.choice(dataset)
            bar_height = target_category[1] // scale
            latex = f"\\text{{{graph_text}What value does {target_category[0]} represent?}}"
            solution = str(target_category[1])
            steps = [f"\\text{{{bar_height} units \\times {scale} = {target_category[1]}}}"]
        else:
            # Find highest/lowest
            if random.choice([True, False]):
                target = max(dataset, key=lambda x: x[1])
                question = "which category has the highest value"
            else:
                target = min(dataset, key=lambda x: x[1])
                question = "which category has the lowest value"

            latex = f"\\text{{{graph_text}Based on the graph, {question}?}}"
            solution = target[0]
            steps = [f"\\text{{{target[0]} has value {target[1]}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: calculations using graph data."""
        dataset = self._create_dataset(4, 20, 60)
        scale = random.choice([5, 10])

        # Adjust values to be multiples of scale
        dataset = [(cat, (val // scale) * scale) for cat, val in dataset]

        # Create graph representation
        graph_text = f"Bar Graph (Scale: Each unit = {scale}):\\n"
        for category, value in dataset:
            bar_height = value // scale
            graph_text += f"{category}: Bar height = {bar_height} units\\n"

        question_type = random.choice(['sum', 'difference'])

        if question_type == 'sum':
            # Sum of two categories
            cat1, cat2 = random.sample(dataset, 2)
            total = cat1[1] + cat2[1]

            latex = f"\\text{{{graph_text}What is the combined value of {cat1[0]} and {cat2[0]}?}}"
            solution = str(total)
            steps = [f"\\text{{{cat1[1]} + {cat2[1]} = {total}}}"]
        else:
            # Difference between two categories
            cat1, cat2 = random.sample(dataset, 2)
            if cat1[1] > cat2[1]:
                diff = cat1[1] - cat2[1]
                latex = f"\\text{{{graph_text}How much greater is {cat1[0]} than {cat2[0]}?}}"
            else:
                diff = cat2[1] - cat1[1]
                latex = f"\\text{{{graph_text}How much greater is {cat2[0]} than {cat1[0]}?}}"

            solution = str(diff)
            steps = [f"\\text{{Difference: {max(cat1[1], cat2[1])} - {min(cat1[1], cat2[1])} = {diff}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step reasoning and analysis."""
        dataset = self._create_dataset(5, 30, 90)
        scale = 10

        # Adjust values to be multiples of scale
        dataset = [(cat, (val // scale) * scale) for cat, val in dataset]

        # Create graph representation
        graph_text = f"Bar Graph (Scale: Each unit = {scale}):\\n"
        for category, value in dataset:
            bar_height = value // scale
            graph_text += f"{category}: Bar height = {bar_height} units\\n"

        question_type = random.choice(['total', 'average', 'range'])

        if question_type == 'total':
            # Sum of all categories
            total = sum(val for _, val in dataset)
            latex = f"\\text{{{graph_text}What is the total of all categories?}}"
            solution = str(total)
            steps = [f"\\text{{Total: {' + '.join(str(v) for _, v in dataset)} = {total}}}"]
        elif question_type == 'average':
            # Average (mean) of values
            total = sum(val for _, val in dataset)
            avg = total // len(dataset)
            latex = f"\\text{{{graph_text}What is the average value? (Round to nearest {scale})}}"
            solution = str(avg)
            steps = [
                f"\\text{{Total: {total}}}",
                f"\\text{{Average: {total} \\div {len(dataset)} \\approx {avg}}}"
            ]
        else:
            # Range (difference between max and min)
            max_cat = max(dataset, key=lambda x: x[1])
            min_cat = min(dataset, key=lambda x: x[1])
            range_val = max_cat[1] - min_cat[1]

            latex = f"\\text{{{graph_text}What is the range of the data (difference between highest and lowest)?}}"
            solution = str(range_val)
            steps = [
                f"\\text{{Highest: {max_cat[0]} = {max_cat[1]}}}",
                f"\\text{{Lowest: {min_cat[0]} = {min_cat[1]}}}",
                f"\\text{{Range: {max_cat[1]} - {min_cat[1]} = {range_val}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = BarGraphsGenerator()

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
