# --- DICTIONARIES ---
# Creating a dictionary of robot specs
robot_specs = {
    "model": "T-800",
    "status": "Active",
    "battery": 88
}

# Accessing data by KEY (not index)
print(f"Model: {robot_specs['model']}")  # Output: T-800

# Adding/Updating data
robot_specs["location"] = "Grid-7"  # New entry
robot_specs["battery"] = 87         # Update existing entry

# Loop through keys and values
for key, value in robot_specs.items():
    print(f"{key}: {value}")

# --- SETS ---
# A list with duplicates
raw_signals = [101, 102, 101, 103, 102, 104]

# Convert to a Set to remove duplicates instantly
unique_signals = set(raw_signals)
# Result: {101, 102, 103, 104}

# Check if something exists (Super fast in Sets!)
if 105 in unique_signals:
    print("Signal 105 detected.")
else:
    print("Signal 105 missing.")