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
