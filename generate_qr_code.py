"""
Generate QR code for freshmath.org website.
"""

import qrcode
import os

def generate_qr_code():
    """Generate a QR code that links to freshmath.org"""

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls size (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in pixels
        border=2,  # Border thickness in boxes
    )

    # Add data
    qr.add_data('https://freshmath.org')
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save to icons directory
    output_path = os.path.join('src', 'icons', 'freshmath_qr.png')
    img.save(output_path)

    print(f"QR code generated successfully!")
    print(f"Saved to: {output_path}")
    print(f"Image size: {img.size}")
    print(f"Links to: https://freshmath.org")

if __name__ == "__main__":
    generate_qr_code()
