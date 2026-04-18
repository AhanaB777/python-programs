""" function to check whether a number falls in a given range """
def check_num(l,h,n):
    if n>=l and n<=h:
        print("Number is in range")
    else:
        print("Number out of range")

low=int(input("Enter lower range: "))
high=int(input("Enter higher range: "))
num=int(input("Enter number: "))
check_num(low,high,num)

