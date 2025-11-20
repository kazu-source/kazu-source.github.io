"""
Test script to verify pagination in challenge worksheets.
Checks that worksheets and answer keys have max 8 problems per page.
"""

import PyPDF2
import os
from pathlib import Path

def analyze_pdf_pagination(pdf_path):
    """Analyze a PDF to count pages and estimate problems per page."""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Extract text from each page to count problem numbers
        page_info = []
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Count problem numbers (1., 2., 3., etc.)
            problem_numbers = []
            for i in range(1, 21):  # Check for problems 1-20
                if f"{i}." in text:
                    problem_numbers.append(i)

            page_info.append({
                'page': page_num + 1,
                'problems': problem_numbers,
                'num_problems': len(problem_numbers)
            })

        return num_pages, page_info

def main():
    output_dir = Path("output/comprehensive_tests")

    # Test a few different challenge worksheets
    test_files = [
        "Unit1_Intro_Combining_Like_Terms_Challenge.pdf",
        "Unit2_Intro_Linear_Equations_Challenge.pdf",
        "Unit4_Graphing_Points_on_a_Coordinate_Plane_Challenge.pdf",
    ]

    print("=" * 80)
    print("PAGINATION TEST")
    print("=" * 80)
    print("\nTesting that challenge worksheets have max 8 problems per page...")
    print()

    for filename in test_files:
        filepath = output_dir / filename
        if not filepath.exists():
            print(f"SKIP: {filename} (not found)")
            continue

        print(f"\n{filename}")
        print("-" * 80)

        num_pages, page_info = analyze_pdf_pagination(filepath)

        print(f"Total pages: {num_pages}")

        all_problems = set()
        for info in page_info:
            all_problems.update(info['problems'])

        total_problems = len(all_problems)
        print(f"Total unique problems: {total_problems}")

        # Expected structure for 10 problems:
        # Page 1: Problems 1-8 (worksheet)
        # Page 2: Problems 9-10 (worksheet)
        # Page 3: Problems 1-8 (answer key)
        # Page 4: Problems 9-10 (answer key)

        for info in page_info:
            if info['num_problems'] > 0:
                min_prob = min(info['problems'])
                max_prob = max(info['problems'])
                print(f"  Page {info['page']}: {info['num_problems']} problems (#{min_prob}-#{max_prob})")

                # Check pagination rule: max 8 problems per page
                if info['num_problems'] > 8:
                    print(f"    FAIL: Page has {info['num_problems']} problems (max should be 8)")
                else:
                    print(f"    PASS: Page has <=8 problems")
            else:
                print(f"  Page {info['page']}: No problems detected")

        # Verify structure
        if num_pages == 2:
            print(f"\n  Expected: 2 pages (<=8 problems total)")
            print(f"  Structure correct: 1 worksheet page + 1 answer key page")
        elif num_pages == 4:
            print(f"\n  Expected: 4 pages (9-10 problems total)")
            print(f"  Structure correct: 2 worksheet pages + 2 answer key pages")
        else:
            print(f"\n  WARNING: Unexpected number of pages: {num_pages}")

if __name__ == "__main__":
    main()
