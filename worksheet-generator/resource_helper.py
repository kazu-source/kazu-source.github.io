"""
Resource Path Helper for PyInstaller

This module provides utilities to handle file paths correctly both during
development and when running as a PyInstaller executable.

When PyInstaller creates an executable, it extracts files to a temporary
directory (sys._MEIPASS). This helper ensures files are found in both scenarios.
"""

import sys
import os


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and PyInstaller.

    Args:
        relative_path: Path relative to the application root

    Returns:
        Absolute path to the resource

    Example:
        excel_file = resource_path("High School Worksheet Topics List.xlsx")
        generators_folder = resource_path("generators")
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Running in normal Python environment
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def is_frozen():
    """
    Check if the application is running as a PyInstaller executable.

    Returns:
        True if frozen (running as .exe), False otherwise
    """
    return getattr(sys, 'frozen', False)
