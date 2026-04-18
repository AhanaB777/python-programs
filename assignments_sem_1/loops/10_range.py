"""
    Write a program to find the range of a set of numbers. Range is the difference between the
    smallest and biggest number in the list.
"""
# Program to find the range of a set of numbers

# take input size
n = int(input("How many numbers? "))

numbers = []

# read numbers
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

# initialize smallest and biggest
smallest = numbers[0]
biggest = numbers[0]

# find smallest and biggest using loop
for x in numbers:
    if x < smallest:
        smallest = x
    if x > biggest:
        biggest = x

# calculate range
range_value = biggest - smallest

print("Smallest number =", smallest)
print("Biggest number =", biggest)
print("Range =", range_value)


