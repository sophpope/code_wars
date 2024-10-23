# Write a function that accepts a number as an input and returns
# a list of integers that stretch from 0 up to the given number
# (including the number!) in the increments of 5. But your list must EXCLUDE
# any numbers that can be divided by 7 without a remainder.

# 1. We only pass one integer to the function that is int > 0 - greater than 0

def num_list(int):
    # a list of integers that stretch from 0 up to the given number (including the number!) in the increments of 5.
    return [i for i in range(0, int+1, 5) if i % 7 != 0]

print(num_list(201))