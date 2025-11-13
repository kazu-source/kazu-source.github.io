"""
Test script for inequalities with number lines.
"""

from inequalities_generator import InequalityGenerator
from pdf_generator import PDFWorksheetGenerator


def test_inequalities():
    """Test inequality generation with number lines."""
    gen = InequalityGenerator()
    pdf_gen = PDFWorksheetGenerator()

    print("Testing Inequalities with Number Lines\n")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} difficulty:")

        # Generate inequalities
        inequalities = gen.generate_worksheet(difficulty, 10)
        print(f"  Generated {len(inequalities)} inequalities")

        # Show samples
        print(f"  Samples:")
        for i, ineq in enumerate(inequalities[:2], 1):
            print(f"    {ineq.latex}")
            print(f"    Solution: x {ineq.inequality_type} {ineq.solution}")
            print(f"    Number line: [{ineq.number_line_min}, {ineq.number_line_max}]")

        # Generate PDF
        output_file = f"test_inequalities_{difficulty}.pdf"
        try:
            pdf_gen.generate_worksheet(
                inequalities,
                output_file,
                title=f"Inequalities - {difficulty.capitalize()}",
                include_answer_key=True
            )
            print(f"  [OK] PDF created: {output_file}")
        except Exception as e:
            print(f"  [ERROR] PDF generation failed: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 60)
    print("Testing complete!")
    print("\nGenerated PDFs:")
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"  - test_inequalities_{diff}.pdf")


if __name__ == "__main__":
    test_inequalities()
