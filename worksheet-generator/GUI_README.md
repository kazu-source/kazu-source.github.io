# Worksheet Generator GUI

Web-based graphical interface for the Algebra 1 Worksheet Generator with all three generation modes.

## Features

✅ **Standard Worksheet Generator** - Generate single-topic worksheets with 4 difficulty levels
✅ **Practice Test Generator** - Create mixed-problem tests (unit review, cumulative, spiral)
✅ **Custom Worksheet Builder** - Combine multiple topics with custom difficulties

## Quick Start

### 1. Install Dependencies

```bash
cd worksheet-generator
pip install -r requirements_api.txt
```

This installs:
- Flask (web server)
- Flask-CORS (API access)
- ReportLab (PDF generation)

### 2. Start the Server

**Option A - Windows Batch File:**
```bash
start_gui_server.bat
```

**Option B - Command Line:**
```bash
python api_server.py
```

### 3. Open the GUI

Navigate to: **http://localhost:5000/worksheet-generator.html**

Or open: `src/pages/worksheet-generator.html` in your browser

## Using the GUI

### Standard Worksheet Tab

Generate a worksheet for a single topic:

1. **Select Unit** - Choose from Units 1-11
2. **Select Topic** - Topic list updates based on unit
3. **Choose Difficulty** - Easy, Medium, Hard, or Challenge
4. **Set Problem Count** - 1-30 problems (default: 10)
5. **Optional: Custom Title** - Override auto-generated title
6. **Click "Generate Worksheet"**

**Output:** PDF saved to `output/Unit{X}/{Type}/{Topic}_{difficulty}_{date}.pdf`

### Practice Test Tab

Create mixed-problem practice tests:

#### Test Types:

**1. Unit Review**
- Combines all topics from one unit
- Configurable: Total problems, difficulty mix
- Perfect for end-of-unit assessments

**2. Cumulative Test**
- Select multiple units (check boxes)
- Covers all topics across selected units
- Ideal for semester reviews

**3. Spiral Review**
- One topic, all 4 difficulty levels
- Progressive practice from easy → challenge
- Set problems per difficulty level

#### Difficulty Mix Options:
- **Balanced** - Equal mix of all 4 levels
- **Progressive** - Starts easy, ends with challenge
- **All Easy/Medium/Hard/Challenge** - Single difficulty

**Output:** PDF saved to appropriate Practice_Tests folder

### Custom Worksheet Builder Tab

Build worksheets with specific topic combinations:

1. **Click "+ Add Topic"** to add a row
2. **For each row:**
   - Select Unit
   - Select Topic
   - Choose Difficulty
   - Set Problem Count (1-20 per topic)
3. **Remove unwanted rows** with "Remove" button
4. **Enter Worksheet Title** (required)
5. **Click "Generate Custom Worksheet"**

**Output:** PDF saved to `output/Custom/{Title}_{date}.pdf`

**Use Cases:**
- Targeted review (e.g., "Equations and Properties Review")
- Mixed-difficulty practice (easy + hard same topic)
- Cross-unit assessments
- Customized homework assignments

## API Endpoints

The Flask server provides these REST API endpoints:

### POST /api/generate-worksheet
Generate standard worksheet

**Request Body:**
```json
{
  "unit": 2.0,
  "topic": "Equations",
  "topicType": "Intro",
  "difficulty": "medium",
  "numProblems": 10,
  "customTitle": "Optional Title"
}
```

**Response:**
```json
{
  "success": true,
  "path": "output/Unit2/Intro/Equations_medium_20251117.pdf",
  "downloadUrl": "/api/download/Equations_medium_20251117.pdf"
}
```

### POST /api/generate-practice-test
Generate practice test

**Request Body (Unit Review):**
```json
{
  "testType": "unit",
  "unit": 2.0,
  "numProblems": 20,
  "difficultyMix": "balanced"
}
```

**Request Body (Cumulative):**
```json
{
  "testType": "cumulative",
  "units": [1.0, 2.0],
  "numProblems": 30,
  "difficultyMix": "progressive"
}
```

**Request Body (Spiral):**
```json
{
  "testType": "spiral",
  "unit": 2.0,
  "topic": "Equations",
  "topicType": "Intro",
  "problemsPerLevel": 5
}
```

### POST /api/generate-custom
Generate custom worksheet

