inventory = {
    "Potion": 5,
    "Sword": 1,
    "Map": 1
}

inventory["Potion"] += 3  # Player found 3 more Potions
inventory["Gold Coin"]= 50 # Player found 50 Gold Coins

# List with duplicates
loot_list = ["Sword", "Shield", "Sword", "Ring", "Shield"]

unique_loot = set(loot_list)

print(inventory)
# Output: {'Potion': 3, 'Sword': 1, 'Map': 1, 'Gold Coin': 50}
print(unique_loot)
# Output: {'Ring', 'Shield', 'Sword'}
