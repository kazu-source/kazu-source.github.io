# Batch Worksheet Generation System

Comprehensive infrastructure for generating worksheets in batches based on Excel topic lists.

## Overview

This system provides automated batch generation of worksheets across multiple topics, units, and difficulty levels. It's designed to scale as you add more grade levels and courses.

## Architecture

### Core Components

1. **Topic Registry** ([topic_registry.py](topic_registry.py))
   - Centralized registry mapping topics to generators
   - Tracks implementation coverage
   - Organized by unit, type, and topic

2. **Excel Configuration Loader** ([excel_config_loader.py](excel_config_loader.py))
   - Loads topic definitions from Excel files
   - Supports multiple courses/grade levels
   - Auto-detects course names from filenames

3. **Batch Orchestrator** ([batch_orchestrator.py](batch_orchestrator.py))
   - Coordinates batch worksheet generation
   - Progress tracking and error handling
   - Generates organized output structure

4. **Generator Factory** ([generator_factory.py](generator_factory.py))
   - Centralized generator instantiation
   - Caching for performance
   - Category organization

5. **Output Manager** ([output_manager.py](output_manager.py))
   - Organizes generated PDFs
   - Tracks generation history in manifest
   - Generates HTML index of all worksheets

6. **CLI Tools**
   - [batch_generate.py](batch_generate.py) - Main batch generation tool
   - [coverage_report.py](coverage_report.py) - Coverage analysis tool

## Quick Start

### Generate Intro and Graphing Worksheets

```bash
python batch_generate.py --filter intro,graphing --difficulty easy
```

### Generate Worksheets for Specific Unit

```bash
python batch_generate.py --unit 4 --difficulty easy
```

### Check Implementation Coverage

```bash
python coverage_report.py --full
```

## CLI Reference

### batch_generate.py

Main tool for batch worksheet generation.

```bash
# Generate all Intro and Graphing worksheets (default)
python batch_generate.py

# Generate with filters
python batch_generate.py --filter intro,graphing --difficulty medium

# Generate specific unit
python batch_generate.py --unit 2 --type intro

# Custom problem count
python batch_generate.py --filter intro --num-problems 15

# Skip existing files
python batch_generate.py --all --skip-existing

# Generate HTML index
python batch_generate.py --filter intro --generate-index
```

**Options:**
- `--filter TYPE1,TYPE2` - Filter by worksheet types
- `--unit NUMBER` - Generate only specific unit
- `--type TYPE` - Generate only specific type
- `--all` - Generate all implemented worksheets
- `--difficulty {easy,medium,hard}` - Difficulty level
- `--num-problems N` - Override default problem count
- `--skip-existing` - Skip if file already exists
- `--output-dir DIR` - Output directory (default: output)
- `--generate-index` - Create HTML index
- `--excel PATH` - Excel configuration file

### coverage_report.py

Analyzes implementation coverage and identifies gaps.

```bash
# Full coverage report
python coverage_report.py --full

# Summary only
python coverage_report.py --summary

# Export to CSV
python coverage_report.py --export coverage.csv

# Save to file
python coverage_report.py --full --output report.txt
```

**Options:**
- `--full` - Detailed coverage report
- `--summary` - Brief summary
- `--export FILE` - Export to CSV
- `--output FILE` - Save report to file
- `--excel PATH` - Excel configuration file

## Output Structure

Generated worksheets are organized as:

```
output/
├── Algebra 1/
│   ├── Unit01/
│   │   ├── Intro/
│   │   │   ├── Variables_easy_20251117.pdf
│   │   │   └── Exponents_easy_20251117.pdf
│   │   └── Graphing/
│   │       └── ...
│   ├── Unit02/
│   │   └── ...
│   └── ...
├── Geometry/
│   └── ...
├── manifest.json          # Tracks all generated worksheets
└── index.html            # HTML index (if generated)
```

## Excel Configuration Format

The system reads topic lists from Excel files:

| Unit | Type      | Topic                     |
|------|-----------|---------------------------|
| 1.0  | Intro     | Variables                 |
| 1.0  | Intro     | Exponents                 |
| 2.0  | Intro     | Linear Equations          |
| 4.0  | Graphing  | Points on Coordinate Plane|

**Columns:**
- **Unit**: Unit number (e.g., 1.0, 2.0, 11.0)
- **Type**: Worksheet type (Intro, Graphing, Solving, Expansion, etc.)
- **Topic**: Topic name

**File Naming:**
- Course name is auto-detected from filename
- `*Algebra*1*.xlsx` → "Algebra 1"
- `*Grade*6*.xlsx` → "Grade 6"

## Adding New Generators

### 1. Create Generator Class

```python
# generators/my_topic_generator.py
class MyTopicGenerator:
    def generate_worksheet(self, difficulty: str, num_problems: int):
        # Generate problems
        problems = []
        for i in range(num_problems):
            # Create problem based on difficulty
            problem = self.create_problem(difficulty)
            problems.append(problem)
        return problems
```

### 2. Register in topic_registry.py

```python
# In register_all_generators():
from generators.my_topic_generator import MyTopicGenerator

registry.register_topic(
    unit=3.0,
    type="Intro",
    topic="My New Topic",
    generator_class=MyTopicGenerator,
    config_key="my_topic_config"
)
```

