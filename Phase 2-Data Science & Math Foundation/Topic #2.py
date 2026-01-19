import numpy as np

# ---------------------------------------------------------
# TOPIC: Statistics (Mean, Median, Std Dev)
# ---------------------------------------------------------

# GROUP 1: Consistent Students (All got B's)
group_a = [80, 82, 81, 79, 83]

# GROUP 2: Chaotic Students (Some F's, Some A+'s)
group_b = [50, 100, 50, 100, 100]

# --- MEAN (The Average) ---
# Calculate average for Group A
mean_a = np.mean(group_a)
# Calculate average for Group B
mean_b = np.mean(group_b)

print(f"Group A Average: {mean_a}")  # Output: 81.0
print(f"Group B Average: {mean_b}")  # Output: 80.0
# NOTICE: The averages are almost the same!
# If you only looked at the Mean, you would think these groups are identical.

# --- STANDARD DEVIATION (The Spread) ---
# This reveals the truth.
std_a = np.std(group_a)
std_b = np.std(group_b)

print(
    f"Group A Consistency (Std Dev): {std_a:.2f}"
)  # Output: 1.41 (Very Low, reliable)
print(
    f"Group B Consistency (Std Dev): {std_b:.2f}"
)  # Output: 24.49 (Very High, chaotic)

# --- MEDIAN (The Middle) ---
# Let's add a "Bill Gates" outlier to Group A
group_a_outlier = [80, 82, 81, 79, 83, 5000]  # Someone cheated and got 5000 points?

print(
    f"Mean with outlier: {np.mean(group_a_outlier):.2f}"
)  # Output: 900.83 (Total Lie)
print(
    f"Median with outlier: {np.median(group_a_outlier):.2f}"
)  # Output: 81.5 (The Truth)
