import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Task 3 - Channel Slicing & Isolation
# put your own image in the same folder and name it sample.jpg (or change path below)

img = Image.open("sample.jpg")
img = np.array(img)

print("--- CHANNEL EXTRACTION SUMMARY ---")
print("Original Image Shape :", img.shape)

# 2D grids for each channel
red_channel = img[:, :, 0]
green_channel = img[:, :, 1]
blue_channel = img[:, :, 2]

print(f"Red Channel 2D Shape : {red_channel.shape} | Mean Intensity: {red_channel.mean():.2f}")
print(f"Green Channel 2D Shape: {green_channel.shape} | Mean Intensity: {green_channel.mean():.2f}")
print(f"Blue Channel 2D Shape : {blue_channel.shape} | Mean Intensity: {blue_channel.mean():.2f}")

# build 3-channel images where only one channel has data, rest are zero
red_only = np.zeros_like(img)
red_only[:, :, 0] = red_channel

green_only = np.zeros_like(img)
green_only[:, :, 1] = green_channel

blue_only = np.zeros_like(img)
blue_only[:, :, 2] = blue_channel

# 2x3 grid - top row colored, bottom row grayscale
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red Only")
axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green Only")
axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue Only")

axes[1, 0].imshow(red_channel, cmap="gray")
axes[1, 0].set_title("Red Grayscale")
axes[1, 1].imshow(green_channel, cmap="gray")
axes[1, 1].set_title("Green Grayscale")
axes[1, 2].imshow(blue_channel, cmap="gray")
axes[1, 2].set_title("Blue Grayscale")

for ax in axes.flat:
    ax.axis("off")

plt.tight_layout()
plt.show()

print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")
