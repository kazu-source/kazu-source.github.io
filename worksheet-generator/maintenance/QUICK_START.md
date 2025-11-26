# Quick Start Guide

## Running Coverage Checks for Different Grade Levels

### For High School

```bash
cd worksheet-generator/maintenance
python check_generator_coverage.py "../High School Worksheet Topics List.xlsx" --config config_highschool.json --output-report
```

### For K-8

```bash
cd worksheet-generator/maintenance
python check_generator_coverage.py "../K-8 Topics.xlsx" --config config_k8.json --output-report
```

## Configuration Files

Each grade level uses a configuration file to customize behavior:

- **config_highschool.json** - Excludes "Expansion" and "Review" topics, uses "chapter" folder pattern
- **config_k8.json** - Excludes "Expansion", "Review", and "Extension" topics, uses "lesson" folder pattern

You can create custom configuration files for specific needs.

## What the Script Does

1. **Reads** the Excel file containing your topic list
2. **Scans** the generators directory for all generator files
3. **Matches** topics to generator files
4. **Reports** coverage statistics and missing generators
5. **Generates** a markdown report (if `-o` flag is used)

## Understanding the Output

### Console Output
- Shows immediate summary of coverage
- Lists all missing generators
- Organizes found generators by unit
- Displays expansion topics that don't need generators

### Markdown Report
- Saved as `[Excel Filename]_coverage_report.md`
- Contains detailed tables
- Includes timestamps
- Perfect for documentation and tracking progress

## Tips

- Run this script every time you add new topics to your Excel file
- Use `--output-report` to keep historical records
- Compare reports over time to track progress
- Missing generators listed with exact expected file paths

## Example Output

```
================================================================================
GENERATOR COVERAGE REPORT - High School
================================================================================
Total topics (excluding Expansion & Review): 102
Generators found: 102
Generators missing: 0
Coverage: 100.0%
```

This tells you that all 102 regular topics have generators, giving you 100% coverage. Expansion and Review topics are listed separately for manual handling.
