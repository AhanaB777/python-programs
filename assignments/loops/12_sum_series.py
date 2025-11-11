"""
    Write a program to add first seven terms of the following series using a for loop: 1/1! + 2/2! +
    3/3! + ... n/n!
"""
sum_series = 0
fact = 1      

for i in range(1, 8):  
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j

    term = i / fact
    sum_series = sum_series + term

print("Sum of the series =", sum_series)