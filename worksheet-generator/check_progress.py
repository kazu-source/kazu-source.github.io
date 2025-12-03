"""
Progress Tracker for High School Worksheet Generators
Run this anytime to see current progress: python check_progress.py
"""

import os
from collections import defaultdict

# Expected topics per unit (from Excel)
EXPECTED = {
    "Geometry": {
        1: 5, 2: 5, 3: 8, 4: 7, 5: 9, 6: 5, 7: 4, 8: 13, 9: 4
    },
    "Algebra_2": {
        1: 4, 2: 6, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 8, 10: 5, 11: 7, 12: 3
    },
    "IM1": {
        1: 12, 2: 8, 3: 3, 4: 7, 5: 3, 6: 7, 7: 11, 8: 11, 9: 3
    }
}

def count_generators():
    base_path = os.path.join(os.path.dirname(__file__), "generators", "High_School")
    results = {}

    for course in ["Geometry", "Algebra_2", "IM1"]:
        course_path = os.path.join(base_path, course)
        results[course] = defaultdict(int)

        if os.path.exists(course_path):
            for item in os.listdir(course_path):
                if item.startswith("Unit_"):
                    unit_num = int(item.split("_")[1])
                    unit_path = os.path.join(course_path, item)
                    if os.path.isdir(unit_path):
                        gen_count = len([f for f in os.listdir(unit_path) if f.endswith("_generator.py")])
                        results[course][unit_num] = gen_count

    return results

def display_progress():
    results = count_generators()

    print("\n" + "=" * 70)
    print("  HIGH SCHOOL WORKSHEET GENERATOR PROGRESS")
    print("=" * 70)

    grand_total_done = 0
    grand_total_expected = 0

    for course in ["Geometry", "Algebra_2", "IM1"]:
        expected = EXPECTED[course]
        actual = results[course]

        course_done = sum(actual.values())
        course_expected = sum(expected.values())
        grand_total_done += course_done
        grand_total_expected += course_expected

        pct = (course_done / course_expected * 100) if course_expected > 0 else 0
        bar_len = 30
        filled = int(bar_len * course_done / course_expected)
        bar = "#" * filled + "-" * (bar_len - filled)

        print(f"\n  {course.replace('_', ' ')}")
        print(f"  [{bar}] {course_done}/{course_expected} ({pct:.0f}%)")
        print("  " + "-" * 50)

        for unit in sorted(expected.keys()):
            exp = expected[unit]
            act = actual.get(unit, 0)
            status = "DONE" if act >= exp else f"{act}/{exp}"
            unit_bar_len = 15
            unit_filled = min(int(unit_bar_len * act / exp), unit_bar_len) if exp > 0 else 0
            unit_bar = "#" * unit_filled + "-" * (unit_bar_len - unit_filled)
            print(f"    Unit {unit:2d}: [{unit_bar}] {status}")

    print("\n" + "=" * 70)
    grand_pct = (grand_total_done / grand_total_expected * 100) if grand_total_expected > 0 else 0
    bar_len = 40
    filled = int(bar_len * grand_total_done / grand_total_expected)
    bar = "#" * filled + "-" * (bar_len - filled)
    print(f"  OVERALL: [{bar}] {grand_total_done}/{grand_total_expected} ({grand_pct:.0f}%)")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    display_progress()
