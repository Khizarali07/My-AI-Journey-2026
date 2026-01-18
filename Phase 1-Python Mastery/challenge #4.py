temps_celsius = [22.5, 25.0, 19.8, 28.4, 30.1, 21.0]

recent_temps = temps_celsius[3:] # Slicing to get last 3 temperatures

# The robust way to always get the last 3 items:
recent_temps = temps_celsius[-3:] # Slicing to get last 3 temperatures

print(recent_temps)  # Output: [28.4, 30.1, 21.0]

temps_fahrenheit = [temp * 9/5 + 32 for temp in recent_temps]

print(temps_fahrenheit)  # Output: [83.12, 86.18, 69.8]