**Request Body:**
```json
{
  "title": "Custom Test",
  "specs": [
    {
      "unit": 2.0,
      "topic": "Equations",
      "topicType": "Intro",
      "difficulty": "medium",
      "numProblems": 5
    },
    {
      "unit": 2.0,
      "topic": "Properties of Equality",
      "topicType": "Intro",
      "difficulty": "hard",
      "numProblems": 5
    }
  ]
}
```

### GET /api/download/<filename>
Download generated PDF

### GET /api/topics/<unit>
Get available topics for a unit

### GET /api/stats
Get generator statistics

## File Structure

```
worksheet-generator/
├── api_server.py              # Flask API server
├── start_gui_server.bat       # Windows startup script
├── requirements_api.txt       # Python dependencies
└── GUI_README.md             # This file

src/
├── pages/
│   └── worksheet-generator.html   # Main GUI
└── js/
    └── worksheet-generator.js     # Frontend JavaScript

output/
├── Unit1/ ... Unit11/        # Standard worksheets
├── Practice_Tests/           # Generated practice tests
└── Custom/                   # Custom worksheets
```

## Available Topics by Unit

### Unit 1: One-Variable Statistics (4 topics)
- Introduction to Statistics
- Representing Data Graphically
- Summarizing Quantitative Data
- Modeling Data Distributions

### Unit 2: Linear Equations & Inequalities (9 topics)
- What Are Solutions?
- Equations
- Inputs and Outputs
- Property of Equality (add/subtract)
- Property of Equality (mult/div)
- Solving Multi-Step Equations
- Linear Equations
- Linear Equation Word Problems
- Solving Equations with Variables on Both Sides

### Unit 3: Two-Variable Statistics (1 topic)
- One-Step Inequalities

### Unit 4: Functions (5 topics)
- Points on a Coordinate Plane
- Line on a Coordinate Plane
- Slope-Intercept Form
- Point-Slope Form
- Standard Form

### Unit 5: Systems of Equations (2 topics)
- Systems of Equations (Intro)
- Systems of Equations (Graphing)

### Unit 11: Linear Relationships (1 topic)
- Using Vertex Form

**Total: 23 topics × 4 difficulty levels = 92 possible worksheets**

## Troubleshooting

### Server won't start
- **Check if port 5000 is in use:**
  ```bash
  netstat -ano | findstr :5000
  ```
- **Kill the process if needed:**
  ```bash
  taskkill /PID <pid> /F
  ```
- **Try a different port:**
  Edit `api_server.py`, change last line to:
  ```python
  app.run(debug=True, port=5001)
  ```

### "Module not found" errors
- Ensure you're in the worksheet-generator directory
- Reinstall dependencies:
  ```bash
  pip install -r requirements_api.txt
  ```

### Can't access from browser
- Check server console for errors
- Ensure Flask server shows "Running on http://127.0.0.1:5000"
- Try http://127.0.0.1:5000 instead of localhost

### CORS errors
- Flask-CORS should handle this automatically
- If issues persist, check browser console for specific error

### PDF not downloading
- Check output folder permissions
- Verify worksheet generated (check console output)
- Look for PDF in `output/` directory manually

### Topic not found
- Verify topic name matches exactly (case-sensitive)
- Check `topic_registry.py` for registered topics
- Ensure all generators are imported

## Development

### Adding New Topics to GUI

1. **Update JavaScript topic data** in `worksheet-generator.js`:
```javascript
const TOPICS_BY_UNIT = {
    '2.0': [
        { value: 'Your New Topic', type: 'Intro' },
        // ... existing topics
    ]
};
```

2. **Ensure backend has generator** registered in `topic_registry.py`

3. **Restart server** to pick up changes

### Customizing the GUI

**Styling:** Edit inline `<style>` in `worksheet-generator.html`

**Functionality:** Modify `worksheet-generator.js`

**Backend Logic:** Update `api_server.py`

## Production Deployment

For production use:

1. **Disable Flask debug mode:**
   ```python
   app.run(debug=False, port=5000)
   ```

2. **Use production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 api_server:app
   ```

3. **Add authentication** if exposing publicly

4. **Configure reverse proxy** (nginx/Apache)

5. **Enable HTTPS** with SSL certificates

## Support

For issues or questions:
1. Check console output for error messages
2. Verify all dependencies installed
3. Ensure worksheet-generator backend is working (test with CLI)
4. Review this README troubleshooting section

## Version

**GUI Version:** 1.0
**Backend Version:** 1.1 (with challenge difficulty)
**Last Updated:** November 2025
