# Exercise 1: Simple Addition Function
# Create a Python function named `add` that takes two parameters, `a` and `b`,
# and returns their sum.
# 
# Answer:
# def add(a, b):
#     return a + b
# 
# Write the function and test it with different values for `a` and `b`.

# Exercise 2: Addition and Subtraction Functions
# Extend the first exercise by creating two functions: `add` and `subtract`.
# The `add` function should take two parameters, `a` and `b`, and return their sum.
# The `subtract` function should take two parameters, `a` and `b`, and return the result of `a - b`.
# 
# Answer:
# def add(a, b):
#     return a + b
# 
# def subtract(a, b):
#     return a - b
# 
# Write both functions and test them with different values.

# Exercise 3: Working with Arrays
# Create a function named `sum_array` that takes a single parameter, `arr`, which is a list of numbers.
# The function should return the sum of all numbers in the list.
# 
# Answer:
# def sum_array(arr):
#     return sum(arr)
# 
# Write the function and test it with different lists of numbers.

# Exercise 4: Array Manipulation Follow-Up
# Using the `sum_array` function from Exercise 3, create another function named `average_array`.
# This function should calculate and return the average of all numbers in the list.
# 
# Answer:
# def average_array(arr):
#     return sum_array(arr) / len(arr)
# 
# Write the `average_array` function and test it with different lists of numbers.

# Exercise 5: Comprehensive List Exercise
# Create a function named `process_numbers` that takes a list of numbers as input.
# The function should return a dictionary with the following keys and values:
# - `sum`: The sum of all numbers (use the `sum_array` function).
# - `average`: The average of all numbers (use the `average_array` function).
# - `max`: The maximum value in the list.
# - `min`: The minimum value in the list.
# 
# Answer:
# def process_numbers(numbers):
#     return {
#         "sum": sum_array(numbers),
#         "average": average_array(numbers),
#         "max": max(numbers),
#         "min": min(numbers)
#     }
# 
# Write the `process_numbers` function and test it with different lists of numbers.
