"""
    check whether the inpt number is armstrong or not.
"""
#input number
n=int(input("enter number: "))

#initialize required variables
sum=0
temp=n

#calculate sum
while n!=0 :
    rem=n%10
    sum+=rem*rem*rem
    n=n//10

#check for armstrong and print result
if sum==temp :
    print(f"Yes {temp} is an armstrong number.")
else: 
    print(f"No {temp} is not an armstrong number.")

