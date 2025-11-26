@echo off
REM Build script for Math Worksheet Generator executable
REM
REM This script builds a standalone executable for Windows

echo =====================================
echo Math Worksheet Generator - Build Script
echo =====================================
echo.

echo Step 1: Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)
echo.

echo Step 2: Checking PyInstaller...
python -m PyInstaller --version
if errorlevel 1 (
    echo ERROR: PyInstaller not installed!
    echo Installing PyInstaller...
    pip install pyinstaller
)
echo.

echo Step 3: Building executable...
echo This may take several minutes...
echo.

python -m PyInstaller Worksheet_Generator.spec

if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo =====================================
echo Build completed successfully!
echo =====================================
echo.
echo The executable can be found in:
echo   dist\Worksheet Generator.exe
echo.
echo File size:
dir "dist\Worksheet Generator.exe" | find "Worksheet Generator.exe"
echo.

pause
