"""
    multiplication table
"""
n=int(input("Enter the number: "))
i=1
while i<=10:
    mult=n*i
    print(f"{n} * {i} = {mult}")
    i+=1