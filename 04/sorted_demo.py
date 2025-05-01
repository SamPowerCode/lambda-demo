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