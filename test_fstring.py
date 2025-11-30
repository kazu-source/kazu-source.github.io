unit1 = 'miles'
numerator = 120
denominator = 2
unit2 = 'hour'

print("Testing f-string patterns...")

# Test 1: Simple \text{ VAR }
result1 = f"\\text{{ {unit1} }}"
print(f"Test 1: {repr(result1)}")

# Test 2: \text with doubled braces for literal
result2 = f"\\text{{{{ literal }}}}"
print(f"Test 2: {repr(result2)}")

# Test 3: Can we do \text{{ VAR }}? NO - this would be unbalanced
# result3 = f"\\text{{{{ {unit1} }}}}"  # This will fail

# Test 4: The RIGHT way - \text{{ }} produces \text{ } in output
# So for \text{VAR} we just need \text{{VAR}}
result4 = f"\\text{{{unit1}}}"
print(f"Test 4: {repr(result4)}")

# Test 5: For \text{ VAR } we need \text{{ VAR }}
result5 = f"\\text{{ {unit1} }}"
print(f"Test 5: {repr(result5)}")

# Test 6: Now try \frac{A}{B}
result6 = f"\\frac{{{numerator}}}{{{denominator}}}"
print(f"Test 6: {repr(result6)}")

# Test 7: \frac{A \text{ UNIT1 }}{B \text{ UNIT2 }}
result7 = f"\\frac{{{numerator} \\text{{ {unit1} }}}}{{{denominator} \\text{{ {unit2} }}}}"
print(f"Test 7: {repr(result7)}")

# Test 8: \frac{A \text{UNIT1}}{B \text{UNIT2s}}
result8 = f"\\frac{{{numerator} \\text{{{unit1}}}}}{{{denominator} \\text{{{unit2}s}}}}"
print(f"Test 8: {repr(result8)}")
