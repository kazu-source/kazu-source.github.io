# Worksheet Generator Formatting Standards

This document defines the standardized formatting conventions for all worksheet generators. Follow these rules to ensure consistency across all worksheets.

---

## LaTeX Formatting

### Fractions
**✓ CORRECT:**
```python
latex = f"\\frac{{{numerator}}}{{{denominator}}}"
# Example: \frac{3}{4}
```

**✗ INCORRECT:**
```python
latex = f"{numerator}/{denominator}"  # Renders as division, not a fraction bar
```

**Notes:**
- Always use `\frac{}{}` for proper fraction rendering
- The PDF generator handles fraction rendering automatically
- No need to manually convert fractions to division notation

---

### Exponents
**✓ CORRECT:**
```python
# Single digit exponents
latex = f"{coef}x^2"

# Multi-digit exponents
latex = f"{coef}x^{{12}}"

# Both formats work - PDF renderer handles curly braces
```

**✗ INCORRECT:**
```python
latex = f"{coef}x**2"  # Python syntax, not LaTeX
latex = f"{coef}x^2^3"  # Ambiguous, use parentheses
```

**Notes:**
- `x^2` and `x^{2}` both work - the PDF renderer strips unnecessary braces
- For multi-character exponents, braces are required: `x^{10}`

---

### Text in LaTeX
**✓ CORRECT:**
```python
latex = f"\\text{{Is }} x = {x_val} \\text{{ a solution to }} {eq}?"
latex = f"\\text{{Sub: }} {expr} \\text{{ for }} x={val}"
```

**✗ INCORRECT:**
```python
latex = f"Is x = {x_val} a solution to {eq}?"  # Missing \text{}, renders as italics
latex = f"\\text{{Is }} x = {x_val} \\text{{ a solution to }} {eq}? \\text{{(1=Yes, 0=No)}}"  # No instructions
```

**Notes:**
- Use `\text{}` for all non-mathematical text
- **Never** include answer instructions like "(1=Yes, 0=No)" in the LaTeX
- Keep questions concise - avoid verbose explanations
- Abbreviate when space is limited: "Substitute" → "Sub"

---

### Numbers and Signs

#### Negative Numbers
**✓ CORRECT:**
```python
latex = f"x = -5"
latex = f"{-a}x + {b}"  # If a is positive, this shows -ax
```

**✗ INCORRECT:**
```python
latex = f"x = - 5"  # Extra space creates rendering issues
```

#### Positive/Negative Terms
**✓ CORRECT:**
```python
# Handle signs properly
if b >= 0:
    latex = f"{a}x + {b}"
else:
    latex = f"{a}x - {abs(b)}"
```

**✗ INCORRECT:**
```python
latex = f"{a}x + {b}"  # If b is negative, renders as "2x + -3"
```

---

### Variable Spacing
**✓ CORRECT:**
```python
# No spaces in variable assignments for compact display
latex = f"\\text{{ for }} x={x_val}, y={y_val}, z={z_val}"
```

**✗ INCORRECT:**
```python
latex = f"\\text{{ when }} x = {x_val}, y = {y_val}, z = {z_val}"  # Too wide
```

**Notes:**
- For multi-variable substitution, remove spaces to prevent text wrapping
- Use "for" instead of "when" to save space

---

### Absolute Value
**✓ CORRECT:**
```python
# Simple absolute value
latex = f"\\left|{x}\\right|"
# Example: \left|-5\right| renders as |-5|

# Absolute value equations
latex = f"\\left|x + {a}\\right| = {b}"
# Example: \left|x + 3\right| = 7

# Nested or complex expressions
latex = f"\\left|{coef}x - {const}\\right| = {result}"
```

**✗ INCORRECT:**
```python
latex = f"|{x}|"  # Plain pipes don't scale properly
latex = f"abs({x})"  # Programming syntax, not mathematical
```

**Notes:**
- Always use `\left|` and `\right|` for proper scaling
- The vertical bars will automatically adjust to expression height
- For nested absolute values, use `\left|\left|x\right| - 2\right|`

