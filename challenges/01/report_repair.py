from itertools import permutations
import functools


def find_entries(values, perm_length):
    perms = set(permutations(values, perm_length))
    filtered_by_criteria = [perm for perm in perms if functools.reduce(lambda a, b: a + b, perm) == 2020]
    pair = filtered_by_criteria[0]

    return functools.reduce(lambda a, b: a * b, pair)


with open('inputs.txt', 'r') as file:
    lines = list(file)
    inputs = [int(numeric_string) for numeric_string in lines]

    print(find_entries(inputs, 2))
    print(find_entries(inputs, 3))
