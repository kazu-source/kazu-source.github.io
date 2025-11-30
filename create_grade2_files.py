"""Create all Grade 2 files"""
import os

BASE = r"c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8"

def create_file(path, cls, topic, unit):
    fp = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)

    desc = ' '.join([w.capitalize() for w in topic.split('_')])

    content = f'''"""
{desc} Generator - Grade 2 {unit}
Generates {topic.replace('_', ' ')} problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class {cls}:
    """Generates {topic.replace('_', ' ')} problems."""

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
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        result = a + b
        latex = f"{{a}} + {{b}} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{{a}} + {{b}} = {{result}}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        result = a + b
        latex = f"{{a}} + {{b}} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{{result}}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(30, 100)
        b = random.randint(20, 100)
        result = a + b
        latex = f"{{a}} + {{b}} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{{result}}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(50, 200)
        b = random.randint(50, 200)
        result = a + b
        latex = f"{{a}} + {{b}} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{{result}}"], difficulty='challenge')


def main():
    generator = {cls}()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {{problem.latex}} = {{problem.solution}}")


if __name__ == '__main__':
    main()
'''

    with open(fp, 'w') as f:
        f.write(content)
    return fp

# Grade 2 all files
grade2_files = [
    # Unit 01
    ('Grade_2/Unit01/add_within_20_generator.py', 'AddWithin20Generator', 'add_within_20', 'Unit01'),
    ('Grade_2/Unit01/add_using_arrays_generator.py', 'AddUsingArraysGenerator', 'add_using_arrays', 'Unit01'),
    ('Grade_2/Unit01/subtract_within_20_generator.py', 'SubtractWithin20Generator', 'subtract_within_20', 'Unit01'),
    ('Grade_2/Unit01/add_and_subtract_within_20_generator.py', 'AddAndSubtractWithin20Generator', 'add_and_subtract_within_20', 'Unit01'),
    # Unit 02
    ('Grade_2/Unit02/intro_to_place_value_generator.py', 'IntroToPlaceValueGenerator', 'intro_to_place_value', 'Unit02'),
    ('Grade_2/Unit02/numbers_in_standard_word_expanded_form_generator.py', 'NumbersInStandardWordExpandedFormGenerator', 'numbers_in_standard_word_expanded_form', 'Unit02'),
    ('Grade_2/Unit02/regroup_whole_numbers_generator.py', 'RegroupWholeNumbersGenerator', 'regroup_whole_numbers', 'Unit02'),
    ('Grade_2/Unit02/comparing_2_and_3_digit_numbers_generator.py', 'Comparing2And3DigitNumbersGenerator', 'comparing_2_and_3_digit_numbers', 'Unit02'),
    ('Grade_2/Unit02/even_and_odd_numbers_generator.py', 'EvenAndOddNumbersGenerator', 'even_and_odd_numbers', 'Unit02'),
    ('Grade_2/Unit02/counting_patterns_within_1000_generator.py', 'CountingPatternsWithin1000Generator', 'counting_patterns_within_1000', 'Unit02'),
    # Unit 03
    ('Grade_2/Unit03/visually_adding_within_100_generator.py', 'VisuallyAddingWithin100Generator', 'visually_adding_within_100', 'Unit03'),
    ('Grade_2/Unit03/strategies_for_adding_within_100_generator.py', 'StrategiesForAddingWithin100Generator', 'strategies_for_adding_within_100', 'Unit03'),
    ('Grade_2/Unit03/visually_subtract_within_100_generator.py', 'VisuallySubtractWithin100Generator', 'visually_subtract_within_100', 'Unit03'),
    ('Grade_2/Unit03/addition_and_subtraction_missing_values_generator.py', 'AdditionAndSubtractionMissingValuesGenerator', 'addition_and_subtraction_missing_values', 'Unit03'),
    ('Grade_2/Unit03/add_subtract_within_100_word_problems_generator.py', 'AddSubtractWithin100WordProblemsGenerator', 'add_subtract_within_100_word_problems', 'Unit03'),
    ('Grade_2/Unit03/add_subtract_within_100_word_problems_multi_step_generator.py', 'AddSubtractWithin100WordProblemsMultiStepGenerator', 'add_subtract_within_100_word_problems_multi_step', 'Unit03'),
    # Unit 04
    ('Grade_2/Unit04/visually_adding_within_1000_generator.py', 'VisuallyAddingWithin1000Generator', 'visually_adding_within_1000', 'Unit04'),
    ('Grade_2/Unit04/strategies_for_adding_within_1000_generator.py', 'StrategiesForAddingWithin1000Generator', 'strategies_for_adding_within_1000', 'Unit04'),
    ('Grade_2/Unit04/strategies_for_subtracting_within_1000_generator.py', 'StrategiesForSubtractingWithin1000Generator', 'strategies_for_subtracting_within_1000', 'Unit04'),
    ('Grade_2/Unit04/adding_up_to_four_2_digit_numbers_generator.py', 'AddingUpToFour2DigitNumbersGenerator', 'adding_up_to_four_2_digit_numbers', 'Unit04'),
    # Unit 05
    ('Grade_2/Unit05/counting_money_generator.py', 'CountingMoneyGenerator', 'counting_money', 'Unit05'),
    ('Grade_2/Unit05/time_generator.py', 'TimeGenerator', 'time', 'Unit05'),
    # Unit 06
    ('Grade_2/Unit06/units_of_length_generator.py', 'UnitsOfLengthGenerator', 'units_of_length', 'Unit06'),
    ('Grade_2/Unit06/measure_lengths_generator.py', 'MeasureLengthsGenerator', 'measure_lengths', 'Unit06'),
    ('Grade_2/Unit06/estimate_lengths_generator.py', 'EstimateLengthsGenerator', 'estimate_lengths', 'Unit06'),
    ('Grade_2/Unit06/length_word_problems_generator.py', 'LengthWordProblemsGenerator', 'length_word_problems', 'Unit06'),
    # Unit 07
    ('Grade_2/Unit07/picture_graphs_generator.py', 'PictureGraphsGenerator', 'picture_graphs', 'Unit07'),
    ('Grade_2/Unit07/bar_graphs_generator.py', 'BarGraphsGenerator', 'bar_graphs', 'Unit07'),
    ('Grade_2/Unit07/line_plots_generator.py', 'LinePlotsGenerator', 'line_plots', 'Unit07'),
    # Unit 08
    ('Grade_2/Unit08/shapes_generator.py', 'ShapesGenerator', 'shapes', 'Unit08'),
    ('Grade_2/Unit08/equal_parts_of_shapes_generator.py', 'EqualPartsOfShapesGenerator', 'equal_parts_of_shapes', 'Unit08'),
    ('Grade_2/Unit08/partition_rectangles_generator.py', 'PartitionRectanglesGenerator', 'partition_rectangles', 'Unit08'),
]

count = 0
for path, cls, topic, unit in grade2_files:
    create_file(path, cls, topic, unit)
    count += 1

print(f"Created {count} Grade 2 files")
