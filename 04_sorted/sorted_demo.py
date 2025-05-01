'''
The sorted() function returns a new list containing all items from the iterable in ascending order. It can accept any iterable, such as lists, tuples, and dictionaries, and it returns a sorted list.

    Syntax: sorted(iterable, *, key=None, reverse=False)

    Parameters:
        iterable: The collection you want to sort.
        key (optional): A function that serves as a key for the sort comparison. This is often a lambda function.
        reverse (optional): A boolean. If True, the list is sorted in descending order.
'''

values = [(1, 'b', 'Square'), (2, 'a', 'Spongebob'), (3, 'c', 'pants')]

def sort_func(x):
    return x[1]

result_func = sorted(values, key=sort_func)

result_lambda = sorted(values, key=lambda x: x[1])


print(f"Function result: {result_func}")
print(f"Lambda result: {result_lambda}")


print(f"{result_lambda[0][2]} {result_lambda[1][2]}{result_lambda[2][2]}")


data = [(1, 2), (3, 1), (5, 4)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)





# Sorting with a key
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['apple', 'cherry', 'banana']


# 1. Using sorted() with a List
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print("Sorted numbers (descending):", sorted_numbers)  # Output: [9, 6, 5, 5, 2, 1]

# 2. Using sorted() with a Tuple
words = ("banana", "apple", "cherry", "date")
sorted_words = sorted(words, key=lambda word: len(word))
print("Sorted words by length:", sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

# 3. Using sorted() with a String
text = "hello"
sorted_chars = sorted(text)
print("Sorted characters:", ''.join(sorted_chars))  # Output: "ehllo"

# 4. Using sorted() with a Set
numbers_set = {5, 3, 9, 1, 4}
sorted_set = sorted(numbers_set)
print("Sorted set:", sorted_set)  # Output: [1, 3, 4, 5, 9]

# 5. Using sorted() with a Dictionary
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_items = sorted(my_dict.items(), key=lambda item: item[1])
print("Sorted dictionary items by value:", sorted_items)  # Output: [('b', 1), ('c', 2), ('a', 3)]

# 6. Using sorted() with Multiple Criteria
data = [(1, 3), (1, 2), (2, 1), (2, 3)]
sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
print("Sorted data by multiple criteria:", sorted_data)  # Output: [(1, 2), (1, 3), (2, 1), (2, 3)]
