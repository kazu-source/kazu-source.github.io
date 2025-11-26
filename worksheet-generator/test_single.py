"""Test script to debug Grade 3 worksheet generation"""
import sys

# Test one generator directly
from generators.K_8.Grade_3.Unit03.adding_with_regrouping_within_1000_generator import AddingWithRegroupingWithin1000Generator
from pdf_generator import PDFWorksheetGenerator

try:
    print("Creating generator...")
    gen = AddingWithRegroupingWithin1000Generator()

    print("Generating problems...")
    problems = gen.generate_worksheet('easy', 8)

    print(f"Generated {len(problems)} problems")
    print(f"First problem: {problems[0]}")

    print("\nGenerating PDF...")
    pdf_gen = PDFWorksheetGenerator()
    pdf_gen.generate_worksheet(
        problems,
        "test_output.pdf",
        title="Test Worksheet",
        include_answer_key=True
    )
    print("PDF generated successfully!")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
