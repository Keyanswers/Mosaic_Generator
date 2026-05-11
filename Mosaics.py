# ==========================================
# PACKAGES
# ==========================================

# Operating system utilities
import os

# OpenCV library
import cv2 as cv

# Path handling utilities
from pathlib import Path

# Python Imaging Library (PIL)
from PIL import Image

# ==========================================
# IMAGE PATHS
# Example paths were simplified
# ==========================================

# Squirrel images
Squire1 = r"C:/Users/Image1.jpg"
Squire2 = r"C:/Users/Image2.jpg"

Squire3 = r"C:/Users/Image3.jpg"
Squire4 = r"C:/Users/Image4.jpg"

Squire5 = r"C:/Users/Image5.jpg"

# Iguana images
Iguana1 = r"C:/Users/Image6.jpg"
Iguana2 = r"C:/Users/Image7.jpg"

Iguana3 = r"C:/Users/Image8.jpg"
Iguana4 = r"C:/Users/Image9.jpg"

Iguana5 = r"C:/Users/Image10.jpg"

# Plastic images
Plas1 = r"C:/Users/Image11.jpg"
Plas2 = r"C:/Users/Image12.jpg"

Plas3 = r"C:/Users/Image13.jpg"
Plas4 = r"C:/Users/Image14.jpg"

Plas5 = r"C:/Users/Image15.jpg"

Plas6 = r"C:/Users/Image16.jpg"
Plas7 = r"C:/Users/Image17.jpg"

Plas8 = r"C:/Users/Image18.jpg"
Plas9 = r"C:/Users/Image19.jpg"

Plas10 = r"C:/Users/Image20.jpg"

# ==========================================
# IMAGE GROUPS
# Each list contains four images
# that will form one mosaic
# ==========================================

L1 = [Squire1, Iguana1, Plas1, Plas6]
L2 = [Squire2, Iguana2, Plas2, Plas7]
L3 = [Squire3, Iguana3, Plas3, Plas8]
L4 = [Squire4, Iguana4, Plas4, Plas9]
L5 = [Squire5, Iguana5, Plas5, Plas10]

# ==========================================
# CREATE MOSAIC CANVAS
# A blank RGB image of 640x640 pixels
# ==========================================

mosaico = Image.new('RGB', (640, 640))

# ==========================================
# POSITIONS FOR EACH IMAGE
# Each image will occupy a 320x320 section
# ==========================================

Pos = [
    (0, 0),  # Top-left
    (320, 0),  # Top-right
    (0, 320),  # Bottom-left
    (320, 320)  # Bottom-right
]

# ==========================================
# PASTE EACH IMAGE INTO THE MOSAIC
# ==========================================

for img_path, Pos in zip(L5, Pos):
    # Open image
    with Image.open(img_path) as img:
        # Resize image to fit mosaic section
        img_resized = img.resize((320, 320))

        # Paste resized image into mosaic
        mosaico.paste(img_resized, Pos)

# ==========================================
# OUTPUT DIRECTORY
# Create directory if it does not exist
# ==========================================

OutPutDir = r"C:/Users/Mosaics"

os.makedirs(OutPutDir,
            exist_ok=True)

# ==========================================
# SAVE FINAL MOSAIC
# ==========================================

mosaico.save(
    os.path.join(OutPutDir,
                 "Mosaic_L5.jpg")
)

# ==========================================
# END
# ==========================================