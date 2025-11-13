# Usage Guide - Math Worksheet Generator

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

or with user flag if you encounter permissions issues:
```bash
python -m pip install --user -r requirements.txt
```

### 2. Run the Application
```bash
python main.py
```

This will launch the GUI application.

## Using the GUI

1. **Select Problem Type**: Choose from the dropdown
   - Linear Equations
   - Systems of Equations
   - *The worksheet title and difficulty descriptions automatically update when you change this*

2. **Select Difficulty Level**: Choose from the dropdown (descriptions change based on problem type)
   - **Easy**
   - **Medium**
   - **Hard**
   - **Challenge**

3. **Set Number of Problems**: Use the spinner to select 5-20 problems (default: 10)

4. **Customize Worksheet Title**: Edit the title field (auto-updates based on problem type, but you can customize it)

5. **Include Answer Key**: Check/uncheck to include answer key on a separate page

6. **Generate**: Click "Generate Worksheet" button and choose where to save the PDF

### Smart Features

- **Auto-updating Title**: The worksheet title automatically updates when you change either the problem type or difficulty level
  - Examples: "Linear Equations - Medium", "Systems of Equations - Hard", "Linear Equations - Challenge"
  - Title format: `{Problem Type} - {Difficulty}`
  - You can still manually edit the title if desired
- **Context-aware Descriptions**: Difficulty level descriptions change based on the selected problem type
- **Consistent Rendering**: All problem types use optimized font sizes and spacing automatically

## Testing

To test all components without using the GUI:

```bash
python test_generator.py
```

This will create sample PDFs for all difficulty levels.

## Code Structure

### equation_generator.py
Contains the `LinearEquationGenerator` class that creates random linear equations:
- `generate_equation(difficulty)`: Generate a single equation
- `generate_worksheet(difficulty, num_problems)`: Generate multiple equations

### pdf_generator.py
Contains the `PDFWorksheetGenerator` class that creates PDF worksheets:
- `render_latex_to_image(latex_str)`: Convert LaTeX to image using matplotlib
- `generate_worksheet(equations, output_path, title, include_answer_key)`: Create PDF

### gui.py
Contains the `WorksheetGeneratorGUI` class with Tkinter interface:
- Provides user-friendly interface for worksheet generation
- Handles file save dialogs and user inputs

### main.py
Entry point that launches the GUI application.

## Extending the Generator

### Adding New Problem Types

The system now uses a **centralized configuration** in `worksheet_config.py` to make adding new problem types easy and prevent font sizing issues.

**Step 1: Create the Generator**

Create a new generator class (e.g., `quadratic_generator.py`):
- Follow the pattern of `LinearEquationGenerator` or `SystemsOfEquationsGenerator`
- Return problem objects with `latex`, `solution`, `steps`, and `difficulty` fields
- For systems or multi-part problems, include separate equation fields

**Step 2: Add Configuration**

In `worksheet_config.py`, add a new entry to `PROBLEM_TYPE_CONFIGS`:

```python
'quadratic': ProblemTypeConfig(
    latex_fontsize=20,        # Font size for LaTeX rendering
    image_width=3.5,          # Width in inches
    image_height=0.7,         # Height in inches
    vertical_offset=0.3,      # Offset from problem number
    problems_per_page=12,     # Max problems per page
    vertical_spacing=0.9,     # Space between problems
    instructions="Solve each quadratic equation. Show your work."
)
```

**Step 3: Update GUI**

In `gui.py`:
- Add the new problem type to the dropdown values
- Add difficulty descriptions to `self.difficulty_descriptions`
- Update `generate_worksheet()` to instantiate the new generator

**Step 4: Update PDF Generator** (if needed)

The PDF generator automatically uses the configuration, but if your problem type has special rendering needs (like systems with braces), add handling in `_draw_worksheet_page()`.

### Configuration Tips

- **Font sizes**: Start with 18-20pt and adjust based on visual tests
- **Image dimensions**: Systems need ~1.0" height, single equations ~0.5-0.7"
- **Spacing**: Should be `image_height + 0.2"` minimum
- **Problems per page**: 15 for small problems, 8 for systems, adjust accordingly

### Adding New Difficulty Levels

In your generator file:

1. Add a new method like `_generate_expert()`
2. Update `generate_equation()` or `generate_system()` to handle the new difficulty
3. Update GUI difficulty descriptions for that problem type

## Troubleshooting

### LaTeX Rendering Issues
If equations don't render properly:
- Ensure matplotlib is installed: `pip install matplotlib`
- The fallback will display equations as plain text

### PDF Not Generated
- Check file permissions for the output directory
- Ensure reportlab is installed: `pip install reportlab`

### GUI Won't Launch
- Tkinter comes with Python but may need separate installation on some Linux systems
- Try: `sudo apt-get install python3-tk` (Ubuntu/Debian)

## Future Enhancements

Planned features for web version:
- Web-based interface (Flask/Django backend)
- User accounts and saved worksheets
- More problem types (quadratic, polynomial, rational, etc.)
- Graph generation for coordinate geometry
- Step-by-step solution display
- Bulk worksheet generation
- Custom problem creation
