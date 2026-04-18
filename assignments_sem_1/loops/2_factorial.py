"""
    Write a program to find the factorial value of any number entered through the keyboard.
"""
#Taking user input
n = int(input("Enter number to calculate factorial : "))

#initializing factorial value as 1
fact=1

#calculating factorial
while n!=0 :
    fact*=n
    n-=1

#printing result
print(f"The factorial is {fact}")
