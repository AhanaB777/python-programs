"""
    Write a program to enter the numbers till the user wants and at the end it should display the count
    of positive, negative and zeros entered.
"""
#initializing count variables
p_count = 0
n_count = 0
z_count = 0

#taking user input and counting
while True :
    #taking user input
    inp = input("Enter a number (enter 'stop' to stop): ")
    
    #if stop encountered then directly print result
    if inp == 'stop':
        break

    #otherwise convert to numbers
    n=int(inp)

    #check and count
    if n==0 :
        z_count+=1
    elif n>0 :
        p_count+=1
    else :
        n_count+=1

#print results
print(f"positve numbers = {p_count}")
print(f"negative numbers = {n_count}")
print(f"zeros = {z_count}")