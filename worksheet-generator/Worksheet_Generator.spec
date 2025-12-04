# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec file for Math Worksheet Generator
#
# Build command: pyinstaller Worksheet_Generator.spec
#

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

# Collect all generator submodules
hidden_imports = [
    # Core dependencies
    'tkinter',
    'tkinter.ttk',
    'tkinter.filedialog',
    'tkinter.messagebox',

    # Excel support
    'openpyxl',
    'openpyxl.workbook',
    'openpyxl.reader',

    # PDF generation
    'reportlab',
    'reportlab.pdfgen',
    'reportlab.pdfgen.canvas',
    'reportlab.lib',
    'reportlab.lib.pagesizes',
    'reportlab.lib.units',
    'reportlab.lib.colors',
    'reportlab.platypus',

    # Image support
    'PIL',
    'PIL.Image',

    # Plotting
    'matplotlib',
    'matplotlib.backends',
    'matplotlib.backends.backend_tkagg',
    'matplotlib.pyplot',
    'matplotlib.figure',

    # Numerical
    'numpy',

    # Standard library
    'pathlib',
    'datetime',
    'threading',
    'subprocess',
    'importlib',
    'importlib.util',
]

# Collect all generator modules
hidden_imports += collect_submodules('generators')

# Collect reportlab data files (fonts, etc.)
reportlab_datas = collect_data_files('reportlab')

a = Analysis(
    ['gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Add generators folder as data
        ('generators', 'generators'),

        # Add Excel files
        ('High School Worksheet Topics List.xlsx', '.'),
        ('K-8 Worksheet Topics List.xlsx', '.'),

        # Add generator registry and helpers
        ('generator_registry.py', '.'),
        ('resource_helper.py', '.'),
        ('check_progress.py', '.'),

        # Add font folders
        ('Lexend', 'Lexend'),
        ('Poppins', 'Poppins'),
    ] + reportlab_datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude unnecessary modules to reduce size
        'pytest',
        'unittest',
        'test',
        '_pytest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Worksheet Generator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add .ico file path here if you have an icon
)
