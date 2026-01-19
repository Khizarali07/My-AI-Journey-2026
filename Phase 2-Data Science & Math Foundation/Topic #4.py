import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ---------------------------------------------------------
# TOPIC: Visualization (Line & Scatter Plots)
# ---------------------------------------------------------

# 1. PREPARE DATA
data = {
    "Years_Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary_k": [40, 42, 50, 55, 65, 70, 85, 90, 95, 110],
}
df = pd.DataFrame(data)

# 2. SETUP THE CANVAS (Matplotlib)
# figsize=(width, height) in inches
plt.figure(figsize=(10, 6))

# 3. DRAW THE PLOT (Seaborn)
# We use a 'lineplot' to show trends over time/progression
# x = horizontal axis, y = vertical axis
sns.lineplot(data=df, x="Years_Experience", y="Salary_k", marker="o", color="blue")

# 4. CUSTOMIZE LABELS (Matplotlib)
plt.title("Software Engineer Salary Trajectory")
plt.xlabel("Years of Experience")
plt.ylabel("Salary (in Thousands)")
plt.grid(True)  # Adds a grid behind the lines for easier reading

# 5. SHOW THE PLOT
# This pops up the window with the graph
plt.show()
