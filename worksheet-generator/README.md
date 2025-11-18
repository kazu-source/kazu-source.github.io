# Algebra 1 Worksheet Generator

Automated worksheet generator for Algebra 1 curriculum with 23 implemented topics across 5 units, generating 92 unique worksheets (4 difficulty levels each).

## Quick Start

### Generate All Worksheets

```bash
python generate_all.py
```

This generates all 92 worksheets in ~45 seconds:
- 23 topics
- 4 difficulty levels each (easy, medium, hard, challenge)
- Organized by unit and type
- Saved to `output/` directory

### Generate Specific Worksheets

Edit `regenerate_specific.py` to specify topics:

```python
worksheets = [
    (2.0, "Intro", "Equations"),
    (2.0, "Intro", "Properties of Equality"),
]
```

Then run:
```bash
python regenerate_specific.py
```

## Available Worksheets

**92 total worksheets** covering:

### Unit 1: One-Variable Statistics
- Introduction to Statistics (4 worksheets)
- Representing Data Graphically (4 worksheets)
- Summarizing Quantitative Data (4 worksheets)
- Modeling Data Distributions (4 worksheets)

### Unit 2: Linear Equations & Inequalities
- What Are Solutions? (4 worksheets)
- Equations (4 worksheets)
- Inputs and Outputs (4 worksheets)
- Properties of Equality (4 worksheets)
- Solving Equations (4 worksheets)

### Unit 3: Two-Variable Statistics
- Scatter Plots (4 worksheets)
- Correlation (4 worksheets)
- Linear Models (4 worksheets)
- Analyzing Relationships (4 worksheets)

### Unit 4: Functions
- Defining Functions (4 worksheets)
- Function Notation (4 worksheets)
- Interpreting Functions (4 worksheets)

### Unit 5: Systems of Equations
- Systems of Equations (4 worksheets)
- Solving Systems (4 worksheets)
- Inequalities and Systems (4 worksheets)

### Unit 11: Linear Relationships
- Comparing Linear Relationships (4 worksheets)
- Linear Equation Review (4 worksheets)
- Slope & Rate of Change (4 worksheets)

See [WORKSHEET_CATALOG.md](WORKSHEET_CATALOG.md) for complete topic list with metadata.

## Directory Structure

```
worksheet-generator/
├── output/                    # Generated worksheets
│   ├── Unit1/
│   │   ├── Intro/
│   │   │   ├── Introduction_to_Statistics_easy_20251117.pdf
│   │   │   ├── Introduction_to_Statistics_medium_20251117.pdf
│   │   │   └── Introduction_to_Statistics_hard_20251117.pdf
│   │   └── Graphing/
│   ├── Unit2/
│   │   ├── Intro/
│   │   └── Graphing/
│   ├── Unit3/
│   ├── Unit4/
│   ├── Unit5/
│   └── Unit11/
├── generators/                # Topic-specific generators
│   ├── chapter01/
│   ├── chapter02/
│   ├── chapter03/
│   ├── chapter04/
│   ├── chapter05/
│   └── chapter11/
├── generate_all.py           # Batch generation script
├── regenerate_specific.py    # Selective generation script
├── create_catalog.py         # Generate catalog files
├── pdf_generator.py          # PDF rendering engine
├── topic_registry.py         # Topic registration system
├── worksheet_config.py       # Configuration settings
└── README.md                 # This file
```

## Worksheet Features

### Four Difficulty Levels

- **Easy**: Basic concepts, smaller numbers, simpler operations
- **Medium**: Standard practice, moderate complexity
- **Hard**: Advanced problems, larger numbers, complex scenarios
- **Challenge**: Expert-level problems with multi-step reasoning, complex operations, and advanced concepts

### PDF Format

- Clean 3-column layout
- Professional Lexend font
- Answer keys on second page
- Proper text wrapping for long problems
- Compact, printer-friendly design

### Randomized Problems

Each generation creates unique problems:
- Random number selection within difficulty ranges
- Varied problem structures
- Multiple problem types per topic
- Ensures fresh practice every time

## Configuration

### Adjusting Problem Count

Edit `worksheet_config.py` to change default problem counts:

```python
CONFIG_REGISTRY = {
    'equations_intro': WorksheetConfig(
        title="Introduction to Equations",
        default_num_problems=15,  # Change this number
        difficulty_levels=['easy', 'medium', 'hard', 'challenge']
    ),
}
```

### Customizing Output Directory

Pass custom directory to `generate_all.py`:

