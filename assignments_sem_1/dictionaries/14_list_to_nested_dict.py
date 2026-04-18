"""
14. Write a Python program to convert more than one list to a nested dictionary.
Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim
Richards': 92}}]
"""

ids   = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
marks = [85, 98, 89, 92]

nested = []

for i in range(len(ids)):
    d = {ids[i]: {names[i]: marks[i]}}
    nested.append(d)

print("Nested dictionary:")
print(nested)