"""
Q10.
"""

string = "CP1404 is not good"

new_string = " ".join(list(string.split())[-1::-1])

print(new_string)
