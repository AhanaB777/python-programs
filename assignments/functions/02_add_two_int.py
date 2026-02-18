"""2. Write a program to add two integers using function."""
def add(a,b):
    s=a+b
    return s
int1=int(input("Enter first num: "))
int2=int(input("Enter second num: "))
result=add(int1,int2)
print(f"Result: {result}")