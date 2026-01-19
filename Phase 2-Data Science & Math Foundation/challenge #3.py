import pandas as pd

inventory = {
    "Fruit": ["Apple", "Banana", "Cherry", "Date"],
    "Price": [0.50, 0.30, 0.10, 1.20],
    "Stock": [100, 200, 50, 20],
}

# Create DataFrame from the inventory dictionary
df = pd.DataFrame(inventory)
print(f"Table:\n{df}")

# First 3 rows of the DataFrame
first_three_rows = df.head(3)
print(f"\nFirst 3 rows:\n{first_three_rows}")

# Summary statistics of the DataFrame
summary_statistics = df.describe()
print(f"\nSummary statistics:\n{summary_statistics}")

# Claculating total inventory value
df["Total Value"] = df["Price"] * df["Stock"]
total_inventory_value = df["Total Value"].sum()

print(f"\nTotal inventory value: ${total_inventory_value:.2f}")
