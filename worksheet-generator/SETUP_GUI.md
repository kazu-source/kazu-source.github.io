# GUI Setup Instructions

Complete setup guide for the Worksheet Generator web interface.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Web browser (Chrome, Firefox, Edge, Safari)

## Step-by-Step Setup

### Step 1: Install Flask Dependencies

Open Command Prompt or Terminal in the `worksheet-generator` directory and run:

```bash
pip install flask flask-cors
```

This installs:
- **Flask** - Web framework for the API server
- **Flask-CORS** - Enables browser access to the API

*Note: ReportLab should already be installed from previous worksheet generator setup*

If not, also run:
```bash
pip install reportlab
```

### Step 2: Verify Installation

Test that everything is installed correctly:

```bash
python -c "import flask, flask_cors; print('All dependencies installed successfully!')"
```

You should see: `All dependencies installed successfully!`

### Step 3: Start the Server

**Option A - Use the batch file (Windows):**
```bash
start_gui_server.bat
```

**Option B - Manual start:**
```bash
python api_server.py
```

You should see:
```
================================================================================
WORKSHEET GENERATOR API SERVER
================================================================================

Server starting on http://localhost:5000

API Endpoints:
  POST /api/generate-worksheet     - Generate standard worksheet
  POST /api/generate-practice-test - Generate practice test
  POST /api/generate-custom        - Generate custom worksheet
  ...

================================================================================

 * Serving Flask app 'api_server'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

**Keep this window open!** The server needs to stay running.

### Step 4: Open the GUI

Open your web browser and navigate to:

```
http://localhost:5000/
```

Then click on "Worksheet Generator" or navigate to:

```
http://localhost:5000/worksheet-generator.html
```

**Alternative:** Open `src/pages/worksheet-generator.html` directly in your browser if the server is running.

## GUI Overview

### Three Generation Modes

1. **Standard Worksheet**
   - Single topic, one difficulty
   - 1-30 problems
   - Custom titles supported

2. **Practice Test**
   - Unit Review (all topics in one unit)
   - Cumulative (multiple units)
   - Spiral Review (one topic, all difficulties)

3. **Custom Builder**
   - Mix multiple topics
   - Different difficulties per topic
   - Build complex assessments

## First Test

Try generating your first worksheet:

1. Click **Standard Worksheet** tab
2. Select **Unit 2**
3. Select **Equations** topic
4. Choose **Medium** difficulty
5. Set **10** problems
6. Click **Generate Worksheet**

The PDF will download automatically!

## Common Issues & Solutions

### Issue: "Module not found: flask"

**Solution:**
```bash
pip install flask flask-cors
```

### Issue: "Port 5000 is already in use"

**Solution 1 - Kill existing process:**
```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace <PID> with the number from above)
taskkill /PID <PID> /F
```

**Solution 2 - Use different port:**
Edit `api_server.py`, change the last line from:
```python
app.run(debug=True, port=5000)
```
to:
```python
app.run(debug=True, port=5001)
```

Then access at `http://localhost:5001/`

### Issue: Server starts but browser can't connect

**Check:**
1. Server is actually running (check console window)
2. No firewall blocking localhost
3. Try `http://127.0.0.1:5000` instead of `localhost`
4. Clear browser cache

### Issue: PDF not generating/downloading

**Check:**
1. Console output for error messages
2. `output/` folder exists and has write permissions
3. Topic name is correct and generator exists
4. Try generating via CLI first to verify backend works:
   ```bash
   python custom_worksheet_builder.py --unit 2 --topic "Equations" --difficulty medium --num 10
   ```

### Issue: "CORS error" in browser console

**Solution:**
Ensure `flask-cors` is installed:
```bash
pip install flask-cors
```

Then restart the server.

## Testing the Installation

### Test 1: API Server Health

With server running, open browser to:
```
http://localhost:5000/api/stats
```

Should see JSON response like:
```json
{
  "success": true,
  "stats": {
    "totalTopics": 23,
    "totalWorksheets": 92,
    "units": 6,
    "difficultyLevels": 4
  }
}
```

### Test 2: Get Topics for Unit 2

```
http://localhost:5000/api/topics/2.0
```

Should see list of Unit 2 topics.

### Test 3: Generate Worksheet via API

Use a tool like Postman or curl:

```bash
curl -X POST http://localhost:5000/api/generate-worksheet \
  -H "Content-Type: application/json" \
  -d "{\"unit\":2.0,\"topic\":\"Equations\",\"topicType\":\"Intro\",\"difficulty\":\"medium\",\"numProblems\":10}"
```

Should return success response with file path.

## File Locations

**Generated PDFs:**
- Standard: `output/Unit{X}/{Type}/`
- Practice Tests: `output/Practice_Tests/` or `output/Unit{X}/Practice_Tests/`
- Custom: `output/Custom/`

**Server Logs:**
- Console window where server is running

**Configuration:**
- API: `api_server.py`
- Frontend: `src/pages/worksheet-generator.html`
- JavaScript: `src/js/worksheet-generator.js`

## Stopping the Server

Press `Ctrl+C` in the server console window, then confirm with `Y`.

## Next Steps

Once everything is working:

1. **Explore all three modes** (Standard, Practice Test, Custom)
2. **Try different difficulty levels** including Challenge
3. **Generate practice tests** for review
4. **Build custom worksheets** for specific needs
5. **Organize generated PDFs** in the output folder

## Need Help?

1. Check this setup guide
2. Review [GUI_README.md](GUI_README.md) for usage details
3. Check console for error messages
4. Verify backend CLI tools work first
5. See [SESSION_SUMMARY.md](SESSION_SUMMARY.md) for overall project info

## Advanced: Running on Network

To access from other devices on your network:

1. Find your local IP address:
   ```bash
   ipconfig  # Windows
   ifconfig  # Mac/Linux
   ```

2. Edit `api_server.py`, change last line to:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```

3. Access from other devices at:
   ```
   http://<your-ip-address>:5000/
   ```

**Security Note:** Only do this on trusted networks!

## Production Deployment

For classroom or school-wide deployment, see [GUI_README.md](GUI_README.md) section on "Production Deployment".

---

**Setup Version:** 1.0
**Last Updated:** November 2025
**For:** Algebra 1 Worksheet Generator v1.1