### 3. Add Configuration in worksheet_config.py

```python
PROBLEM_TYPE_CONFIGS = {
    'my_topic_config': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=10,
        vertical_spacing=1.0,
        default_num_problems=10,
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Solve each problem."
    ),
    # ...
}
```

### 4. Add to Excel File

Add row to your Excel topic list:
- Unit: 3.0
- Type: Intro
- Topic: My New Topic

## Current Implementation Status

As of 2025-11-17:

- **Total Topics**: 107 (Algebra 1 draft)
- **Implemented**: 10 (9.3%)
- **Intro + Graphing**: 10/81 (12.3%)

### Implemented Topics

**Unit 2 - Intro:**
- Linear Equations
- Linear Equation Word Problems
- Property of Equality (add/subtract)
- Property of Equality (mult/div)
- Solving Multi-Step Equations

**Unit 3 - Graphing:**
- One-Step Inequalities

**Unit 4 - Graphing:**
- Points on a Coordinate Plane

**Unit 5:**
- Systems of Equations (Intro)
- Systems of Equations (Graphing)

**Unit 11 - Graphing:**
- Using Vertex Form

## Extending to Multiple Courses

The system is designed for multiple grade levels:

### 1. Create Excel Files

Create separate Excel files:
- `Algebra 1 Worksheet Topics.xlsx`
- `Algebra 2 Worksheet Topics.xlsx`
- `Geometry Worksheet Topics.xlsx`
- `Grade 6 Worksheet Topics.xlsx`

### 2. Auto-Discovery

The system will auto-discover all Excel topic files:

```python
from excel_config_loader import MultiCourseLoader

loader = MultiCourseLoader("worksheet-generator")
all_courses = loader.load_all()
# Auto-detects and loads all *Topic*.xlsx files
```

### 3. Generate by Course

```bash
# Future: Generate for specific course
python batch_generate.py --course "Algebra 2" --filter intro
```

## Manifest and Tracking

The system maintains a `manifest.json` file tracking all generated worksheets:

```json
[
  {
    "timestamp": "2025-11-17T10:30:00",
    "course": "Algebra 1",
    "unit": 2.0,
    "type": "Intro",
    "topic": "Linear Equations",
    "difficulty": "easy",
    "num_problems": 10,
    "file_path": "output/Algebra 1/Unit02/Intro/Linear Equations_easy_20251117.pdf",
    "file_size_bytes": 87432
  }
]
```

### Query Manifest

```python
from output_manager import OutputManager

mgr = OutputManager()
worksheets = mgr.get_worksheets(unit=2.0, difficulty="easy")
```

## HTML Index

Generate a browsable HTML index of all worksheets:

```bash
python batch_generate.py --all --generate-index
```

Opens `output/index.html` showing:
- All worksheets organized by course and unit
- Direct links to PDFs
- Metadata (type, difficulty, problem count)

## Development Workflow

### 1. Plan Topics in Excel

Edit `High School Worksheet Topics List.xlsx` to define what worksheets you want.

### 2. Check Coverage

```bash
python coverage_report.py --full
```

Identifies which topics need generators.

### 3. Implement Generators

Create generator classes for unimplemented topics.

### 4. Test Single Generator

Use GUI or direct testing to verify generator works.

### 5. Batch Generate

```bash
python batch_generate.py --filter intro,graphing
```

### 6. Review Output

Check `output/` directory for generated PDFs.

## Troubleshooting

### No Tasks Created

If batch generation creates 0 tasks:
- Check `--coverage` to see what's implemented
- Verify Excel file is loaded correctly
- Ensure filters match available topics

### Generation Failures

Common issues:
- Generator method signature mismatch
- Missing configuration in `worksheet_config.py`
- PDF generator compatibility issues

Check error messages in batch output for details.

### Excel Not Found

Ensure Excel path is correct:
```bash
python batch_generate.py --excel "path/to/your/file.xlsx"
```

## Future Enhancements

Planned features:
- [ ] Multi-course support in CLI
- [ ] Parallel generation for speed
- [ ] Difficulty mix (easy/medium/hard in one batch)
- [ ] Answer key-only generation
- [ ] Worksheet variants (different problem sets)
- [ ] Web interface for batch generation

## Files Reference

| File | Purpose |
|------|---------|
| `topic_registry.py` | Topic → Generator mapping |
| `excel_config_loader.py` | Excel topic list loader |
| `batch_orchestrator.py` | Batch generation coordinator |
| `generator_factory.py` | Generator instantiation |
| `output_manager.py` | Output organization & tracking |
| `batch_generate.py` | CLI batch generation tool |
| `coverage_report.py` | Coverage analysis tool |
| `worksheet_config.py` | Rendering configurations |

## Summary

This batch generation system provides:

- **Scalability**: Easy to add new topics, units, and courses
- **Organization**: Structured output by course/unit/type
- **Tracking**: Manifest of all generated worksheets
- **Visibility**: Coverage reports show implementation status
- **Flexibility**: CLI tools for different workflows
- **Extensibility**: Simple to add new generators

The system is production-ready for generating worksheets for implemented topics, with a clear path for expanding coverage.
