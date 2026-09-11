import math

# Task 1 - Display Pixel Density Calculator

w = int(input("Enter horizontal resolution (pixels): "))
h = int(input("Enter vertical resolution (pixels): "))
d = float(input("Enter physical diagonal size (inches): "))

# total pixels
total_pixels = w * h

# aspect ratio using gcd
g = math.gcd(w, h)
ratio_w = w // g
ratio_h = h // g

# diagonal pixel count (pythagoras)
diagonal_px = math.sqrt(w**2 + h**2)

# dpi formula
dpi = diagonal_px / d

# classify density
if dpi < 100:
    category = "Low Density (Standard Monitor)"
elif dpi <= 200:
    category = "Medium Density (HD Display)"
else:
    category = "High Density (Retina / Mobile)"

print("\n--- DISPLAY METRICS ANALYSIS ---")
print(f"Total Pixel Count : {total_pixels:,} pixels")
print(f"Aspect Ratio : {ratio_w}:{ratio_h}")
print(f"Calculated DPI : {dpi:.2f} DPI")
print(f"Density Category : {category}")
