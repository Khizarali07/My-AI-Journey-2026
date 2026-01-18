import time
import numpy as np  # Standard industry alias

# 1. CREATING ARRAYS
# A massive list (1 Million items) to see the speed difference
data_list = list(range(1, 1_000_001))
# Convert to NumPy Array
data_array = np.array(data_list)

print(f"Processing {len(data_list):,} items...")
# print(f"List: {data_list}") # Too big to print
# print(f"Array: {data_array}") # Too big to print

# 2. VECTORIZATION (The Superpower)
# Task: Multiply every number by 10.

# The Old Way (Slow Loop)
start_time = time.time()
new_list = []
for x in data_list:
    new_list.append(x * 10)

end_time = time.time()  # Placeholder for timing
# print(f"Multiplied List: {new_list}")
print(
    f"Time taken (Old Way): {end_time - start_time:.5f} seconds"
)  # Placeholder for timing

start_time = time.time()
# The NumPy Way (Fast & Clean)
new_array = data_array * 10
end_time = time.time()

# print(f"Multiplied Array: {new_array}")
print(
    f"Time taken (NumPy Way): {end_time - start_time:.5f} seconds"
)  # Placeholder for timing

# 3. FILTERING (B oolean Indexing)
# Task: Get all numbers greater than 20
# This creates a mask of True/False, then picks only the True ones
high_values = new_array[new_array > 20]
# print(f"Values > 20: {high_values}")
print(f"Count of Values > 20: {len(high_values):,}")
