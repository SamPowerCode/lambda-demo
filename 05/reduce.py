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
