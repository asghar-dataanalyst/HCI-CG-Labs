import numpy as np

# Task 2 - Environment Setup & Synthetic Image Matrix Creation
# make sure numpy, pillow and matplotlib are installed first:
# pip install numpy pillow matplotlib

# blank black image, 300 rows x 400 cols x 3 channels
img = np.zeros((300, 400, 3), dtype=np.uint8)

mid_h = 300 // 2   # 150
mid_w = 400 // 2   # 200

# top left - red
img[0:mid_h, 0:mid_w] = [255, 0, 0]

# top right - green
img[0:mid_h, mid_w:400] = [0, 255, 0]

# bottom left - blue
img[mid_h:300, 0:mid_w] = [0, 0, 255]

# bottom right - white
img[mid_h:300, mid_w:400] = [255, 255, 255]

print("--- SYNTHETIC MATRIX METRICS ---")
print("Array Shape (H, W, C) :", img.shape)
print("Data Type :", img.dtype)
print(f"Total Elements : {img.size:,} values")
print(f"Memory Footprint : {img.nbytes:,} bytes ({img.nbytes/1024:.2f} KB)")

# optional - to actually see the image, uncomment below
# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.show()
