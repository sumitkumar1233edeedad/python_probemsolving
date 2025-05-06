# Question: Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]

# Create a list of integers from 0 to 9
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use the map function with a lambda to double each value in the list
print(list(map(lambda i: i*2, l)))