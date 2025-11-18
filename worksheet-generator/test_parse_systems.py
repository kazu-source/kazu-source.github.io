"""Test the system equation parsing."""

import re

def parse_system_equation(eq: str):
    """Parse a system equation into components."""

    # Split at equals sign
    if '=' not in eq:
        return None

    left, right = eq.split('=', 1)
    left = left.strip()
    right = right.strip()

    result = {
        'x_coef': '',
        'y_sign': '+',
        'y_coef': '',
        'constant': right
    }

    print(f"\nParsing: {eq}")
    print(f"  Left side: '{left}'")
    print(f"  Right side: '{right}'")

    # Find x term - match optional sign and coefficient before x
    x_match = re.search(r'([+-]?\s*\d*)\s*x', left)
    if x_match:
        coef = x_match.group(1).replace(' ', '')
        print(f"  X match: '{coef}'")
        if coef == '' or coef == '+':
            result['x_coef'] = '1'
        elif coef == '-':
            result['x_coef'] = '-1'
        else:
            result['x_coef'] = coef

    # Find y term - match sign and coefficient after x
    y_match = re.search(r'x\s*([+-])\s*(\d*)\s*y', left)
    if y_match:
        result['y_sign'] = y_match.group(1)
        coef = y_match.group(2)
        result['y_coef'] = coef if coef else '1'
        print(f"  Y match: sign='{result['y_sign']}', coef='{result['y_coef']}'")

    print(f"  Result: {result}")
    return result

# Test cases
test_equations = [
    "2x + 3y = 13",
    "x - y = -1",
    "5x + 4y = 24",
    "6x + 2y = 80",
    "4x - 6y = 24"
]

for eq in test_equations:
    parse_system_equation(eq)
