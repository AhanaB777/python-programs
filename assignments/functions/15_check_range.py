"""15. Write a Python function to check whether a number falls in a given range."""
def checkRange(l,u,n):
    if l>u:
        print("Enter proper range")
    elif l<=n and n<=u:
        print("Number falls in given range")
    else:
        print("Number is out of range")
l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
n=int(input("Enter num: "))
checkRange(l,u,n)