"""10. Write a Python program to get the top three items in terms of cost in a shop.
d1={'dress':23,'pant':45,'shoe':12,'bungle':55,'book':8}
output:
bungle 55
pant 45
dress 23
"""
d1 = {'dress':23, 'pant':45, 'shoe':12, 'bungle':55, 'book':8}

# Convert dictionary → list of items
items = list(d1.items())

# Manual sorting (Descending based on cost)
for i in range(len(items)):
    for j in range(i+1, len(items)):
        if items[i][1] < items[j][1]:
            # swap
            temp = items[i]
            items[i] = items[j]
            items[j] = temp

# Print top 3
for i in range(3):
    print(items[i][0], items[i][1])
