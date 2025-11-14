# Changelog

## [Unreleased]

### Added
- **Smart Default Problem Counts**: Different problem types now have different default numbers of problems based on their space requirements
  - Linear Equations: 10 problems (pure equations, compact)
  - Inequalities: 8 problems (need space for number lines)
  - Systems of Equations: 6 problems (need space for coordinate planes or work area)
- New `default_num_problems` field in `ProblemTypeConfig` dataclass
- Auto-updating problem count in GUI when switching problem types
- Test script `test_default_counts.py` to verify default counts

### Changed
- Updated `worksheet_config.py` to include default problem counts for each type
- Enhanced GUI to automatically update the number of problems spinbox when problem type changes
- Updated README.md to document smart defaults feature

### Technical Details
- Added `_update_default_num_problems()` method to GUI class
- Added `problem_type_map` to map display names to configuration keys
- Extended `ProblemTypeConfig` dataclass with `default_num_problems` parameter
- Imported `get_config` from `worksheet_config` in GUI module

## Previous Versions
(No formal versioning prior to this change)
