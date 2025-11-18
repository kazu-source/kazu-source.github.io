# Font Size Standards

This document defines the standard font sizes for all worksheets in the WhyMath worksheet generator.

## Standard Font Sizes

- **Problem Numbers**: 12pt Lexend (with Helvetica fallback)
- **Equations**: 21pt Lexend (rendered via matplotlib LaTeX)
- **Font Ratio**: 1.75x (equation font is 1.75 times the problem number font)

## Rationale

The 1.75x ratio (12pt → 21pt) provides:
- Clear visual hierarchy between problem numbers and equations
- Excellent readability for mathematical notation
- Proper vertical alignment when using minimal padding (0.005")
- Consistent appearance across all worksheet types

## Implementation

### Problem Numbers
Set in `pdf_generator.py` wherever problem numbers are rendered:
```python
c.setFont("Lexend", 12)  # Problem numbers
```

### Equations
Set in `pdf_generator.py` for LaTeX rendering:
```python
img = self.render_latex_to_image(equation_latex, 21)  # Equations
```

### Class Constants
Defined at the class level in `PDFWorksheetGenerator`:
```python
PROBLEM_NUMBER_FONT_SIZE = 12  # Lexend 12pt
EQUATION_FONT_SIZE = 21  # Lexend 21pt (1.75x ratio)
```

## Maintaining the Standard

When creating new worksheet types:

1. Use `PROBLEM_NUMBER_FONT_SIZE` constant for all problem numbers
2. Use `EQUATION_FONT_SIZE` constant for all equation rendering
3. If you need to adjust font sizes, maintain the 1.75x ratio
4. Update this document if ratio changes

## Current Worksheet Types

All the following worksheet types use this standard:

**Equation-based worksheets** (equations rendered as LaTeX images):
- Linear Equations
- Systems of Equations (Algebraic)
- Inequalities
- Properties of Equality (Add/Subtract)
- Properties of Equality (Mult/Div)
- Multi-step Equations
- Word Problems

**Graphing worksheets** (equations shown as text above graphs):
- Graphing Points (point labels use smaller font)
- Graphing Systems (equations use 21pt)
- Graphing Parabolas (equations use 21pt)

## Visual Alignment

The standard includes vertical alignment settings:
- Padding in LaTeX image rendering: 0.005 inches
- Vertical offset for single equations: -0.11 inches
- Image height for 21pt equations: 0.28 inches

These settings ensure equations align vertically with problem numbers at the baseline.
