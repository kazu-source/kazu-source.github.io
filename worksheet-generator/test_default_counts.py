"""
Test script to verify default problem counts work correctly.
This tests the logic without launching the full GUI.
"""

import sys
import io

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from worksheet_config import get_config

# Mapping from display names to config keys (same as in GUI)
problem_type_map = {
    'Linear Equations': 'linear_equation',
    'Systems of Equations': 'system_of_equations',
    'Inequalities': 'inequality'
}

print("Testing Default Problem Counts")
print("=" * 60)

for display_name, config_key in problem_type_map.items():
    config = get_config(config_key)
    print(f"\n{display_name}:")
    print(f"  Config key: {config_key}")
    print(f"  Default problems: {config.default_num_problems}")
    print(f"  ✓ Expected behavior:")

    if 'Equation' in display_name and 'System' not in display_name:
        expected = 10
        reason = "Pure equations"
    elif 'System' in display_name:
        expected = 6
        reason = "Needs coordinate plane"
    elif 'Inequalities' in display_name:
        expected = 8
        reason = "Needs number line"
    else:
        expected = 10
        reason = "Default"

    print(f"    {reason} → {expected} problems")

    if config.default_num_problems == expected:
        print(f"    ✅ PASS")
    else:
        print(f"    ❌ FAIL (got {config.default_num_problems}, expected {expected})")

print("\n" + "=" * 60)
print("All tests completed!")
