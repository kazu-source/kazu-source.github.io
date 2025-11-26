# Maintenance Scripts

This folder contains maintenance and utility scripts for managing the worksheet generator system.

## Scripts

### check_generator_coverage.py

Checks if all topics listed in an Excel file have corresponding generator files in the generators directory. The script is fully configurable for different grade levels through JSON configuration files.

**Usage:**

```bash
# Basic usage - check coverage and print to console
python check_generator_coverage.py "../High School Worksheet Topics List.xlsx" --config config_highschool.json

# Generate a detailed markdown report
python check_generator_coverage.py "../High School Worksheet Topics List.xlsx" --config config_highschool.json --output-report

# For different grade levels
python check_generator_coverage.py "../K-8 Topics.xlsx" --config config_k8.json -o

# Specify custom generators directory (overrides config)
python check_generator_coverage.py "../Topics.xlsx" --config config_highschool.json --generators-dir "../custom_generators"
```

**Options:**

- `excel_file` (required): Path to the Excel file containing the topic list
- `--config` or `-c` (required): Path to configuration JSON file
- `--output-report` or `-o`: Generate a detailed markdown report file
- `--generators-dir` or `-g`: Override generators directory from config

**Configuration Files:**

The script uses JSON configuration files to adapt to different grade levels. Two configuration files are provided:

- `config_highschool.json` - For High School topics
- `config_k8.json` - For K-8 topics

**Configuration Format:**

```json
{
  "grade_level": "High School",
  "folder_pattern": "chapter",
  "excluded_types": ["Expansion", "Review"],
  "unit_format": "numeric",
  "generators_subdir": "generators"
}
```

- `grade_level`: Display name for reports (e.g., "High School", "Middle School")
- `folder_pattern`: Prefix for unit folders (e.g., "chapter", "lesson", "unit")
- `excluded_types`: Topic types to exclude from coverage calculation
- `unit_format`: Format of unit numbers (currently supports "numeric")
- `generators_subdir`: Subdirectory containing generator files

**Excel File Format:**

The Excel file should have the following columns:
- Column 1: Unit (e.g., "1", "2", "3")
- Column 2: Type (e.g., "Intro", "Graphing", "Solving", "Expansion")
- Column 3: Topic (e.g., "Variables", "Linear Equations")

**Output:**

The script will:
1. Print a console report showing:
   - Total topics and coverage percentage
   - Number of generators by chapter
   - List of missing generators
   - List of found generators organized by unit

2. If `--output-report` is specified, generate a markdown file with detailed coverage information

**Example Console Output:**

```
================================================================================
GENERATOR COVERAGE REPORT - High School
Source: High School Worksheet Topics List.xlsx
================================================================================

Total topics in Excel: 118

Generator files by chapter:
  Chapter 01: 16 generators
  Chapter 02: 11 generators
  ...

================================================================================
SUMMARY
================================================================================
Total topics (excluding Expansion & Review): 102
Generators found: 102
Generators missing: 0
Expansion topics (not checked): 11
Review topics (not checked): 5
Coverage: 100.0%
```

**Example Markdown Report:**

When using `--output-report`, a markdown file will be created with the naming pattern:
- Input: `High School Worksheet Topics List.xlsx`
- Output: `High School Worksheet Topics List_coverage_report.md`

This report includes:
- Detailed summary statistics
- Table of missing generators with expected file paths
- Complete list of expansion topics
- Organized breakdown of found generators by unit

## Running from Different Locations

The script is designed to work from the maintenance directory. All paths are relative to the script location:

```bash
# From the maintenance directory
cd worksheet-generator/maintenance
python check_generator_coverage.py "../High School Worksheet Topics List.xlsx"

# From the worksheet-generator directory
cd worksheet-generator
python maintenance/check_generator_coverage.py "High School Worksheet Topics List.xlsx"
```

## Future Scripts

This directory can house additional maintenance scripts such as:
- Generator validation scripts
- Batch worksheet generation utilities
- Topic registry verification tools
- Migration scripts for updating generator formats
