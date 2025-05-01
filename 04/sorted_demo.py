values = [(1, 'b', 'Square'), (2, 'a', 'Spongebob'), (3, 'c', 'pants')]

def sort_func(x):
    return x[1]

result_func = sorted(values, key=sort_func)

result_lambda = sorted(values, key=lambda x: x[1])


print(f"Function result: {result_func}")
print(f"Lambda result: {result_lambda}")

print(f"{result_lambda[0][2]} {result_lambda[1][2]}{result_lambda[2][2]}")