my_numbers = [1, 2, 3, 4, 5]

def square_func(x):
    return x ** 2

result_func = list(map(square_func, my_numbers))
result_lambda = list(map(lambda x: x ** 2, my_numbers))


print(f"Function result: {result_func}")
print(f"Lambda result: {result_lambda}")

