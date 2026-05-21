---
title: "Image Mosaic Generator in Python"
author: "Juan Carlos Rubio Polania, PhD"
date: "2025-05-07"
---
  

# Image Mosaic Generator in Python 🖼️🐍

## Overview

This repository demonstrates a simple workflow for generating image mosaics using Python and the Pillow (`PIL`) library.

The script loads multiple images, resizes them into uniform dimensions, and combines them into a single mosaic image arranged in a grid layout.

Although animal and plastic images are used as examples in this project, the workflow can be adapted to many other applications, including:
- Computer vision datasets
- Deep learning visualization
- Ecological monitoring
- Satellite imagery
- Biodiversity datasets
- Image comparison panels
- Social media content
- Scientific figures

The implementation creates a 2 × 2 mosaic where each image occupies a predefined section of the canvas.

---

# Features

- 🖼️ Automatic image mosaics
- 📏 Image resizing
- ⚡ Fast image composition
- 💻 Simple Python workflow
- 📂 Automatic output directory creation
- 🧠 Adaptable to multiple image categories

---

# Required Packages

```python
from PIL import Image
import os
```

---

# Workflow

## 1. Define Image Paths

```python
Image1 = r"C:/Users/Image1.jpg"
Image2 = r"C:/Users/Image2.jpg"
```

The script loads image paths that will be used in the mosaic.

---

## 2. Create Image Groups

```python
L1 = [Image1, Image2, Image3, Image4]
```

Each list represents a mosaic composition.

---

## 3. Create Mosaic Canvas

```python
mosaico = Image.new('RGB', (640, 640))
```

A blank image canvas is generated.

---

## 4. Define Image Positions

```python
Pos = [
    (0, 0),
    (320, 0),
    (0, 320),
    (320, 320)
]
```

Each coordinate defines where an image will be pasted.

---

## 5. Resize and Paste Images

```python
img_resized = img.resize((320, 320))
mosaico.paste(img_resized, Pos)
```

All images are resized to maintain a consistent mosaic structure.

---

## 6. Save Final Mosaic

```python
mosaico.save("Mosaic.jpg")
```

The final mosaic image is exported.

---

# Example Layout

```text
+-------------+-------------+
|   Image 1   |   Image 2   |
+-------------+-------------+
|   Image 3   |   Image 4   |
+-------------+-------------+
```

---

# Applications

This workflow can be useful for:

- 🧠 Deep learning datasets
- 📊 Computer vision projects
- 🌿 Ecological monitoring
- 🛰️ Remote sensing
- 📚 Scientific publications
- 🎥 Social media visualizations
- 🖼️ Automated figure generation

---

# Requirements

- Python
- Pillow (PIL)

Install Pillow using:

```bash
pip install pillow
```

---

# License

This project is licensed under the MIT License.

---

# Author

Juan Carlos Rubio Polania, PhD
