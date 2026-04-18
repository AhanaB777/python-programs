def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n
n=4
res=fact(n)
print(f"fact of {n} is {res}")
