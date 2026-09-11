# HCI & CG - Lab 1 (Display Density Metrics & Image Array Mechanics in NumPy)

This repo has my Lab 1 submission for the Human-Computer Interaction and Computer Graphics course. The lab is basically about two things - figuring out screen density (DPI/PPI) with a bit of math, and playing around with images as NumPy arrays.

## What's in here

- `HCI_CG_Asghar_Hussain.pptx` - this is my Assignment 1 slides, added here along with Lab 1 stuff.
- `task1_dpi_calculator.py` - takes screen width, height and diagonal size as input and calculates total pixels, aspect ratio and DPI, then tells you if the screen is low/medium/high density.
- `task2_synthetic_image.py` - builds a blank 300x400 image from scratch using `np.zeros()` and fills each quarter with a different color (red, green, blue, white).
- `task3_channel_slicing.py` - loads `sample.jpg`, pulls out the Red, Green and Blue channels separately, and shows them in a 2x3 plot (colored on top, grayscale on bottom).
- `task4_downsampling.py` - shrinks `sample.jpg` by taking every 8th pixel, then blows it back up so you can see the pixelation, and prints how much memory got saved.
- `sample.jpg` - the test image used for tasks 3 and 4.
- `screenshots/` - output screenshots for all four tasks.

## How to run it

1. Install the needed packages first:
```
pip install numpy pillow matplotlib
```

2. Run whichever task you want:
```
python task1_dpi_calculator.py
python task2_synthetic_image.py
python task3_channel_slicing.py
python task4_downsampling.py
```

For task 1 you'll be asked to type in the resolution and screen size. Tasks 3 and 4 need `sample.jpg` to be in the same folder as the script.

## Short answer question

**Why does RGBA use 33% more memory than RGB?**

RGB stores 3 bytes per pixel (Red, Green, Blue). RGBA adds a 4th channel, Alpha, which controls transparency, so it's 4 bytes per pixel instead of 3. Going from 3 to 4 bytes is a 1/3 increase, which comes out to 33% more memory.
