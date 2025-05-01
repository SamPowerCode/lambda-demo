def add_func(x, y):
    return x + y

add_lambda =lambda x, y: x + y

result_func = add_func(1, 2)
result_lambda = add_lambda(1, 2)
print(f"Function result: {result_func}")
print(f"Lambda result: {result_lambda}")

