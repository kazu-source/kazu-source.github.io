"""
Progress Tracker for All Worksheet Generators
Run this anytime to see current progress: python check_progress.py
"""

import os
from collections import defaultdict

# Expected topics per unit (from Excel files)

# K-8 Expected counts
K8_EXPECTED = {
    "Kindergarten": {
        1: 5, 2: 3, 3: 3, 4: 2, 5: 2, 6: 2, 7: 3, 8: 5, 9: 4, 10: 4
    },
    "Grade_1": {
        1: 3, 2: 4, 3: 4, 4: 3, 5: 4, 6: 3, 7: 3, 8: 4, 9: 4, 10: 6
    },
    "Grade_2": {
        1: 4, 2: 6, 3: 6, 4: 4, 5: 2, 6: 4, 7: 3, 8: 3
    },
    "Grade_3": {
        1: 2, 2: 6, 3: 6, 4: 5, 5: 3, 6: 3, 7: 4, 8: 3, 9: 1, 10: 3, 11: 2, 12: 2, 13: 2, 14: 3
    },
    "Grade_4": {
        1: 6, 2: 3, 3: 5, 4: 4, 5: 8, 6: 3, 7: 4, 8: 8, 9: 4, 10: 10, 11: 6, 12: 3, 13: 1, 14: 8
    },
    "Grade_5": {
        1: 7, 2: 4, 3: 3, 4: 5, 5: 4
    },
    "Grade_6": {
        1: 4, 2: 8, 3: 6, 4: 5, 5: 7, 6: 14, 7: 9, 8: 3, 9: 3, 10: 5, 11: 10, 12: 4
    },
    "Grade_7": {
        1: 6, 2: 3, 3: 6, 4: 5, 5: 9, 6: 8, 7: 4, 8: 2, 9: 7
    },
    "Grade_8": {
        1: 11, 2: 4, 3: 13, 4: 5, 5: 7, 6: 7, 7: 4, 8: 1
    }
}

# High School Expected counts
HS_EXPECTED = {
    "Algebra": {
        1: 23, 2: 21, 3: 12, 4: 8, 5: 2, 6: 5, 7: 4, 8: 10, 9: 13, 10: 5, 11: 2, 12: 4, 13: 4, 14: 3
    },
    "Geometry": {
        1: 5, 2: 5, 3: 8, 4: 7, 5: 9, 6: 5, 7: 4, 8: 13, 9: 4
    },
    "Algebra_2": {
        1: 4, 2: 6, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 8, 10: 5, 11: 7, 12: 3
    },
    "IM1": {
        1: 12, 2: 8, 3: 3, 4: 7, 5: 3, 6: 7, 7: 11, 8: 11, 9: 3
    },
    "IM2": {
        1: 2, 2: 8, 3: 8, 4: 3, 5: 6, 6: 5, 7: 3, 8: 7, 9: 8, 10: 4, 11: 8, 12: 5, 13: 8
    },
    "IM3": {
        1: 6, 2: 7, 3: 4, 4: 4, 5: 6, 6: 8, 7: 6, 8: 8, 9: 5, 10: 2, 11: 1, 12: 1, 13: 8
    },
    "AP_Statistics": {
        1: 5, 2: 4, 3: 8, 4: 7, 5: 7, 6: 7, 7: 4, 8: 7, 9: 7, 10: 9, 11: 5, 12: 2, 13: 2, 14: 1
    },
    "Calculus": {
        1: 7, 2: 6, 3: 8, 4: 8, 5: 3, 6: 8, 7: 3, 8: 2, 9: 8, 10: 7, 11: 7, 12: 8, 13: 3,
        14: 4, 15: 2, 16: 1, 17: 3, 18: 1, 19: 1, 20: 1, 21: 6, 22: 2, 23: 5, 24: 4, 25: 1, 26: 1
    }
}


