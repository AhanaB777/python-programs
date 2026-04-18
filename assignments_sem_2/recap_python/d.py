"""D. Write a program to calculate sum of the following series: 1+2+3+...+n """
n=int(input("Value of n: "))
s=0
for i in range(1,n+1):
    s+=i
print("Sum of series: ",s)