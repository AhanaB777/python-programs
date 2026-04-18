"""
    Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each
    digit of the number is equal to the number itself, then the number is called an Armstrong number.
    For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )
"""
#initialize required variables

i=1
#check for arm 
while i<=500:
    temp = i
    cubes_sum = 0
    while temp>0 :
        rem=temp%10
        cubes_sum += rem * rem * rem
        temp//=10
    if cubes_sum == i :
        print(i)
        
    i+=1