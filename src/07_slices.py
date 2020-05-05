"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
a_one = slice(1, 2, 1)
print(a[a_one])

# Output the second-to-last element: 9
a_two = slice(-2, -3, -1)
print(a[a_two])

# Output the last three elements in the array: [7, 9, 6]
a_three = slice(3, 6, 1)
print(a[a_three])

# Output the two middle elements in the array: [1, 7]
a_four = slice(2, 4, 1)
print(a[a_four])

# Output every element except the first one: [4, 1, 7, 9, 6]
a_five = slice(1, 6, 1)
print(a[a_five])

# Output every element except the last one: [2, 4, 1, 7, 9]
a_six = slice(0, 5, 1)
print(a[a_six])

# For string s...

s = "Hello, world!"
new_string = slice(6, 12, 1)

# Output just the 8th-12th characters: "world"
print(s[new_string])