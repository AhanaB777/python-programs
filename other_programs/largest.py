#PROGRAM TO FIND THE LARGEST NUMBER AMONG THREE NUMBERS

#take input
a,b,c=map(int,input("Enter three numbers: ").split())

#using conditional operator
if a>b and a>c :
    largest = a
elif a>b and c>a :
    largest = c
elif b>a and b>c :
    largest = b
elif b>a and c>b :
    largest = c
else :
    largest = 0 

#print result
print(f"Largest number is {largest}")



