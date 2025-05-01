my_numbers = [1, 2, 3, 4, 5]

def is_even_func(x):
    return x % 2 == 0


result_func = list(filter(is_even_func, my_numbers))

result_lambda = list(filter(lambda x: x % 2 == 0, my_numbers))


print(f"Function result: {result_func}")
print(f"Lambda result: {result_lambda}")