---

### Square Roots and Radicals
**✓ CORRECT:**
```python
# Simple square root
latex = f"\\sqrt{{{x}}}"
# Example: \sqrt{16}

# Square root of expression
latex = f"\\sqrt{{{coef}x + {const}}}"
# Example: \sqrt{2x + 5}

# Nth root (cube root, etc.)
latex = f"\\sqrt[3]{{{x}}}"  # Cube root
latex = f"\\sqrt[{n}]{{{x}}}"  # Nth root
# Example: \sqrt[3]{27} or \sqrt[4]{16}

# Complex radical expressions
latex = f"\\sqrt{{\\frac{{{a}}}{{{b}}}}}"
# Example: \sqrt{\frac{3}{4}}
```

**✗ INCORRECT:**
```python
latex = f"sqrt({x})"  # Programming syntax
latex = f"{x}^(1/2)"  # Technically correct but not standard notation
latex = f"√{x}"  # Unicode symbol may not render properly
```

**Notes:**
- Use `\sqrt{}` for square roots
- Use `\sqrt[n]{}` for nth roots (cube root, fourth root, etc.)
- Curly braces are required even for single digits: `\sqrt{5}`
- Can nest with fractions: `\sqrt{\frac{a}{b}}`

---

### Logarithms
**✓ CORRECT:**
```python
# Common logarithm (base 10)
latex = f"\\log({x})"
# Example: \log(100)

# Natural logarithm
latex = f"\\ln({x})"
# Example: \ln(e)

# Logarithm with custom base
latex = f"\\log_{{{base}}}({x})"
# Example: \log_{2}(8)

# Logarithmic equations
latex = f"\\log_{{{base}}}(x) = {result}"
latex = f"\\ln(x + {a}) = {b}"

# Change of base formula display
latex = f"\\frac{{\\log({x})}}{{\\log({base})}}"
```

**✗ INCORRECT:**
```python
latex = f"log({x})"  # Missing backslash, renders as "l·o·g"
latex = f"log_{base}({x})"  # Base needs curly braces
latex = f"LOG({x})"  # Uppercase is non-standard
```

**Notes:**
- `\log` for common log (base 10)
- `\ln` for natural log (base e)
- `\log_{}` requires curly braces for subscript base
- Parentheses for arguments are standard: `\log(x)` not `\log x`

---

### Factored Forms and Parentheses
**✓ CORRECT:**
```python
# Simple factored form
latex = f"({a}x + {b})({c}x + {d})"
# Example: (2x + 3)(x - 5)

# Trinomial to factored
latex = f"(x + {p})(x + {q})"
# Example: (x + 3)(x - 2)

# Difference of squares
latex = f"({a}x + {b})({a}x - {b})"
# Example: (x + 4)(x - 4)

# Perfect square trinomial
latex = f"(x + {a})^2"
# Example: (x + 3)^2

# Factoring with GCF
latex = f"{gcf}({inner_expr})"
# Example: 3(2x + 5)

# Grouping notation
latex = f"\\left({a}x + {b}\\right)\\left({c}x + {d}\\right)"
# Use \left( \right) for larger expressions
```

**✗ INCORRECT:**
```python
latex = f"{a}x + {b}{c}x + {d}"  # Missing parentheses
latex = f"[{a}x + {b}][{c}x + {d}]"  # Square brackets not standard for factors
```

**Notes:**
- Use regular parentheses `()` for most factored forms
- Use `\left( \right)` when expressions are tall (fractions, exponents)
- Always show multiplication between factors explicitly
- For GCF: `3(x + 2)` not `3*(x + 2)`

---

