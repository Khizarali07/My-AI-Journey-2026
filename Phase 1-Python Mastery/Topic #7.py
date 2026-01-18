# --- 1. TRY / EXCEPT ---
def safe_division(a, b):
    try:
        # Try to run this risky code
        result = a / b
        return result
    except ZeroDivisionError:
        # If the specific error happens, run this instead
        return "Error: Cannot divide by zero."
    except Exception as e:
        # Catch any other unexpected error
        return f"Unexpected Error: {e}"

# --- 2. FILE I/O ---
# 'w' mode = Write (Overwrites file). 'a' = Append (Adds to end). 'r' = Read.
# The 'with' block ensures the file closes automatically.
filename = "system_logs.txt"

with open(filename, "w") as file:
    file.write("System Log Started.\n")
    file.write("User: Admin logged in.\n")

# Reading the file back
with open(filename, "r") as file:
    content = file.read()
    print("--- File Content ---")
    print(content)

# --- 3. DECORATORS (The Advanced Concept) ---
# A decorator is a function that takes a function and returns a new function.

def logger_decorator(func):
    def wrapper():
        print(f"LOG: Running function '{func.__name__}'...")
        func() # Run the original function
        print("LOG: Finished.")
    return wrapper

# Apply the decorator using '@'
@logger_decorator
def run_backup():
    print("...Backup in progress...")

# Calling the function triggers the wrapper logic
run_backup()
# Output:
# LOG: Running function 'run_backup'...
# ...Backup in progress...
# LOG: Finished.