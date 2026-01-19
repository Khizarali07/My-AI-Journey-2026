import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
df = pd.DataFrame(
    {"Month": ["Jan", "Feb", "Mar", "Apr", "May"], "Users": [100, 150, 300, 700, 1200]}
)

# Set the figure size
plt.figure(figsize=(8, 5))

# Create a bar plot
sns.barplot(x="Month", y="Users", data=df, palette="viridis")

# Add title and labels
plt.title("Number of Users Over Months", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Number of Users", fontsize=14)

# Show the plot
plt.show()
