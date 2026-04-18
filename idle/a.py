s=input("Enter a string: ")
digit=""
for ch in s:
    if ch.isdigit():
        digit+=ch+" "
list_digit=digit.split()

num_list=[]
for i in range(0,len(list_digit)):
    num_list.append(int(list_digit[i]))

#print(num_list)

if len(num_list)==0:
    print("Digits are not present")
else: 
    sum=0
    for i in num_list:
        sum+=i
    print(f"Sum of digits: {sum}")
    
    average=sum/len(num_list)
    print(f"Average of digits: {average}")

    max_digit=-1
    for i in num_list :
        if i>max_digit:
            max_digit=i
    print(f"Maximum digit: {max_digit}")

    min_digit=num_list[0]
    for i in num_list:
        if i<min_digit:
            min_digit=i
    print(f"Minimum digit: {min_digit}")
