"""
Q9.
"""

class Building:

    def __init__(self, name, maximum_occupancy):
        self.name = name
        self.maximum_occupancy = maximum_occupancy

    def will_fit(self, number):
        return number <= self.maximum_occupancy

b = Building("Innovation", 1200)
result = b.will_fit(1201)
print(result)
