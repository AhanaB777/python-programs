def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1) 

def reverse(m):
    num=m
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
    