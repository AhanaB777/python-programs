"""18. Write a Python function that takes a number as a parameter and check the number is prime
or not."""
def checkPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("The number is Not Prime")
            break
        else:
            print("The number is Prime")


n=int(input("Enter number: "))
checkPrime(n)