### Polynomials
**✓ CORRECT:**
```python
# Standard form (descending powers)
latex = f"{a}x^2 + {b}x + {c}"
# Example: 2x^2 + 5x - 3

# Higher degree polynomials
latex = f"{a}x^3 + {b}x^2 + {c}x + {d}"
# Example: x^3 - 4x^2 + 5x + 2

# Handle signs properly
if b >= 0:
    latex = f"{a}x^2 + {b}x + {c}"
else:
    latex = f"{a}x^2 - {abs(b)}x + {c}"

# Leading coefficient of 1
if a == 1:
    latex = f"x^2 + {b}x + {c}"
elif a == -1:
    latex = f"-x^2 + {b}x + {c}"
else:
    latex = f"{a}x^2 + {b}x + {c}"

# Multi-variable polynomials
latex = f"{a}x^2y + {b}xy^2 + {c}xy"
# Example: 3x^2y - 2xy^2 + 5xy
```

**✗ INCORRECT:**
```python
latex = f"{c} + {b}x + {a}x^2"  # Ascending order (non-standard)
latex = f"{a}x**2 + {b}x + {c}"  # Python exponent syntax
```

**Notes:**
- Always use descending order of exponents (highest power first)
- Handle zero coefficients by omitting those terms
- Use proper sign handling for negative coefficients
- Leading coefficient of 1 should be omitted for x term

---

### Rational Expressions (Algebraic Fractions)
**✓ CORRECT:**
```python
# Simple rational expression
latex = f"\\frac{{{numerator_expr}}}{{{denominator_expr}}}"
# Example: \frac{x + 3}{x - 2}

# Polynomial over polynomial
latex = f"\\frac{{{a}x^2 + {b}x + {c}}}{{{d}x + {e}}}"
# Example: \frac{2x^2 - 3x + 1}{x + 5}

# Factored form in fractions
latex = f"\\frac{{(x + {a})(x + {b})}}{{(x + {c})(x + {d})}}"
# Example: \frac{(x + 2)(x - 3)}{(x + 1)(x - 4)}

# Complex fractions (fraction in fraction)
latex = f"\\frac{{\\frac{{{a}}}{{{b}}}}}{{\\frac{{{c}}}{{{d}}}}}"
# Example: \frac{\frac{2}{3}}{\frac{5}{7}}

# Mixed rational expressions
latex = f"{whole} + \\frac{{{num}}}{{{den}}}"
# Example: 2 + \frac{3}{x + 1}
```

**✗ INCORRECT:**
```python
latex = f"({num})/({den})"  # Division operator, not fraction bar
latex = f"\\frac{num}{den}"  # Missing curly braces
```

**Notes:**
- Always use `\frac{}{}` for algebraic fractions
- Parentheses in numerator/denominator are handled automatically
- For complex fractions, nest `\frac{}{}` commands
- Factor when possible for clarity

---

### Quadratic Formula and Special Formulas
**✓ CORRECT:**
```python
# Quadratic formula
latex = f"x = \\frac{{-{b} \\pm \\sqrt{{{b}^2 - 4({a})({c})}}}}{{2({a})}}"
# Simplified version
latex = f"x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}"

# Distance formula
latex = f"d = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}}"

# Plus-minus symbol
latex = f"x = {val} \\pm {delta}"
# Example: x = 3 ± 2

# Discriminant
latex = f"\\Delta = b^2 - 4ac"
latex = f"b^2 - 4ac = {disc_value}"
```

**✗ INCORRECT:**
```python
latex = f"x = (-{b} +/- sqrt({b}^2 - 4*{a}*{c})) / (2*{a})"
latex = f"x = {val} ± {delta}"  # Unicode ± may not render
```

**Notes:**
- Use `\pm` for plus-minus symbol
- Use `\mp` for minus-plus symbol
- Quadratic formula should show full structure
- Use `\Delta` (capital delta) for discriminant symbol

---

### Inequalities with Special Symbols
**✓ CORRECT:**
```python
# Basic inequalities
latex = f"{a}x + {b} < {c}"  # Less than
latex = f"{a}x + {b} > {c}"  # Greater than
latex = f"{a}x + {b} \\leq {c}"  # Less than or equal
latex = f"{a}x + {b} \\geq {c}"  # Greater than or equal
latex = f"{a}x + {b} \\neq {c}"  # Not equal

# Compound inequalities
latex = f"{lower} < x < {upper}"
latex = f"{lower} \\leq x \\leq {upper}"

# Absolute value inequalities
latex = f"\\left|x - {center}\\right| < {distance}"
latex = f"\\left|{a}x + {b}\\right| \\geq {c}"
```

