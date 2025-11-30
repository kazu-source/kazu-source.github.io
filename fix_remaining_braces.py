"""
Manually fix remaining brace errors by replacing specific problematic patterns.
"""

import re

# List of files with specific line patterns to fix
fixes = [
    # Kindergarten
    (r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Kindergarten\Unit01\counting_up_to_3_generator.py',
     [
         (r'f"\\text\{\{There are \}\} {count} \\text\{\{ circle\(s\)\}\}\}"', r'f"\\text{{{{There are }}}} {count} \\text{{{{ circle(s)}}}}"'),
         (r'\\text\{\{There is \}\} 1 \\text\{\{ shape\}\}\}"', r'\\text{{{{There is }}}} 1 \\text{{{{ shape}}}}"'),
         (r'f"\\text\{\{Find all circles \(ignore squares\)\}\}\}"', r'f"\\text{{{{Find all circles (ignore squares)}}}}"'),
     ]),
]

# Actually, let's use a simpler approach - search and replace ALL instances of these patterns:
#  }}}}} -> }}}} (but only when preceded by something that looks like a variable)
# {{{{ {var}}}} -> {{ {var} }}

def fix_file(filepath):
    """Fix a specific file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Fix pattern: \\text{{{{ LITERAL_OR_VAR }}}}} where there are 5 closing braces
        # This should be: \\text{{{{ LITERAL_OR_VAR }}}}
        content = re.sub(r'(\\text\{\{)\{\{([^{}]+?)\}\}\}\}\}', r'\1{{\2}}}}', content)

        # Fix pattern: {{{{ {var}}}} -> {{ {var} }}
        # Match: \\text{{{{ {something} }}}}
        # Replace with: \\text{{ {something} }}
        content = re.sub(r'\\text\{\{\{\{(\s*)(\{[^}]+\})(\s*)\}\}\}\}', r'\\text{{ \\2 }}', content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

# Get list of failing files from the test output
failing_files = [
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_1\Unit08\comparing_lengths_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_1\Unit08\measuring_with_non_standard_units_generator.py',
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
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_5\Unit04\fractions_word_problems_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_6\Unit03\intro_to_rates_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_8\Unit01\arithmetic_with_scientific_notation_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_8\Unit01\exponent_properties_integer_exponents_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_8\Unit01\exponent_properties_intro_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_8\Unit01\negative_exponents_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_8\Unit01\square_and_cube_roots_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_8\Unit01\working_with_powers_of_10_generator.py',
    r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8\Grade_8\Unit03\graphing_proportional_relationships_generator.py',
]

fixed_count = 0
for filepath in failing_files:
    if fix_file(filepath):
        fixed_count += 1
        print(f"Fixed: {filepath}")

print(f"\nFixed {fixed_count} files out of {len(failing_files)}")
