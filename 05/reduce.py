'''
The reduce() function is part of the functools module and is used to apply a function cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.

    Syntax: reduce(function, iterable[, initializer])

    Parameters:
        function: A function of two arguments. It is applied cumulatively to the items of the iterable.
        iterable: The iterable whose items are to be reduced.
        initializer (optional): A value that is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty.
'''
from functools import reduce

my_numbers = [1, 2, 3, 4, 5]
# 3
# 6
# 10
# 15

sum_of_numbers = reduce(lambda accumulator, next_num: accumulator + next_num, my_numbers)
print(f"Sum of numbers: {sum_of_numbers}")

max_value = reduce(lambda accumulator, next_num: accumulator if accumulator > next_num else next_num, my_numbers)
print(f"Max value: {max_value}")


from functools import reduce
import math

# 1. Sum of All Elements in a List
numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, numbers)
print("Total sum:", total_sum)  # Output: 15

# 2. Product of All Elements in a List
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)  # Output: 120

# 3. Find the Maximum Element in a List
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum:", maximum)  # Output: 5

# 4. Concatenate a List of Strings
words = ["Hello", "world", "from", "reduce"]
sentence = reduce(lambda x, y: x + " " + y, words)
print("Concatenated sentence:", sentence)  # Output: "Hello world from reduce"

# 5. Calculate the GCD of a List of Numbers
numbers_for_gcd = [48, 64, 80]
gcd = reduce(lambda x, y: math.gcd(x, y), numbers_for_gcd)
print("GCD:", gcd)  # Output: 16

# 6. Flatten a List of Lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened_list = reduce(lambda x, y: x + y, list_of_lists)
print("Flattened list:", flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
