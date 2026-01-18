import numpy as np

# --- 1. CREATING DIMENSIONS ---
# 1D Array (Vector)
arr_1d = np.array([1, 2, 3, 4, 5, 6])

# 2D Array (Matrix) - List of Lists
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])

# --- 2. INSPECTING ---
# .shape is the most important command in AI. Memorize it.
print(f"Shape of 2D: {arr_2d.shape}")
# Output: (2, 3) -> 2 Rows, 3 Columns

# --- 3. RESHAPING ---
# We can turn our 1D array (6 items) into a 2D array (2x3)
# Note: 2 * 3 must equal 6, or it crashes.
reshaped = arr_1d.reshape(2, 3)
print(f"Reshaped:\n{reshaped}")

# --- 4. AGGREGATION (Math across Axes) ---
# axis=0 means "collapse the rows" (downwards)
# axis=1 means "collapse the columns" (sideways)
col_sums = arr_2d.sum(axis=0)  # [10+40, 20+50, 30+60]
print(f"Sum of columns (Axis 0): {col_sums}")  # [50, 70, 90]

# --- 5. INITIALIZERS (Shortcuts) ---
zeros = np.zeros((3, 3))  # 3x3 Matrix of pure zeros (Great for placeholders)
ones = np.ones((2, 2))  # 2x2 Matrix of pure ones

# --- 6. SAVING ---
# Save to disk
np.save("my_matrix.npy", arr_2d)
# Load from disk
loaded = np.load("my_matrix.npy")
print(f"Loaded from disk:\n{loaded}")