def count_k8_generators():
    """Count generators in K-8 folder."""
    base_path = os.path.join(os.path.dirname(__file__), "generators", "K_8")
    results = {}

    for grade in K8_EXPECTED.keys():
        grade_path = os.path.join(base_path, grade)
        results[grade] = defaultdict(int)

        if os.path.exists(grade_path):
            for item in os.listdir(grade_path):
                if item.startswith("Unit"):
                    unit_path = os.path.join(grade_path, item)
                    if os.path.isdir(unit_path):
                        # Handle both Unit01 and Unit_1 formats
                        unit_num_str = item.replace("Unit", "").replace("_", "")
                        try:
                            unit_num = int(unit_num_str)
                            gen_count = len([f for f in os.listdir(unit_path) if f.endswith("_generator.py")])
                            results[grade][unit_num] = gen_count
                        except ValueError:
                            pass

    return results


def count_hs_generators():
    """Count generators in High School folder."""
    base_path = os.path.join(os.path.dirname(__file__), "generators", "High_School")
    results = {}

    for course in HS_EXPECTED.keys():
        course_path = os.path.join(base_path, course)
        results[course] = defaultdict(int)

        if os.path.exists(course_path):
            for item in os.listdir(course_path):
                if item.startswith("Unit_"):
                    unit_path = os.path.join(course_path, item)
                    if os.path.isdir(unit_path):
                        unit_num = int(item.split("_")[1])
                        gen_count = len([f for f in os.listdir(unit_path) if f.endswith("_generator.py")])
                        results[course][unit_num] = gen_count

    return results


def display_section(title, expected_dict, results, show_units=True):
    """Display progress for a section (K-8 or High School)."""
    section_done = 0
    section_expected = 0

    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print("=" * 70)

    for name in expected_dict.keys():
        expected = expected_dict[name]
        actual = results.get(name, {})

        course_done = sum(actual.values())
        course_expected = sum(expected.values())
        section_done += course_done
        section_expected += course_expected

        pct = (course_done / course_expected * 100) if course_expected > 0 else 0
        bar_len = 30
        filled = int(bar_len * min(course_done, course_expected) / course_expected) if course_expected > 0 else 0
        bar = "#" * filled + "-" * (bar_len - filled)

        display_name = name.replace("_", " ")
        print(f"\n  {display_name}")
        print(f"  [{bar}] {course_done}/{course_expected} ({pct:.0f}%)")

        if show_units:
            print("  " + "-" * 50)
            for unit in sorted(expected.keys()):
                exp = expected[unit]
                act = actual.get(unit, 0)
                status = "DONE" if act >= exp else f"{act}/{exp}"
                unit_bar_len = 15
                unit_filled = min(int(unit_bar_len * act / exp), unit_bar_len) if exp > 0 else 0
                unit_bar = "#" * unit_filled + "-" * (unit_bar_len - unit_filled)
                print(f"    Unit {unit:2d}: [{unit_bar}] {status}")

    return section_done, section_expected


def display_progress(show_units=True):
    """Display progress for all grade levels."""
    k8_results = count_k8_generators()
    hs_results = count_hs_generators()

    grand_total_done = 0
    grand_total_expected = 0

    # K-8 Section
    k8_done, k8_expected = display_section("K-8 WORKSHEET GENERATORS", K8_EXPECTED, k8_results, show_units)
    grand_total_done += k8_done
    grand_total_expected += k8_expected

    print(f"\n  K-8 Subtotal: {k8_done}/{k8_expected}")

    # High School Section
    hs_done, hs_expected = display_section("HIGH SCHOOL WORKSHEET GENERATORS", HS_EXPECTED, hs_results, show_units)
    grand_total_done += hs_done
    grand_total_expected += hs_expected

    print(f"\n  High School Subtotal: {hs_done}/{hs_expected}")

    # Grand Total
    print("\n" + "=" * 70)
    grand_pct = (grand_total_done / grand_total_expected * 100) if grand_total_expected > 0 else 0
    bar_len = 40
    filled = int(bar_len * grand_total_done / grand_total_expected) if grand_total_expected > 0 else 0
    bar = "#" * filled + "-" * (bar_len - filled)
    print(f"  GRAND TOTAL: [{bar}] {grand_total_done}/{grand_total_expected} ({grand_pct:.0f}%)")
    print("=" * 70 + "\n")


def display_summary():
    """Display a compact summary without unit details."""
    display_progress(show_units=False)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--summary":
        display_summary()
    else:
        display_progress()
