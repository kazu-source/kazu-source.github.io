"""Test all Grade 3 Unit 7-8 generators."""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import all generators
from generators.K_8.Grade_3.Unit07.letters_and_symbols_in_multiplication_and_division_equations_generator import LettersAndSymbolsGenerator
from generators.K_8.Grade_3.Unit07.multiplication_and_division_word_problems_generator import MultiplicationDivisionWordProblemsGenerator
from generators.K_8.Grade_3.Unit07.associative_property_of_multiplication_generator import AssociativePropertyGenerator
from generators.K_8.Grade_3.Unit07.multiplying_by_tens_generator import MultiplyingByTensGenerator

# Unit 8 - need to import using importlib due to filename starting with number
import importlib.util

def load_two_step_gen():
    spec = importlib.util.spec_from_file_location(
        "two_step_gen",
        os.path.join(os.path.dirname(__file__), "generators", "K_8", "Grade_3", "Unit08", "2_step_expressions_generator.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.TwoStepExpressionsGenerator

from generators.K_8.Grade_3.Unit08.estimation_word_problems_generator import EstimationWordProblemsGenerator
from generators.K_8.Grade_3.Unit08.one_and_two_step_word_problems_generator import OneAndTwoStepWordProblemsGenerator

TwoStepExpressionsGenerator = load_two_step_gen()

generators = [
    ('Unit07: Letters and Symbols', LettersAndSymbolsGenerator),
    ('Unit07: Mult/Div Word Problems', MultiplicationDivisionWordProblemsGenerator),
    ('Unit07: Associative Property', AssociativePropertyGenerator),
    ('Unit07: Multiplying by Tens', MultiplyingByTensGenerator),
    ('Unit08: Two-Step Expressions', TwoStepExpressionsGenerator),
    ('Unit08: Estimation Word Problems', EstimationWordProblemsGenerator),
    ('Unit08: One/Two-Step Word Problems', OneAndTwoStepWordProblemsGenerator),
]

print('Testing all 7 Grade 3 Unit 7-8 generators with all difficulty levels...')
print('=' * 70)

success_count = 0
for name, GeneratorClass in generators:
    try:
        gen = GeneratorClass(seed=42)
        for diff in ['easy', 'medium', 'hard', 'challenge']:
            problems = gen.generate_worksheet(diff, 1)
            assert len(problems) == 1, f"Expected 1 problem, got {len(problems)}"
            assert problems[0].solution is not None, "Solution is None"
            assert problems[0].latex is not None, "Latex is None"
            assert problems[0].steps is not None, "Steps is None"
        print(f'[PASS] {name} - All difficulties work!')
        success_count += 1
    except Exception as e:
        print(f'[FAIL] {name} - ERROR: {e}')
        import traceback
        traceback.print_exc()

print('=' * 70)
print(f'Result: {success_count}/7 generators passed all tests!')

if success_count == 7:
    print('\n[SUCCESS] All generators successfully created and tested!')