```python
generate_all_worksheets(output_base_dir="my_worksheets")
```

### Modifying Difficulty Ranges

Edit individual generator files in `generators/chapter##/`:

```python
self.difficulty_ranges = {
    'easy': (1, 10),      # Adjust ranges
    'medium': (1, 20),
    'hard': (1, 50)
}
```

## Adding New Topics

1. Create generator in appropriate chapter folder:
```python
# generators/chapter02/my_topic_generator.py
class MyTopicGenerator:
    def generate_worksheet(self, difficulty: str, num_problems: int):
        # Implementation
```

2. Register in `topic_registry.py`:
```python
registry.register(
    unit=2.0,
    type=TopicType.INTRO,
    topic="My Topic",
    generator=MyTopicGenerator(),
    config_key='my_topic'
)
```

3. Add config in `worksheet_config.py`:
```python
'my_topic': WorksheetConfig(
    title="My Topic",
    default_num_problems=12,
    difficulty_levels=['easy', 'medium', 'hard']
)
```

4. Run `python generate_all.py` to include in batch generation

## Troubleshooting

### "Generator not found" error
- Check topic is registered in `topic_registry.py`
- Verify generator class is imported
- Ensure `register_all_generators()` is called

### PDF rendering issues
- Text bleeding off page: Check column width (3.0") and text wrapping
- Large images: Verify text rendering is enabled for that problem type
- Font errors: Ensure Lexend font is installed or fallback to Helvetica

### Unicode errors (Windows)
- Use ASCII characters only in print statements
- Avoid special characters in console output

### Invalid filename errors
- Check topic names don't contain: ? / \ : * " < > |
- Filename sanitization handles most cases automatically

### Performance issues
- Batch generation takes ~45 seconds for 92 worksheets
- Individual worksheet generation takes <1 second
- Use `regenerate_specific.py` for testing to avoid full regeneration

## File Naming Convention

```
{Topic}_{difficulty}_{date}.pdf
```

Examples:
- `Equations_easy_20251117.pdf`
- `Properties_of_Equality_medium_20251117.pdf`
- `Solving_Systems_hard_20251117.pdf`

Date format: YYYYMMDD (allows easy sorting by date)

## Coverage Statistics

- **Total Topics**: 23
- **Total Worksheets**: 92 (23 × 4 difficulty levels)
- **Difficulty Levels**: 4 (easy, medium, hard, challenge)
- **Units Covered**: 6 (Units 1, 2, 3, 4, 5, 11)
- **Units Pending**: 8 (Units 6-10, 12-14)
- **Problem Types**: Intro, Graphing, Mixed

## For Teachers

### Recommended Usage

1. **Pre-assessment**: Use easy worksheets to gauge student understanding
2. **Practice**: Assign medium worksheets for standard practice
3. **Advanced Practice**: Use hard worksheets for stronger students
4. **Honors/Competition**: Use challenge worksheets for gifted students and math competitions
5. **Review**: Regenerate worksheets for different problem sets

### Answer Keys

- Every worksheet includes answer key on page 2
- Solutions shown in red for easy grading
- Step-by-step solutions for complex problems (where applicable)

### Printing Tips

- Standard 8.5" × 11" paper
- Black & white printing recommended
- Answer keys print in red (shows as gray on B&W)
- 3-column layout optimizes paper usage

## Technical Details

### Dependencies

```bash
pip install reportlab
```

### Python Version
- Python 3.7+
- Tested on Windows 10/11

### Generator Architecture

- **Topic Registry**: Central registration system for all generators
- **PDF Generator**: ReportLab-based rendering engine
- **Problem Generators**: Topic-specific problem creation logic
- **Config System**: Centralized configuration for all topics

### Rendering Engine

- **ReportLab Canvas**: Low-level PDF generation
- **Text Rendering**: Plain text for readability and compactness
- **LaTeX Support**: Available for complex mathematical expressions
- **Text Wrapping**: Automatic wrapping for long problems (0.18" line height)
- **Font**: Lexend (primary), Helvetica (fallback)

## Version History

- **v1.1** (Nov 2025): Challenge difficulty update - 92 worksheets
  - Added challenge difficulty level to all 23 generators
  - 4 difficulty levels (easy, medium, hard, challenge)
  - Expert-level problems for honors students and competitions
- **v1.0** (Nov 2025): Initial release with 69 worksheets
  - 23 topics across 6 units
  - 3 difficulty levels
  - Batch generation support
  - Automated catalog generation
