# Math Worksheet Generator

A desktop application for generating printable math worksheets with answer keys.

## Features
- **Multiple Problem Types**: Linear equations, systems of equations, and inequalities
- **4 Difficulty Levels** for each problem type
- **Professional PDFs** with LaTeX-rendered equations
- **Visual Number Lines** for inequalities showing solution regions
- **Answer Keys** on separate page
- **Smart GUI Interface**: Auto-updates worksheet title AND default problem count based on problem type
- **Smart Defaults**: Different problem types have different default counts based on space requirements:
  - Pure equations: 10 problems (default)
  - Inequalities (with number lines): 8 problems
  - Systems of equations (with coordinate planes): 6 problems
- **Centralized Configuration**: Easy to add new problem types with consistent rendering

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Project Structure
- `equation_generator.py` - Linear equation generation
- `systems_generator.py` - Systems of equations generation
- `inequalities_generator.py` - Inequality generation with number lines
- `pdf_generator.py` - PDF creation with LaTeX rendering and number lines
- `worksheet_config.py` - **Centralized configuration for problem types**
- `gui.py` - Desktop interface (Tkinter)
- `main.py` - Entry point
- `test_all_types.py` - Testing script for all problem types

## Architecture Highlights

**Centralized Configuration**: The `worksheet_config.py` file contains all rendering settings (font sizes, spacing, layout) for each problem type. This makes it easy to add new problem types without worrying about font sizing issues - just add a configuration entry and the PDF generator handles the rest!

## Problem Types & Difficulty Levels

### Linear Equations
1. **Easy**: One-step equations (x + 5 = 12, 3x = 15)
2. **Medium**: Two-step equations (2x + 3 = 11)
3. **Hard**: Multi-step equations (3(x + 2) - 5 = 10)
4. **Challenge**: Variables on both sides (2x + 3 = x + 7)

### Systems of Equations
1. **Easy**: One variable already solved (substitution)
2. **Medium**: Standard form, good for elimination/substitution
3. **Hard**: Larger coefficients, requires multiplication
4. **Challenge**: May have fraction solutions

### Inequalities
1. **Easy**: One-step inequalities (x + 5 < 12)
2. **Medium**: Two-step inequalities (2x + 3 > 11)
3. **Hard**: Multi-step with parentheses (3(x + 2) - 5 < 10)
4. **Challenge**: Variables on both sides (may require flipping direction)
- **Includes visual number lines** showing solution regions with open/closed circles and arrows
