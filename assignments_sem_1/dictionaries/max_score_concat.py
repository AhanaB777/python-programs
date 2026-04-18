""" Program to concat two dictionaries and if two keys are same then take the value that is maximum """

m1 = {'pl1': 20, 'pl2': 30, 'pl3': 50}
m2 = {'pl3': 10, 'pl5': 50, 'pl1': 30}

result = {}

# Copy m1 first
for k in m1:
    result[k] = m1[k]

# Merge m2
for k in m2:
    if k in result:
        if m2[k] > result[k]:
            result[k] = m2[k]
    else:
        result[k] = m2[k]

print(result)

