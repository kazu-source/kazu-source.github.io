# Number Line Style Matching

## Overview

Updated number line styling to match the coordinate plane graphs, creating visual consistency across all graphing elements in the worksheet generator.

---

## Style Comparison

### OLD STYLE (Bold/Thick)
Previously used in [pdf_generator.py:252-318](pdf_generator.py#L252-L318)

- **Line width**: 3 (very thick)
- **Tick width**: 3, length: 10
- **Label size**: 14 (large)
- **Point marker size**: 15
- **Arrow line width**: 4 (very thick)
- **Color**: Blue for solution elements

**Visual characteristics:**
- Bold, heavy appearance
- Large text
- Thick lines throughout
- Inconsistent with coordinate plane styling

### NEW STYLE (Refined)
Now implemented in [numberline_utils.py](numberline_utils.py)

- **Line width**: 1.5 (matches coordinate plane axes)
- **Tick width**: 1.5, length: 8
- **Label size**: 9 (matches coordinate plane tick labels)
- **Point marker size**: 10 (proportional to coordinate plane points)
- **Arrow line width**: 2 (proportional to coordinate plane arrows)
- **Color**: Blue for solution elements

**Visual characteristics:**
- Refined, professional appearance
- Consistent with coordinate plane graphs
- Better readability
- Unified visual language across all graph types

---

## Coordinate Plane Style Reference

For reference, here are the coordinate plane styles we're matching:

**From [graphing_utils.py](graphing_utils.py):**
- Axes line width: 1.5
- Grid line width: 0.5 (dashed, alpha=0.7)
- Arrow line width: 1.5
- Tick label font size: 9
- Axis label font size: 12
- Point size: 50
- Point edge width: 1

---

## Implementation

### New Utility File: `numberline_utils.py`

Created a dedicated module for number line generation with consistent styling:

```python
class NumberLine:
    """Class for creating and managing number line graphs."""

    def create_figure(self, figsize=(8, 1.2), dpi=150):
        # Axes styled to match coordinate planes
        ax.spines['bottom'].set_linewidth(1.5)  # Match coordinate plane
        ax.tick_params(axis='x', width=1.5, length=8, labelsize=9)

        # Arrow matches coordinate plane arrow style
        ax.annotate('', xy=(...), arrowprops=dict(lw=1.5))

    def plot_solution_point(self, ax, value, is_equal=True):
        # Marker size proportional to coordinate plane points
        ax.plot(value, 0, 'o', markersize=10, ...)

    def plot_solution_region(self, ax, boundary_value, is_left=True):
        # Arrow width proportional to coordinate plane
        arrowprops=dict(arrowstyle='->', color='blue', lw=2)
```

### Key Functions:

1. **`create_blank_numberline()`**
   - Creates a blank number line (no solution shown)
   - Use for worksheet problems

2. **`create_numberline_with_solution()`**
   - Creates a number line with inequality solution
   - Automatically handles open/closed circles
   - Automatically handles left/right arrows
   - Use for answer keys

---

## Testing

### Test Script: `test_numberline_comparison.py`

Generated side-by-side comparison images:

**Blank Number Lines:**
- `comparison_old_blank.png` - Old thick style
- `comparison_new_blank.png` - New refined style

**With Solution (x >= 3):**
- `comparison_old_solution_gte.png` - Old thick style
- `comparison_new_solution_gte.png` - New refined style

**With Solution (x < -2):**
- `comparison_old_solution_lt.png` - Old thick style
- `comparison_new_solution_lt.png` - New refined style

### Running Tests:

```bash
# Test the new utilities
python numberline_utils.py

# Generate comparison images
python test_numberline_comparison.py
```

---

## Usage Examples

### Basic Usage:

```python
from numberline_utils import create_blank_numberline, create_numberline_with_solution

# Create a blank number line for a worksheet
blank_img = create_blank_numberline(min_val=-5, max_val=10)

# Create a number line showing x >= 3
solution_img = create_numberline_with_solution(
    min_val=-5,
    max_val=10,
    boundary_value=3,
    inequality_type='>='
)
```

### Advanced Usage with NumberLine Class:

```python
from numberline_utils import NumberLine

# Create custom number line
line = NumberLine(min_val=-10, max_val=10)
fig, ax = line.create_figure()

# Add custom elements
line.plot_solution_point(ax, value=5, is_equal=True)
line.plot_solution_region(ax, boundary_value=5, is_left=False)

# Render to image
img = line.render_to_image(fig)
img.save("custom_numberline.png")
```

---

## Benefits of Style Matching

1. **Visual Consistency**
   - All graph types (coordinate planes and number lines) now share a unified visual language
   - Students won't be distracted by inconsistent styling

2. **Professional Appearance**
   - Refined, clean look
   - Not overly bold or heavy
   - Better for printing and digital viewing

3. **Better Readability**
   - Appropriately sized text (9pt matches other math content)
   - Clear without being overwhelming
   - Proper visual hierarchy

4. **Scalability**
   - Consistent patterns make it easier to add new graph types
   - Clear style guide for future development
   - Maintainable codebase

---

## Migration Path

### For Existing Code:

The old number line rendering functions in `pdf_generator.py` can be gradually replaced:

**Old approach:**
```python
# In pdf_generator.py
def render_blank_numberline(self, min_val, max_val, ...):
    # Old thick style implementation
    ax.spines['bottom'].set_linewidth(3)
    ax.tick_params(axis='x', width=3, length=10, labelsize=14)
```

**New approach:**
```python
# Import from new utility
from numberline_utils import create_blank_numberline, create_numberline_with_solution

# Use the new functions
worksheet_img = create_blank_numberline(min_val, max_val)
answer_img = create_numberline_with_solution(min_val, max_val, boundary, inequality_type)
```

### Recommendation:

Update the inequalities generator to use the new number line utilities for consistency with the graphing points implementation.

---

## Files Created/Modified

### New Files:
- `numberline_utils.py` - New utility module for number lines
- `test_numberline_comparison.py` - Comparison test script
- `NUMBERLINE_STYLE_MATCHING.md` - This documentation file

### Test Output Files:
- `test_blank_numberline.png`
- `test_numberline_gte.png`
- `test_numberline_lt.png`
- `test_numberline_compact.png`
- `comparison_old_blank.png`
- `comparison_new_blank.png`
- `comparison_old_solution_gte.png`
- `comparison_new_solution_gte.png`
- `comparison_old_solution_lt.png`
- `comparison_new_solution_lt.png`

### Existing Files (reference only):
- `pdf_generator.py` - Contains old number line rendering (lines 252-318)
- `graphing_utils.py` - Coordinate plane utilities (style reference)

---

## Next Steps

1. **Optional Migration**: Update `inequalities_generator.py` to use new number line utilities
2. **Optional Refactor**: Remove old number line methods from `pdf_generator.py` after migration
3. **Consistency Check**: Ensure all number line usage across the codebase uses the new style

---

## Success Metrics

- [x] Number line utilities created
- [x] Style matches coordinate planes
- [x] Tests passing
- [x] Comparison images generated
- [x] Documentation complete
- [ ] Migration to new style (optional)

**The number line styling now matches the coordinate plane graphs perfectly!**
