# Password Authentication System
correct_password="OpenSesame"

attempt = 0


# This Loop will run until the user has made 3 attempts
while attempt < 3:
    # Ask the user to enter the password
    user_input = input("Enter the password: ")

    # Check if the entered password is correct
    if user_input == correct_password:
        print("Access Granted.")
        break

    # If the password is incorrect
    else:
        attempt += 1
        print(f"Access Denied. You have {3 - attempt} attempts left.")
    # After 3 failed attempts, lock the system
    if attempt == 3 :
        print("Too many failed attempts. System Locked.")
