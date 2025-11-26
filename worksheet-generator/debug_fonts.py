import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

print("Current directory:", os.getcwd())
print("__file__ would be:", "worksheet-generator/debug_fonts.py")

# Simulate what pdf_generator does
base_dir = os.path.dirname(os.path.dirname(os.path.abspath("worksheet-generator/pdf_generator.py")))
print(f"base_dir: {base_dir}")

lexend_regular = os.path.join(base_dir, 'Lexend', 'static', 'Lexend-Regular.ttf')
print(f"Lexend path: {lexend_regular}")
print(f"Lexend exists: {os.path.exists(lexend_regular)}")

poppins_regular = os.path.join(base_dir, 'Poppins', 'Poppins-Regular.ttf')
print(f"Poppins path: {poppins_regular}")
print(f"Poppins exists: {os.path.exists(poppins_regular)}")

# Try to register
try:
    if os.path.exists(lexend_regular):
        pdfmetrics.registerFont(TTFont('Lexend', lexend_regular))
        print("Successfully registered Lexend")
    else:
        print("Lexend font file not found!")
except Exception as e:
    print(f"Error registering Lexend: {e}")
