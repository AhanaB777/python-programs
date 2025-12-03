""" Factorial of a number using recursion """
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a num: "))
res=fact(n)
print(f"Factorial of {n} is {res}")    
