"""14. Write a Python function to calculate the factorial of a number (a non-negative integer). The
function accepts the number as an argument."""
def fact(n):
    if n<0:
        return 0
    if n==0:
        return 1
    else:
        f=1
        for i in range(n,0,-1):
            f=f*i
        return f

n=int(input("Enter value of n: "))
res=fact(n)
print(f"Factorial of {n} is {res}")