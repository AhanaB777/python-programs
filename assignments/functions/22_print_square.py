"""22. Write a Python function to create and print a list where the values are square of numbers
between 1 and 30 (both included)"""
def printSquare():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    for i in l:
        print(i,end=" ")
printSquare()