# Batch Worksheet Generation Guide

## Overview

The `batch_generate_worksheets.py` script automatically discovers all generators in the `generators/chapter##/` directories and generates worksheets for any difficulty level. This makes it flexible and maintainable across different grade levels.

## Features

- **Automatic Discovery**: Finds all generators in `generators/chapter##/` folders
- **Flexible Filtering**: Generate by difficulty, chapter, or both
- **Batch Generation**: Generate all difficulty levels at once
- **Customizable**: Adjust number of problems, output location, and more

## Basic Usage

### Generate Easy Worksheets
```bash
python batch_generate_worksheets.py --difficulty easy --output easy_worksheets
```

### Generate Medium Worksheets
```bash
python batch_generate_worksheets.py --difficulty medium --output medium_worksheets
```

### Generate Hard Worksheets
```bash
python batch_generate_worksheets.py --difficulty hard --output hard_worksheets
```

### Generate Challenge Worksheets
```bash
python batch_generate_worksheets.py --difficulty challenge --output challenge_worksheets
```

## Advanced Usage

### Generate All Difficulty Levels
```bash
python batch_generate_worksheets.py --all-difficulties --output all_worksheets
```
This creates subdirectories for each difficulty:
- `all_worksheets/easy_worksheets/`
- `all_worksheets/medium_worksheets/`
- `all_worksheets/hard_worksheets/`
- `all_worksheets/challenge_worksheets/`

### Filter by Chapters
Generate only specific chapters (e.g., chapters 1, 2, and 3):
```bash
python batch_generate_worksheets.py --difficulty easy --chapters 1 2 3
```

### Customize Number of Problems
Generate worksheets with 12 problems each instead of the default 8:
```bash
python batch_generate_worksheets.py --difficulty medium --problems 12
```

### Generate Without Answer Keys
```bash
python batch_generate_worksheets.py --difficulty easy --no-answer-key
```

## Command-Line Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--difficulty` | `-d` | Difficulty level: easy, medium, hard, or challenge |
| `--all-difficulties` | `-a` | Generate all four difficulty levels |
| `--output` | `-o` | Output directory (default: generated_worksheets) |
| `--problems` | `-p` | Number of problems per worksheet (default: 8) |
| `--chapters` | `-c` | Filter by chapter numbers (e.g., 1 2 3) |
| `--no-answer-key` | | Exclude answer keys from PDFs |

## Examples

### Example 1: Generate all easy worksheets
```bash
python batch_generate_worksheets.py -d easy -o easy_worksheets
```

### Example 2: Generate medium worksheets for Algebra 1 (chapters 1-5)
```bash
python batch_generate_worksheets.py -d medium -c 1 2 3 4 5 -o algebra1_medium
```

### Example 3: Generate challenge worksheets with 10 problems each
```bash
python batch_generate_worksheets.py -d challenge -p 10 -o challenge_10prob
```

### Example 4: Generate all levels for geometry topics (chapter 4)
```bash
python batch_generate_worksheets.py -a -c 4 -o geometry_all
```

## How It Works

1. **Discovery Phase**: Script scans `generators/chapter##/` directories
2. **Loading Phase**: Dynamically imports each `*_generator.py` file
3. **Generation Phase**: For each generator:
   - Instantiates the generator class
   - Calls `generate_worksheet(difficulty, num_problems)`
   - Generates PDF with answer key
4. **Output**: Saves all PDFs to specified directory

## Output

The script generates:
- **PDF worksheets** with problems and answer keys
- **Summary report** showing success/failure statistics
- **Error messages** for any failed generations

## Discovered Generators (Current)

As of the last run, the script discovered **102 generators** across all chapters:

- Chapter 1: Variables, Exponents, Evaluating Expressions, etc.
- Chapter 2: Equations, Inputs/Outputs, Linear Equations, etc.
- Chapter 3: Inequalities, Compound Inequalities, etc.
- Chapter 4: Graphing, Slope, Intercepts, etc.
- Chapter 5-13: Systems, Sequences, Quadratics, etc.

## Adding New Generators

To add a new worksheet type:

1. Create a generator file: `generators/chapter##/your_topic_generator.py`
2. Implement a class ending in `Generator` with a `generate_worksheet(difficulty, num_problems)` method
3. Run the batch script - it will automatically discover your new generator!

No configuration files need to be updated. The script handles everything automatically.

## Performance

- Generates approximately 1-2 worksheets per second
- 102 generators × 4 difficulties = 408 total worksheets in ~5-10 minutes
- Each worksheet is 100-500KB depending on complexity

## Troubleshooting

**Issue**: Generator not discovered
- **Solution**: Ensure filename ends with `_generator.py` and class name ends with `Generator`

**Issue**: Unicode errors on Windows
- **Solution**: Script uses ASCII-safe characters ([OK], [FAIL]) instead of Unicode checkmarks

**Issue**: Import errors for specific generators
- **Solution**: Check generator file for syntax errors. The script will skip problematic files and continue.

## Migration from Old Scripts

**Old approach** (hardcoded):
```python
# generate_all_easy.py - manually registered 33 topics
register_all_generators()
registry = get_registry()
```

**New approach** (automatic):
```python
# batch_generate_worksheets.py - discovers all 102 generators automatically
python batch_generate_worksheets.py --difficulty easy
```

Benefits:
- ✅ No manual registration needed
- ✅ Automatically finds new generators
- ✅ Works across different course levels
- ✅ More maintainable
- ✅ More flexible filtering options
