===============================================================================
                    Math Worksheet Generator
                       Distribution Guide
===============================================================================

CONGRATULATIONS! You've successfully packaged the Math Worksheet Generator
as a standalone Windows executable.

===============================================================================
WHAT WAS CREATED
===============================================================================

Location: worksheet-generator\dist\Worksheet Generator.exe
Size: ~43 MB
Type: Standalone Windows executable (no Python installation required)

The executable includes:
- Complete GUI interface
- All 103 math worksheet generators
- PDF generation capabilities
- Excel data files for topics
- All required libraries (matplotlib, reportlab, numpy, openpyxl, etc.)

===============================================================================
TESTING THE EXECUTABLE
===============================================================================

Before distributing to students:

1. Copy "Worksheet Generator.exe" to a test location
2. Double-click to run
3. Test generating a few worksheets:
   - Select a subject (e.g., "High-School - Algebra")
   - Select a topic (e.g., "Variables")
   - Choose difficulty level
   - Click "Generate Worksheet"
4. Verify the PDF opens correctly

===============================================================================
DISTRIBUTING TO STUDENTS
===============================================================================

Option 1: Direct File Share
---------------------------
- Simply share the "Worksheet Generator.exe" file
- Students can run it directly - no installation needed
- Recommended: Create a shared folder or USB drive

Option 2: Create a Zip File
---------------------------
1. Right-click "Worksheet Generator.exe"
2. Select "Send to" > "Compressed (zipped) folder"
3. Share the .zip file
4. Students extract and run the .exe

Option 3: Network Share
-----------------------
- Place the executable on a school network drive
- Students can run it from the network location

===============================================================================
STUDENT INSTRUCTIONS
===============================================================================

Share these instructions with your students:

"""
MATH WORKSHEET GENERATOR - INSTRUCTIONS

1. Download/locate "Worksheet Generator.exe"
2. Double-click to open the program
3. Select your subject from the dropdown
4. Select a topic from the list
5. Choose a difficulty level (Easy/Medium/Hard/Challenge)
6. Click "Generate Worksheet"
7. The PDF will open automatically
8. Print or save as needed

Note: The first time you run the program, Windows may show a security
warning. Click "More info" then "Run anyway" - this is normal for new
applications that haven't been digitally signed.
"""

===============================================================================
WINDOWS SECURITY WARNINGS
===============================================================================

When students first run the executable, Windows Defender may show:
"Windows protected your PC"

This is NORMAL for unsigned executables. To proceed:
1. Click "More info"
2. Click "Run anyway"

To avoid this warning (optional advanced steps):
- Purchase a code signing certificate (~$100-300/year)
- Sign the executable with signtool.exe
- This adds your digital signature to the .exe

===============================================================================
TROUBLESHOOTING
===============================================================================

Issue: "DLL not found" errors
Solution: Ensure students are running Windows 10 or later

Issue: Program opens but crashes when generating
Solution: Check if antivirus is blocking file creation
         Add the program to antivirus exceptions

Issue: Very slow to start
Solution: This is normal - first launch may take 10-20 seconds
         The program extracts files to a temporary folder

Issue: "Can't find generators"
Solution: Don't separate the .exe from its temp extraction folder
         It should be run as-is from wherever it's placed

===============================================================================
REBUILDING THE EXECUTABLE
===============================================================================

If you need to rebuild (e.g., after adding new generators):

Option 1: Using the batch file
   > cd worksheet-generator
   > build_exe.bat

Option 2: Manual build
   > cd worksheet-generator
   > python build_generator_registry.py
   > python -m PyInstaller Worksheet_Generator.spec --clean

The new executable will be in: worksheet-generator\dist\

===============================================================================
FILE SIZE & PERFORMANCE
===============================================================================

Executable Size: ~43 MB
- Includes Python interpreter
- Includes all scientific libraries
- No external dependencies needed

Startup Time: 5-15 seconds (first launch)
- Subsequent launches are faster
- Windows caches the temp extraction

Memory Usage: ~200-300 MB when running
- Normal for applications with matplotlib/numpy

PDF Generation: < 1 second per worksheet
- Very fast generation
- Professional quality output

===============================================================================
TECHNICAL DETAILS (for reference)
===============================================================================

Built with:
- PyInstaller 6.16.0
- Python 3.12.2
- Generator Registry System (103 generators)
- Resource path helper for frozen state detection

Key Files (in source, not distributed):
- gui.py: Main application
- generator_registry.py: Auto-generated imports
- resource_helper.py: Path handling for PyInstaller
- Worksheet_Generator.spec: Build configuration
- build_exe.bat: Rebuild script

===============================================================================
ADDING NEW GENERATORS
===============================================================================

If you add new generators to the codebase:

1. Add the new generator file(s) to the appropriate Unit folder
2. Rebuild the registry:
   > python build_generator_registry.py
3. Rebuild the executable:
   > build_exe.bat
4. The new topics will appear in the Subject/Topic dropdowns

===============================================================================
SUPPORT & MAINTENANCE
===============================================================================

The executable is fully self-contained and maintenance-free for students.

For teachers/administrators:
- No updates needed unless you modify the source code
- Can be redistributed freely to any number of students
- Works offline - no internet connection required

===============================================================================
LICENSE & DISTRIBUTION
===============================================================================

This tool was created for educational purposes.
You may freely distribute this executable to your students.

===============================================================================

Generated: November 2024
PyInstaller Version: 6.16.0
Python Version: 3.12.2

===============================================================================
