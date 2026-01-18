import numpy as np

pixels = np.array([10, 255, 30, 0, 150, 240])

# Normalize pixel values to range 0-1
normalized_pixels = pixels / 255.0
print("Normalized Pixels:", normalized_pixels)

# Filter pixels with normalized value greater than 100
bright_pixels = pixels[pixels > 100]
print("Bright Pixels (Normalized > 100):", bright_pixels)
