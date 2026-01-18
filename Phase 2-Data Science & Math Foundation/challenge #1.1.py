import numpy as np

arr_1d = np.arange(12)

arr_3d = arr_1d.reshape((3, 2, 2))

print("1D Array:")
print(arr_1d)
print("\n3D Array:")
print(arr_3d)

# Calculate the Mean (Average) brightness of each image
mean_brightness = arr_3d.mean(
    axis=(1)
)  # Axis(1,2) means 1 collapse from column and 2 means how much row to collapse

# original_shape
print("Original Shape:", arr_3d.shape)
# mean_brightness_shape
print("Mean Brightness Shape:", mean_brightness.shape)
print("Mean Brightness of each image:", mean_brightness)

arr_3d_new = arr_1d.reshape((6, 2, 1))
print("\n3D Array:")
print(arr_3d_new)

# Calculate the Mean (Average) brightness of each image
mean_brightness = arr_3d_new.mean(
    axis=(1, 2)
)  # Axis(1,2) means 1 collapse from column and 2 means how much row to collapse

# original_shape
print("Original Shape:", arr_3d_new.shape)
# mean_brightness_shape
print("Mean Brightness Shape:", mean_brightness.shape)
print("Mean Brightness of each image:", mean_brightness)

np.save("mean_brightness.npy", mean_brightness)

loaded = np.load("mean_brightness.npy")

# Verify loaded data
print("Loaded Mean Brightness from .npy file:", loaded)
