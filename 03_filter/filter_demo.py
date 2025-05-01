'''
The filter() function constructs an iterator from elements of an iterable for which a function returns True.

    Syntax: filter(function, iterable)

    Parameters:
        function: A function that tests each element of the iterable. It should return True or False.
        iterable: The iterable to be filtered.
'''

my_numbers = [1, 2, 3, 4, 5]

def is_even_func(x):
    return x % 2 == 0


result_func = list(filter(is_even_func, my_numbers))

result_lambda = list(filter(lambda x: x % 2 == 0, my_numbers))


print(f"Function result: {result_func}")
print(f"Lambda result: {result_lambda}")


# 1. Using filter() with a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers:", list(even_numbers))  # Output: [2, 4, 6, 8]

# 2. Using filter() with a Tuple
words = ("apple", "banana", "cherry", "date", "fig")
long_words = filter(lambda word: len(word) >= 5, words)
print("Long words:", tuple(long_words))  # Output: ('apple', 'banana', 'cherry')

# 3. Using filter() with a String
text = "hello world"
vowels = "aeiou"
filtered_text = filter(lambda char: char not in vowels, text)
print("Filtered text:", ''.join(filtered_text))  # Output: "hll wrld"

# 4. Using filter() with a Set
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8}
small_numbers = filter(lambda x: x <= 5, numbers_set)
print("Small numbers:", set(small_numbers))  # Output: {1, 2, 3, 4, 5}

# 5. Using filter() with a Dictionary
my_dict = {'a': 5, 'b': 15, 'c': 10, 'd': 7}
filtered_items = filter(lambda item: item[1] >= 10, my_dict.items())
print("Filtered items:", dict(filtered_items))  # Output: {'b': 15, 'c': 10}

# 6. Using filter() with Multiple Conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = filter(lambda x: x % 2 == 0 and x > 4, numbers)
print("Filtered numbers:", list(filtered_numbers))  # Output: [6, 8]
