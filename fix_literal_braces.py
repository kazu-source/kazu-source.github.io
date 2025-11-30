"""
Fix the over-aggressive brace reduction.
The pattern {{{LITERAL}}} should be {{{{LITERAL}}}} when LITERAL doesn't contain variables.
"""

import os
import re

def fix_file(filepath):
    """Fix literal text patterns that were incorrectly reduced."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Pattern: \text{{{WORDS}}} where WORDS doesn't contain {
        # Should be: \text{{{{WORDS}}}}
        # Match: \text{{{ followed by text (no {) followed by }}}
        content = re.sub(r'\\text\{\{\{([^{}]+)\}\}\}', r'\\text{{{{\1}}}}', content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"Error: {e}")
        return False

# List of files with "invalid syntax" or "expecting" errors
failing_files = [
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_1\Unit10\comparing_2d_shapes_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_1\Unit10\extending_patterns_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_1\Unit10\identifying_2d_shapes_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_1\Unit10\reading_bar_graphs_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_1\Unit10\reading_picture_graphs_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_1\Unit10\recognizing_patterns_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit02\numbers_in_standard_word_expanded_form_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit05\counting_money_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit05\time_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit06\estimate_lengths_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit06\length_word_problems_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit06\measure_lengths_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit06\units_of_length_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit07\bar_graphs_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit07\line_plots_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit07\picture_graphs_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit08\partition_rectangles_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_2\Unit08\shapes_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit01\decimals_on_number_line_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit01\decimals_written_form_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit01\decimal_place_value_intro_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit01\rounding_decimals_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit02\adding_decimals_intro_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit02\adding_decimals_tenths_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit02\common_fractions_decimals_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit03\subtracting_decimals_intro_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit03\subtracting_decimals_tenths_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit04\common_denominators_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit04\fractions_unlike_denominators_strategies_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit04\fractions_word_problems_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit05\multi_digit_division_estimation_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit05\multi_digit_multiplication_estimation_generator.py',
]

fixed = 0
for filepath in failing_files:
    if fix_file(filepath):
        fixed += 1
        print(f"Fixed: {os.path.basename(filepath)}")

print(f"\nFixed {fixed}/{len(failing_files)} files")
