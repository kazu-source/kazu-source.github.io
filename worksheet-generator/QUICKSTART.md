# Quick Start Guide - 5 Minutes to Your First Worksheet

Get started with the Worksheet Generator in just 5 minutes!

## Step 1: Install Flask (2 minutes)

Open Command Prompt in the `worksheet-generator` folder and run:

```bash
pip install flask flask-cors
```

Wait for installation to complete. You should see "Successfully installed flask flask-cors".

## Step 2: Start the Server (30 seconds)

Double-click: **`start_gui_server.bat`**

Or in Command Prompt:
```bash
python api_server.py
```

You should see:
```
================================================================================
WORKSHEET GENERATOR API SERVER
================================================================================
Server starting on http://localhost:5000
...
 * Running on http://127.0.0.1:5000
```

**Keep this window open!**

## Step 3: Open the GUI (30 seconds)

Open your web browser and go to:

```
http://localhost:5000/worksheet-generator.html
```

You should see a purple header with "Algebra 1 Worksheet Generator".

## Step 4: Generate Your First Worksheet (2 minutes)

1. Make sure you're on the **"Standard Worksheet"** tab

2. **Select Unit 2** from the first dropdown

3. **Select "Equations"** from the second dropdown (it appears after selecting unit)

4. **Keep "Medium"** difficulty selected

5. **Keep "10"** problems

6. **Click the blue "Generate Worksheet" button**

7. **PDF downloads automatically!**
   - Opens in your default PDF viewer
   - Saved to: `output/Unit2/Intro/Equations_medium_20251117.pdf`

## Done! 🎉

You just generated your first worksheet with:
- 10 medium-difficulty equation problems
- Answer key on page 2
- Professional formatting
- Ready to print

## What's Next?

### Try Challenge Difficulty
Same steps, but select **"Challenge"** instead of Medium

### Try a Practice Test
1. Click the **"Practice Test"** tab
2. Select **"Unit Review"**
3. Choose **"Unit 2"**
4. Set **20** problems
5. Select **"Balanced"** difficulty mix
6. Click **"Generate Practice Test"**

### Try Custom Builder
1. Click the **"Custom Builder"** tab
2. You'll see one row already added
3. Select **Unit 2**, **Equations**, **Medium**, **5 problems**
4. Click **"+ Add Topic"**
5. Select **Unit 2**, **Properties of Equality (add/subtract)**, **Hard**, **5 problems**
6. Enter title: **"Mixed Review"**
7. Click **"Generate Custom Worksheet"**

## Troubleshooting

### Can't access http://localhost:5000
- Check the server window is still running
- Try http://127.0.0.1:5000 instead
- Make sure Flask installed successfully

### "Module not found: flask"
Run this again:
```bash
pip install flask flask-cors
```

### Port 5000 already in use
Kill the existing process:
```bash
netstat -ano | findstr :5000
taskkill /PID <number> /F
```

### PDF not downloading
- Check console for errors
- Verify output folder exists
- Try generating again

## All Features Available

### Standard Worksheet:
- 23 topics
- 4 difficulty levels (Easy, Medium, Hard, Challenge)
- 1-30 problems
- Custom titles

### Practice Test:
- Unit Review (all topics in one unit)
- Cumulative (multiple units)
- Spiral Review (one topic, all difficulties)
- 6 difficulty mix options

### Custom Builder:
- Combine any topics
- Mix difficulties
- Custom problem counts
- Unlimited combinations

## Need More Help?

See these guides:
- **SETUP_GUI.md** - Detailed installation
- **GUI_README.md** - Complete usage guide
- **COMPLETE_FEATURE_SUMMARY.md** - All features explained

## Stop the Server

When done:
1. Go to the server console window
2. Press **Ctrl+C**
3. Type **Y** and press Enter

---

**That's it!** You're now ready to generate unlimited worksheets for your students.

**Happy Teaching! 📚**
