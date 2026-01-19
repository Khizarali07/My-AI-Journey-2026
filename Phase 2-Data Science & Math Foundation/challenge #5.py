import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dataset creation
df = pd.DataFrame(
    {
        "Mileage": [50000, 20000, 100000, 15000, None, 80000],
        "Year": [2015, 2020, 2010, 2021, 2018, 2012],
        "Price": [15000, 25000, 8000, 28000, 18000, 10000],
    }
)

# Print the initial DataFrame
print(f"Initial DataFrame:\n{df}\n")

# Step 1: Inspect for missing values
print("Missing Values:\n", df.isnull().sum(), "\n")

# Fill the missing Mileage with the Median of that column
df["Mileage"].fillna(df["Mileage"].median(), inplace=True)

# Correlation matrix
corr_matrix = df.corr()
print("Correlation Matrix:\n", corr_matrix, "\n")

# Visualization: Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Car Features Correlation Heatmap")
plt.show()

# Observation:
# Look at 'Price' vs 'Mileage'. You will likely see a NEGATIVE number.
# This means: As Mileage goes UP, Price goes DOWN. The AI needs to learn this pattern.
