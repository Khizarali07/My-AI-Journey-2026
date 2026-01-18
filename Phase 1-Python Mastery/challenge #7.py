def save_user_data(username, age):

    try:
        age = int(age)

        file = "database.txt"
        with open(file, "a") as f:
            f.write(f"User: {username}, Age: {age}\n")
            print("User data saved successfully.")

    except ValueError:
        print("Error: Age must be a number.")
        return
    finally:
        print("Execution completed.")


# Example usage
save_user_data("Alice", 30)
save_user_data("Bob", "unknown")

# Example of using the decorator


def additional_info_decorator(func):
    def wrapper(username, age):
        print("Starting user registration...")
        func(username, age)
        print("User registration completed.")

    return wrapper


@additional_info_decorator
def register_user(username, age):
    with open("database_for_decorator.txt", "a") as f:
        f.write(f"Registered User: {username}, Age: {age}\n using decorator\n")


# Example usage of the decorated function
register_user("Charlie", 25)
