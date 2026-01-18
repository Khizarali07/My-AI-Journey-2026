# Function to calculate flight time
def calculate_flight_time(distance, speed):

    time = distance / speed
    return time

# Example usage
target_distance = 500
drone_speed = 120

# Calculate estimated drone flight time
estimated_time = calculate_flight_time(target_distance, drone_speed)

# Print the result
print(f"Estimated flight time: {estimated_time:.2f} hours")
