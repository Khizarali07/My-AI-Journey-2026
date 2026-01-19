import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# TOPIC: Exploratory Data Analysis (EDA) - The Full Loop
# ---------------------------------------------------------

# 1. CREATE "DIRTY" DATA
# Notice I put a 'None' (missing value) in there to simulate real life
data = {
    "Square_Feet": [1500, 2500, 1800, None, 3000, 1200],
    "Num_Bedrooms": [3, 5, 4, 3, 5, 2],
    "Age_Years": [10, 2, 15, 20, 1, 30],
    "Price": [300000, 500000, 320000, 280000, 550000, 200000],
}

df = pd.DataFrame(data)

# Print the initial DataFrame
print("Initial DataFrame:")
print(df)

# 2. DETECTIVE STEP 1: INSPECTION
print("--- MISSING VALUES ---")
# .isnull().sum() counts how many empty cells are in each column
print(df.isnull().sum())

# 3. DETECTIVE STEP 2: CLEANING
# We found a missing value in 'Square_Feet'. Let's drop that row.
df_clean = df.dropna()
print(f"\nRows remaining after cleaning: {len(df_clean)}")

# 4. DETECTIVE STEP 3: CORRELATION
# We use .corr() to see the mathematical relationships
corr_matrix = df_clean.corr()

print("\n--- CORRELATION MATRIX ---")
print(corr_matrix)

# 5. VISUALIZATION (The Heatmap)
# This draws the matrix.
# annot=True writes the numbers in the boxes.
# cmap='coolwarm' makes high correlations Red and low ones Blue.
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("What correlates with House Price?")
plt.show()

# OBSERVATION:
# Look at 'Price' vs 'Age_Years'. You will likely see a NEGATIVE number.
# This means: As Age goes UP, Price goes DOWN. The AI needs to learn this pattern.
