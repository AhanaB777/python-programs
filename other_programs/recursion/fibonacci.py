""" nth term of fibonacci series using recursion """
def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
n=int(input("Enter value of n: "))
res=fibo(n)
print(f"{n}th term of fibonacci series is {res}")