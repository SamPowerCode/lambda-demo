'''
The map() function applies a given function to all items in an iterable (like a list) and returns an iterator that produces the results.

    Syntax: map(function, iterable, ...)

    Parameters:
        function: A function that is applied to each item of the iterable(s).
        iterable: One or more iterables.
'''

my_numbers = [1, 2, 3, 4, 5]

def square_func(x):
    return x ** 2

result_func = list(map(square_func, my_numbers))
result_lambda = list(map(lambda x: x ** 2, my_numbers))


print(f"Function result: {result_func}")
print(f"Lambda result: {result_lambda}")

# 1. Using map() with a List
celsius_temps = [0, 20, 30, 100]
fahrenheit_temps = map(lambda c: (c * 9/5) + 32, celsius_temps)
print("Fahrenheit temperatures:", list(fahrenheit_temps))  # Output: [32.0, 68.0, 86.0, 212.0]

# 2. Using map() with a Tuple
numbers = (1, 2, 3, 4)
squared_numbers = map(lambda x: x ** 2, numbers)
print("Squared numbers:", tuple(squared_numbers))  # Output: (1, 4, 9, 16)

# 3. Using map() with a String
text = "hello"
ascii_values = map(lambda char: ord(char), text)
print("ASCII values:", list(ascii_values))  # Output: [104, 101, 108, 108, 111]

# 4. Using map() with Multiple Iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = map(lambda x, y: x + y, list1, list2)
print("Sum of lists:", list(sum_list))  # Output: [5, 7, 9]

# 5. Using map() with a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
uppercase_keys = map(lambda key: key.upper(), my_dict.keys())
print("Uppercase keys:", list(uppercase_keys))  # Output: ['A', 'B', 'C']

# 6. Using map() with a Set
numbers_set = {1, 2, 3, 4}
doubled_numbers = map(lambda x: x * 2, numbers_set)
print("Doubled numbers:", set(doubled_numbers))  # Output: {2, 4, 6, 8}