"""
    Two numbers are entered through the keyboard. Write a program to find the value of one number
    raised to the power of another.
"""
#input base
x=int(input("Enter value of base: "))

#input power
y=int(input("Enter value of power: "))

#initialize value of result
result=1

#calculate base^power
while y!=0 :
    result*=x
    y-=1

#print result
print(f"The result is : {result}")