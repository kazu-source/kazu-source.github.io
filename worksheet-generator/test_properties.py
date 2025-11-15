"""
Test script for properties of equality worksheets.
"""

import os
from properties_generator import PropertiesOfEqualityGenerator
from pdf_generator import PDFWorksheetGenerator

# Create test_output directory if it doesn't exist
TEST_OUTPUT_DIR = "test_output"
os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

def test_properties_worksheet():
    """Test properties of equality worksheet generation."""
    print("=" * 60)
    print("Testing Properties of Equality Worksheet")
    print("=" * 60)
    print()

    # Test mixed (addition and subtraction)
    print("1. Testing MIXED (addition and subtraction) - 10 problems...")
    generator = PropertiesOfEqualityGenerator()
    problems = generator.generate_worksheet('medium', 10, 'mixed')

    pdf_gen = PDFWorksheetGenerator()
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_mixed.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                               title="Properties of Equality - Mixed",
                               include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (mixed addition/subtraction)")
    print(f"  - 2 columns x 5 rows layout")
    print()

    # Test addition only
    print("2. Testing ADDITION only - 10 problems...")
    problems = generator.generate_worksheet('medium', 10, 'addition')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_addition.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                               title="Addition Property of Equality",
                               include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (addition only)")
    print()

    # Test subtraction only
    print("3. Testing SUBTRACTION only - 10 problems...")
    problems = generator.generate_worksheet('medium', 10, 'subtraction')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_subtraction.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                               title="Subtraction Property of Equality",
                               include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (subtraction only)")
    print()

    # Test different difficulty levels
    print("4. Testing EASY difficulty...")
    problems = generator.generate_worksheet('easy', 10, 'mixed')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_easy.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                               title="Properties of Equality - Easy",
                               include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print()

    print("5. Testing HARD difficulty...")
    problems = generator.generate_worksheet('hard', 10, 'mixed')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_hard.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                               title="Properties of Equality - Hard",
                               include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print()

    print("=" * 60)
    print("All properties worksheet tests completed!")
    print("=" * 60)
    print()
    print("Check the following in the generated PDFs:")
    print("  1. Each problem shows: Given equation, Operation, Blank line for answer")
    print("  2. Answer key shows the result in RED")
    print("  3. Layout is 2 columns x 5 rows")
    print("  4. Dynamic spacing works correctly")

if __name__ == "__main__":
    test_properties_worksheet()
