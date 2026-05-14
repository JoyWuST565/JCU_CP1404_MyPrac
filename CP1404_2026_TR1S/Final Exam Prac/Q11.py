"""
Q11.
"""

calories = [75, 65, 6175]
food = ["Egg", "Apple", "Carrot Cake"]

def create_dictionary(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result

print(create_dictionary(food, calories))
