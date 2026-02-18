""" 11. Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y 
"""

d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}

for k in d1:
    if k in d2 and d1[k] == d2[k]:
        print(k, ":", d1[k], "is present in both x and y")