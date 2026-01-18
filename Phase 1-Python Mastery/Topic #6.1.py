# PARENT CLASS
class Robot:
    def __init__(self, name, version):
        self.name = name
        self.version = version
    
    def move(self):
        print(f"{self.name} is moving forward.")

# CHILD CLASS (Inherits from Robot)
# Syntax: class ChildName(ParentName):
class FlyingRobot(Robot):
    def __init__(self, name, version, rotor_count):
        # 1. Use super() to let the Parent handle the name/version setup
        super().__init__(name, version)
        
        # 2. Add specific logic for this Child
        self.rotor_count = rotor_count

    # New method specific to this child
    def fly(self):
        print(f"{self.name} is flying using {self.rotor_count} rotors!")

    # Overriding: Replacing a parent method with a new version
    def move(self):
        print(f"{self.name} is gliding through the air.")

# --- Using Inheritance ---

generic_bot = Robot("Gen-1", 1.0)
generic_bot.move() 
# Output: Gen-1 is moving forward.

drone = FlyingRobot("SkyNet", 2.0, 4)
drone.move()  # Uses the OVERRIDDEN method
# Output: SkyNet is gliding through the air.
drone.fly()   # Uses the NEW method
# Output: SkyNet is flying using 4 rotors!