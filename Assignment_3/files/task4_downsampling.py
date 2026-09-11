import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Task 4 - Spatial Downsampling & Pixelation via Striding

img = Image.open("sample.jpg")
img = np.array(img)

N = 8

original_shape = img.shape
original_bytes = img.nbytes

# take every Nth pixel along rows and cols
downsampled = img[::N, ::N, :]

down_shape = downsampled.shape
down_bytes = downsampled.nbytes

# blow it back up to original size to see the pixelation
pixelated = np.repeat(downsampled, N, axis=0)
pixelated = np.repeat(pixelated, N, axis=1)

# in case the original dims weren't perfectly divisible by N, trim/pad to match
pixelated = pixelated[:original_shape[0], :original_shape[1], :]

dim_reduction = (1 - (down_shape[0] * down_shape[1]) / (original_shape[0] * original_shape[1])) * 100
mem_reduction = (1 - down_bytes / original_bytes) * 100

print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
print(f"Original Shape : {original_shape} | Memory: {original_bytes:,} bytes")
print(f"Downsampled Shape : {down_shape} | Memory: {down_bytes:,} bytes")
print(f"Re-expanded Shape : {pixelated.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction: {dim_reduction:.2f}% reduction")
print(f"Memory Savings : {mem_reduction:.2f}% data reduction")

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img)
axes[0].set_title("Original")
axes[1].imshow(pixelated)
axes[1].set_title(f"Pixelated (N={N})")
for ax in axes:
    ax.axis("off")
plt.tight_layout()
plt.show()
