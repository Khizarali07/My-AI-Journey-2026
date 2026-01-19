import pandas as pd

# ---------------------------------------------------------
# TOPIC: Pandas Basics (Creating & Inspecting DataFrames)
# ---------------------------------------------------------

# 1. CREATE DATA
# We use a dictionary to represent the columns
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Job": ["Engineer", "Doctor", "Artist", "Chef"],
    "Salary": [70000, 120000, 45000, 60000],
}

# 2. LOAD INTO PANDAS
# This creates the "DataFrame" (the table)
df = pd.DataFrame(data)

# 3. INSPECT DATA
# .head(n) shows the top n rows. Good for a quick peek at massive data.
print("--- TOP 2 ROWS ---")
print(df.head(2))

# .info() gives us the technical summary (Data types, missing values)
# Essential to check if your numbers were accidentally read as text.
print("\n--- TABLE INFO ---")
print(df.info())

# .describe() gives us instant statistics (Mean, min, max) for numeric columns
# It automatically ignores text columns like "Name".
print("\n--- STATISTICS ---")
print(df.describe())

# 4. SELECTING A COLUMN
# We can grab just one column (a "Series") like a dictionary key
print(f"\nAverage Age: {df['Age'].mean()}")
