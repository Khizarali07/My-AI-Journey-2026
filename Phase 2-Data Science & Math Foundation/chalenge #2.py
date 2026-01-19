import numpy as np

city_temps = [20, 22, 19, 21, 20, 100]

# Mean of the temperatures
mean_temp = np.mean(city_temps)
print("Mean Temperature:", f"{mean_temp:.2f}")

# Median of the temperatures
median_temp = np.median(city_temps)
print("Median Temperature:", f"{median_temp:.2f}")

# I WILL ALWAYS TRUST MEDIAN MORE THAN MEAN IN PRESENCE OF OUTLIERS

# Standard Deviation of the temperatures
std_dev_temp = np.std(city_temps)
print("Standard Deviation of Temperature:", f"{std_dev_temp:.2f}")