**✗ INCORRECT:**
```python
latex = f"{a}x + {b} <= {c}"  # Programming syntax
latex = f"{a}x + {b} ≤ {c}"  # Unicode may not render
latex = f"{a}x + {b} != {c}"  # Use \neq instead
```

**Notes:**
- Use `\leq` and `\geq` for ≤ and ≥
- Use `\neq` for ≠
- Plain `<` and `>` work without backslash
- For compound inequalities, no "and" needed: `a < x < b`

---

### Piecewise Functions
**✓ CORRECT:**
```python
# Piecewise function using cases environment
latex = f"f(x) = \\begin{{cases}} {expr1} & \\text{{if }} x < {bound} \\\\\\\\ {expr2} & \\text{{if }} x \\geq {bound} \\end{{cases}}"

# Example with three pieces
latex = f"""f(x) = \\begin{{cases}}
{a}x + {b} & \\text{{if }} x < {c1} \\\\\\\\
{d} & \\text{{if }} {c1} \\leq x < {c2} \\\\\\\\
{e}x - {f} & \\text{{if }} x \\geq {c2}
\\end{{cases}}"""
```

**Notes:**
- Use `\begin{cases}...\end{cases}` environment
- Separate pieces with `\\` (double backslash)
- Use `&` before conditions for alignment
- Include `\text{}` for "if" conditions

---

## Problem Types and Question Wording

### Yes/No Questions
**✓ CORRECT:**
```python
latex = f"Is x = {val} a solution to {eq}?"
latex = f"Does {eq} have a solution?"
```

**✗ INCORRECT:**
```python
latex = f"Verify: Is x = {val} a solution to {eq}?"  # Remove "Verify:"
latex = f"Is x = {val} a solution to {eq}? (1=Yes, 0=No)"  # No instructions
```

### Find/Solve Questions
**✓ CORRECT:**
```python
latex = f"Find x if {eq}"
latex = f"Solve: {eq}"
latex = f"Which value makes {eq} true?"
```

---

## Systems of Equations

### Format
**✓ CORRECT:**
```python
# Standard form: ax + by = c
eq1 = f"{a1}x + {b1}y = {c1}"
eq2 = f"{a2}x + {b2}y = {c2}"
```

**Notes:**
- Always use standard form `ax + by = c`
- The PDF generator handles vertical alignment automatically using LaTeX array environment
- No manual spacing or alignment needed

---

## Inequality Rendering

### Number Lines
**Current Settings:**
- Number lines are positioned 0.25 inches left of default to avoid edge overflow
- This is handled in `pdf_generator.py` - no changes needed in generators

---

## Code Style for Generators

### Random Value Ranges
```python
# Keep ranges reasonable for student comprehension
x_val = random.randint(2, 10)      # Easy: single digits
x_val = random.randint(-5, 12)     # Medium: include negatives
x_val = random.randint(-20, 20)    # Hard: wider range
```

### Difficulty Progression
- **Easy:** Single-step, small numbers, positive only
- **Medium:** Two-step, larger numbers, negatives introduced
- **Hard:** Multi-step, variables on both sides, larger coefficients
- **Challenge:** Complex expressions, multiple variables, fractions

### Solution Calculation
```python
# Always calculate solution BEFORE building latex string
solution = a * x_val + b  # Calculate first
latex = f"{a}x + {b} = {solution}"  # Then build string
```

**Why:** Ensures the equation has the expected integer solution

---

## Common Patterns

### Coefficient of 1
```python
# Handle coefficient of 1 properly
if coef == 1:
    term = "x"
elif coef == -1:
    term = "-x"
else:
    term = f"{coef}x"
```

