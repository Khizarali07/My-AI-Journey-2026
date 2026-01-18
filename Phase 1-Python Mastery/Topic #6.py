class Droid:
    # The Constructor: Runs when we create a new Droid
    def __init__(self, name, model):
        # We attach variables to 'self' so they stay with this specific object
        self.name = name
        self.model = model
        self.battery = 100  # All droids start with 100% battery
        print(f"Droid {self.name} is online.")

    # A Method (Action)
    def introduce(self):
        print(f"Hello, I am {self.name}, a {self.model} series droid.")

    # A Method that changes data
    def work(self):
        if self.battery >= 10:
            self.battery -= 10
            print(f"{self.name} is working... Battery at {self.battery}%")
        else:
            print(f"{self.name} is low on battery! Please charge.")

# --- Using the Class ---

# Create an Object (Instance) named 'r2'
# This calls __init__ automatically with "R2-D2" and "Astromech"
r2 = Droid("R2-D2", "Astromech")

# Call methods
r2.introduce() # Output: Hello, I am R2-D2...
r2.work()      # Output: R2-D2 is working... Battery at 90%
r2.work()      # Output: R2-D2 is working... Battery at 80%

# Create a SECOND object. Totally separate from r2.
c3 = Droid("C-3PO", "Protocol")
c3.introduce()