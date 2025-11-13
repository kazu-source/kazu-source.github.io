"""
Quick test script to verify all components work together.
"""

from equation_generator import LinearEquationGenerator
from pdf_generator import PDFWorksheetGenerator


def test_all_difficulties():
    """Test generation for all difficulty levels."""
    generator = LinearEquationGenerator()
    pdf_gen = PDFWorksheetGenerator()

    difficulties = ['easy', 'medium', 'hard', 'challenge']

    print("Testing Math Worksheet Generator\n")
    print("=" * 50)

    for difficulty in difficulties:
        print(f"\nTesting {difficulty.upper()} difficulty:")

        # Generate equations
        equations = generator.generate_worksheet(difficulty, 10)
        print(f"  Generated {len(equations)} equations")

        # Show sample equations
        print(f"  Sample equations:")
        for i, eq in enumerate(equations[:3], 1):
            print(f"    {i}. {eq.latex} -> x = {eq.solution}")

        # Generate PDF
        output_file = f"test_{difficulty}_worksheet.pdf"
        try:
            pdf_gen.generate_worksheet(
                equations,
                output_file,
                title=f"Linear Equations - {difficulty.capitalize()}",
                include_answer_key=True
            )
            print(f"  [OK] PDF created: {output_file}")
        except Exception as e:
            print(f"  [ERROR] PDF generation failed: {e}")

    print("\n" + "=" * 50)
    print("Testing complete!")
    print("\nGenerated test PDFs:")
    for difficulty in difficulties:
        print(f"  - test_{difficulty}_worksheet.pdf")


if __name__ == "__main__":
    test_all_difficulties()
