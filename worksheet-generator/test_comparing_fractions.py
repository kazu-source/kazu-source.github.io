"""Test comparing fractions generator"""
import time
from generators.K_8.Grade_3.Unit06.comparing_fractions_generator import ComparingFractionsGenerator
from pdf_generator import PDFWorksheetGenerator

try:
    print("Creating generator...")
    gen = ComparingFractionsGenerator()

    print("Generating problems...")
    start = time.time()
    problems = gen.generate_worksheet('easy', 8)
    gen_time = time.time() - start
    print(f"Generated {len(problems)} problems in {gen_time:.2f}s")

    for i, p in enumerate(problems, 1):
        print(f"{i}. {p.latex}")

    print("\nGenerating PDF...")
    start = time.time()
    pdf_gen = PDFWorksheetGenerator()
    pdf_gen.generate_worksheet(
        problems,
        "test_comparing_fractions.pdf",
        title="Test - Comparing Fractions",
        include_answer_key=True
    )
    pdf_time = time.time() - start
    print(f"PDF generated in {pdf_time:.2f}s")
    print(f"Total time: {gen_time + pdf_time:.2f}s")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
