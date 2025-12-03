""" Calculating GCD using recursion """
def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a==b:
        return 1
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)
a=int(input("Enter first numero: "))
b=int(input("Enter second numero: "))
result=gcd(a,b)
print(f"GCD of {a} and {b} is {result}")