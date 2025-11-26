"""
Picture Graphs Generator - Grade 3 Unit 14
Generates problems for reading and interpreting picture graphs
Focuses on data interpretation with symbols representing values
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PictureGraphsGenerator:
    """Generates picture graph problems."""

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
        categories = random.sample([
            'Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries',
            'Red', 'Blue', 'Green', 'Yellow', 'Purple',
            'Dogs', 'Cats', 'Birds', 'Fish', 'Rabbits',
            'Soccer', 'Basketball', 'Baseball', 'Tennis', 'Swimming'
        ], num_categories)

        values = [random.randint(min_val, max_val) for _ in range(num_categories)]
        return list(zip(categories, values))

    def _generate_easy(self) -> Equation:
        """Generate easy problems: reading values with each symbol = 1."""
        dataset = self._create_dataset(3, 2, 8)
        symbol = random.choice(['star', 'heart', 'smiley face', 'apple', 'book'])

        # Create graph representation
        graph_text = f"Picture Graph (Each {symbol} = 1):\\n"
        for category, value in dataset:
            graph_text += f"{category}: {value} {symbol}s\\n"

        # Ask simple reading question
        target_category = random.choice(dataset)

        latex = f"\\text{{{graph_text}How many {symbol}s are shown for {target_category[0]}?}}"
        solution = str(target_category[1])

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Count the {symbol}s for {target_category[0]}: {target_category[1]}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: symbols represent values other than 1."""
        dataset = self._create_dataset(4, 10, 40)
        symbol = random.choice(['star', 'heart', 'circle', 'square', 'triangle'])
        symbol_value = random.choice([2, 5, 10])

        # Adjust values to be multiples of symbol_value
        dataset = [(cat, (val // symbol_value) * symbol_value) for cat, val in dataset]

        # Create graph representation
        graph_text = f"Picture Graph (Each {symbol} = {symbol_value}):\\n"
        for category, value in dataset:
            num_symbols = value // symbol_value
            graph_text += f"{category}: {num_symbols} {symbol}s\\n"

        question_type = random.choice(['read', 'compare'])

        if question_type == 'read':
            target_category = random.choice(dataset)
            latex = f"\\text{{{graph_text}How many does {target_category[0]} represent?}}"
            solution = str(target_category[1])
            steps = [f"\\text{{{target_category[1] // symbol_value} {symbol}s \\times {symbol_value} = {target_category[1]}}}"]
        else:
            # Find most/least
            if random.choice([True, False]):
                target = max(dataset, key=lambda x: x[1])
                question = "which category has the most"
            else:
                target = min(dataset, key=lambda x: x[1])
                question = "which category has the least"

            latex = f"\\text{{{graph_text}Based on the graph, {question}?}}"
            solution = target[0]
            steps = [f"\\text{{{target[0]} has {target[1]}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: calculations using graph data."""
        dataset = self._create_dataset(4, 15, 35)
        symbol = random.choice(['star', 'heart', 'circle', 'flower'])
        symbol_value = random.choice([5, 10])

        # Adjust values to be multiples of symbol_value
        dataset = [(cat, (val // symbol_value) * symbol_value) for cat, val in dataset]

        # Create graph representation
        graph_text = f"Picture Graph (Each {symbol} = {symbol_value}):\\n"
        for category, value in dataset:
            num_symbols = value // symbol_value
            graph_text += f"{category}: {num_symbols} {symbol}s\\n"

        question_type = random.choice(['total', 'difference'])

        if question_type == 'total':
            # Sum of two categories
            cat1, cat2 = random.sample(dataset, 2)
            total = cat1[1] + cat2[1]

            latex = f"\\text{{{graph_text}How many {cat1[0]} and {cat2[0]} combined?}}"
            solution = str(total)
            steps = [f"\\text{{{cat1[1]} + {cat2[1]} = {total}}}"]
        else:
            # Difference between two categories
            cat1, cat2 = random.sample(dataset, 2)
            if cat1[1] > cat2[1]:
                diff = cat1[1] - cat2[1]
                latex = f"\\text{{{graph_text}How many more {cat1[0]} than {cat2[0]}?}}"
            else:
                diff = cat2[1] - cat1[1]
                latex = f"\\text{{{graph_text}How many more {cat2[0]} than {cat1[0]}?}}"

            solution = str(diff)
            steps = [f"\\text{{Difference: {max(cat1[1], cat2[1])} - {min(cat1[1], cat2[1])} = {diff}}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step reasoning."""
        dataset = self._create_dataset(5, 20, 50)
        symbol = random.choice(['star', 'heart', 'circle', 'square'])
        symbol_value = random.choice([5, 10])

        # Adjust values to be multiples of symbol_value
        dataset = [(cat, (val // symbol_value) * symbol_value) for cat, val in dataset]

        # Create graph representation
        graph_text = f"Picture Graph (Each {symbol} = {symbol_value}):\\n"
        for category, value in dataset:
            num_symbols = value // symbol_value
            graph_text += f"{category}: {num_symbols} {symbol}s\\n"

        question_type = random.choice(['total_all', 'average', 'ratio'])

        if question_type == 'total_all':
            # Sum of all categories
            total = sum(val for _, val in dataset)
            latex = f"\\text{{{graph_text}What is the total of all categories?}}"
            solution = str(total)
            steps = [f"\\text{{Total: {' + '.join(str(v) for _, v in dataset)} = {total}}}"]
        elif question_type == 'average':
            # Average (mean) of values
            total = sum(val for _, val in dataset)
            avg = total // len(dataset)
            latex = f"\\text{{{graph_text}What is the average value? (Round to nearest whole number)}}"
            solution = str(avg)
            steps = [
                f"\\text{{Total: {total}}}",
                f"\\text{{Average: {total} \\div {len(dataset)} = {avg}}}"
            ]
        else:
            # Ratio comparison
            cat1, cat2 = random.sample(dataset, 2)
            if cat1[1] > cat2[1]:
                times = cat1[1] // cat2[1] if cat2[1] != 0 else 1
                latex = f"\\text{{{graph_text}About how many times more {cat1[0]} than {cat2[0]}?}}"
            else:
                times = cat2[1] // cat1[1] if cat1[1] != 0 else 1
                latex = f"\\text{{{graph_text}About how many times more {cat2[0]} than {cat1[0]}?}}"

            solution = str(times)
            steps = [f"\\text{{Ratio: approximately {times} times}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = PictureGraphsGenerator()

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