### Building Equations with Proper Signs
```python
# Method 1: Conditional
if const >= 0:
    latex = f"{coef}x + {const} = {result}"
else:
    latex = f"{coef}x - {abs(const)} = {result}"

# Method 2: Sign variable
sign = '+' if const >= 0 else '-'
latex = f"{coef}x {sign} {abs(const)} = {result}"
```

---

## PDF Rendering Notes

### Font Sizes
- Problem numbers: 12pt
- Equations: 12pt (not 21pt as previously used)
- Title: Standard reportlab default

### Margins
- Standard: 1 inch on all sides
- Text should not extend to page edges
- This is enforced in `pdf_generator.py`

### Multi-Column Layout
- Problems are automatically arranged in columns
- The PDF generator handles spacing
- Keep problem text concise to prevent overflow

---

## Testing Standards

### Always Test With:
1. Easy difficulty (verify basic functionality)
2. Hard/Challenge difficulty (verify edge cases)
3. Generate 6+ problems (verify variety)
4. Check both worksheet and answer key

### Sample Test Code:
```python
if __name__ == "__main__":
    gen = YourGenerator()

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        problems = gen.generate_worksheet(difficulty, 5)
        for i, p in enumerate(problems, 1):
            print(f"{i}. {p.latex}")
            print(f"   Solution: {p.solution}")
```

---

## Quick Reference

### Basic Elements
| Element | Format | Example |
|---------|--------|---------|
| Fraction | `\frac{a}{b}` | `\frac{3}{4}` |
| Exponent | `x^2` or `x^{12}` | `3x^2` |
| Text | `\text{...}` | `\text{Is }` |
| Negative | No space | `x = -5` |
| Variable list | No spaces | `x=1, y=2` |
| Yes/No | No instructions | `Is x = 3 a solution?` |

### Advanced Notation
| Element | Format | Example |
|---------|--------|---------|
| Absolute value | `\left|...\right|` | `\left|x + 3\right|` |
| Square root | `\sqrt{...}` | `\sqrt{16}` |
| Nth root | `\sqrt[n]{...}` | `\sqrt[3]{27}` |
| Common log | `\log(...)` | `\log(100)` |
| Natural log | `\ln(...)` | `\ln(e)` |
| Log with base | `\log_{base}(...)` | `\log_{2}(8)` |
| Factored form | `(a)(b)` | `(x + 2)(x - 3)` |
| Polynomial | Descending powers | `2x^2 + 5x - 3` |
| Rational expr | `\frac{expr}{expr}` | `\frac{x + 1}{x - 2}` |
| Plus-minus | `\pm` | `x = 3 \pm 2` |
| Less/equal | `\leq` | `x \leq 5` |
| Greater/equal | `\geq` | `x \geq 3` |
| Not equal | `\neq` | `x \neq 0` |
| Piecewise | `\begin{cases}...\end{cases}` | See section above |

---

## Version History
- **v1.1** - Advanced notation expansion (2025-01-18)
  - Added: Absolute value (`\left|...\right|`)
  - Added: Square roots and radicals (`\sqrt{}`, `\sqrt[n]{}`)
  - Added: Logarithms (`\log`, `\ln`, `\log_{}`)
  - Added: Factored forms and parentheses
  - Added: Polynomials (standard form, descending powers)
  - Added: Rational expressions (algebraic fractions)
  - Added: Quadratic formula and special formulas (`\pm`, `\Delta`)
  - Added: Inequality symbols (`\leq`, `\geq`, `\neq`)
  - Added: Piecewise functions (`\begin{cases}...\end{cases}`)
  - Expanded: Quick reference with advanced notation table

- **v1.0** - Initial standards document (2025-01-18)
  - Fractions: Use `\frac{}{}`
  - Exponents: Both `^2` and `^{2}` supported
  - Text: Remove instruction parentheticals
  - Substitution: Use compact "for x=1, y=2" format
  - Systems: LaTeX array alignment (automatic)
