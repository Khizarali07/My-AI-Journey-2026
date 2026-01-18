# Define the robot model name
model_name = "Optimus"

# Define the current year for calculation context
current_year = 2026

# Output a startup message
print("Initializing system...")

# Input: Ask for birth year and convert the string input to an integer immediately
birth_year = int(input("Enter your birth year: "))

# Logic: Calculate age directly inside the f-string
# We subtract the birth year from the constant current_year
print(f"Scanning {model_name}... You are approximately {current_year - birth_year} years old.")