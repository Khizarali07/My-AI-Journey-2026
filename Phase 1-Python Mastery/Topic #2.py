# --- IF/ELSE EXAMPLE ---
battery_level = 15

# Check if battery is low
if battery_level < 20:
    print("Warning: Low Battery.")
elif battery_level == 100:
    print("Battery Full.")
else:
    print("System Normal.")

# --- FOR LOOP EXAMPLE ---
# A list of server names (we will cover Lists in 1.4, just treat this as a collection)
servers = ["Server-A", "Server-B", "Server-C", "Server-D", "Server-E"]

# Iterate through every server in the list
for server in servers:
    # If the server is 'Server-B', skip it (maybe it's under maintenance)
    if server == "Server-B":
        continue 
    
    # If we hit 'Server-D', stop everything
    if server == "Server-D":
        print("Critical Error on Server-D. Stopping.")
        break
    
    # Otherwise, print status
    print(f"Pinging {server}... Online.")

# --- WHILE LOOP EXAMPLE ---
power = 0
# Keep running while power is less than 3
while power < 3:
    print(f"Charging... Power at {power}%")
    power = power + 1