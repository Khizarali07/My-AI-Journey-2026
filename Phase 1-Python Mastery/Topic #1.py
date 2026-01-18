# Create a variable named 'system_name' holding a String (text)
system_name = "Jarvis"

# Create a variable named 'system_version' holding an Integer (whole number)
system_version = 1

# OUTPUT: Print a message to the screen
print("System initializing...")

# INPUT: Ask the user for their name and store it in a variable called 'user_name'
# The program pauses here until you type something and hit Enter
user_name = input("Please identify yourself: ")

# LOGIC: Let's calculate the next version number
# We take the current version (1) and add 1 to it
next_version = system_version + 1

# OUTPUT using f-strings (Formatted String Literals)
# Notice the 'f' before the first quote. This lets us use {variable_name} inside.
print(f"Welcome, {user_name}. I am {system_name} version {system_version}.")
print(f"Update ready. Preparing to install version {next_version}...")