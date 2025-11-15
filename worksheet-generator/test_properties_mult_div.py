"""
Test script for multiplication and division properties of equality worksheets.
"""

import os
from properties_mult_div_generator import PropertiesMultDivGenerator
from pdf_generator import PDFWorksheetGenerator

# Create test_output directory if it doesn't exist
TEST_OUTPUT_DIR = "test_output"
os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

def test_properties_mult_div_worksheet():
    """Test multiplication and division properties of equality worksheet generation."""
    print("=" * 60)
    print("Testing Mult/Div Properties of Equality Worksheet")
    print("=" * 60)
    print()

    # Test mixed (multiplication and division)
    print("1. Testing MIXED (multiplication and division) - 10 problems...")
    generator = PropertiesMultDivGenerator()
    problems = generator.generate_worksheet('medium', 10, 'mixed')

    pdf_gen = PDFWorksheetGenerator()
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_mult_div_mixed.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Properties of Equality - Multiplication & Division",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (mixed multiplication/division)")
    print(f"  - 2 columns x 5 rows layout")
    print()

    # Test multiplication only
    print("2. Testing MULTIPLICATION only - 10 problems...")
    problems = generator.generate_worksheet('medium', 10, 'multiplication')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_multiplication.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Multiplication Property of Equality",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (multiplication only)")
    print()

    # Test division only
    print("3. Testing DIVISION only - 10 problems...")
    problems = generator.generate_worksheet('medium', 10, 'division')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_division.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Division Property of Equality",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print(f"  - 10 problems (division only)")
    print()

    # Test different difficulty levels
    print("4. Testing EASY difficulty...")
    problems = generator.generate_worksheet('easy', 10, 'mixed')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_mult_div_easy.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Properties of Equality - Mult/Div - Easy",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print()

    print("5. Testing HARD difficulty...")
    problems = generator.generate_worksheet('hard', 10, 'mixed')
    output_file = os.path.join(TEST_OUTPUT_DIR, "test_properties_mult_div_hard.pdf")
    pdf_gen.generate_worksheet(problems, output_file,
                              title="Properties of Equality - Mult/Div - Hard",
                              include_answer_key=True)
    print(f"  [OK] Created: {output_file}")
    print()

    print("=" * 60)
    print("All mult/div properties worksheet tests completed!")
    print("=" * 60)
    print()
    print("Check the following in the generated PDFs:")
    print("  1. Each problem shows: Given equation, Operation, Blank line for answer")
    print("  2. Answer key shows the result in RED")
    print("  3. Layout is 2 columns x 5 rows")
    print("  4. Dynamic spacing works correctly")

if __name__ == "__main__":
    test_properties_mult_div_worksheet()
