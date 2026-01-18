# --- LISTS & TUPLES ---
# A LIST of robot names (Changeable)
robots = ["R2-D2", "C-3PO", "BB-8", "Wall-E", "T-800"]

# A TUPLE of coordinates (Unchangeable/Read-Only)
base_location = (40.7128, -74.0060)

# --- SLICING ---
# Get the first robot (Index 0)
first = robots[0]  # "R2-D2"

# Get robots from index 1 up to (but not including) 4
team = robots[1:4] # ['C-3PO', 'BB-8', 'Wall-E']
print(team)

# Get the LAST robot (negative index counts from the end)
last = robots[-1]  # "T-800"
print(last)

# --- LIST COMPREHENSION ---
# Challenge: We want a new list with the length of every robot name.

# The "Old Way" (Loops):
name_lengths = []
for bot in robots:
    name_lengths.append(len(bot))

    print(name_lengths)

# The "Pythonic Way" (List Comprehension):
# Syntax: [ EXPRESSION for ITEM in LIST ]
name_lengths = [len(bot) for bot in robots]
print(name_lengths)
# Result: [5, 5, 4, 6, 5]