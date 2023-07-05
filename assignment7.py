# Write a Python program to triple all numbers of a given list of integers. Use Python map.


# sample list:  [1, 2, 3, 4, 5, 6, 7]


# Triple of list numbers:

# 					[3, 6, 9, 12, 15, 18, 21]


#Solution

def triple_numbers(numbers):
    return list(map(lambda x: x * 3, numbers))

# Sample list
numbers = [1, 2, 3, 4, 5, 6, 7]

# Triple the numbers using map
tripled_numbers = triple_numbers(numbers)

# Print the result
print("Triple of list numbers:")
print(tripled_numbers)

