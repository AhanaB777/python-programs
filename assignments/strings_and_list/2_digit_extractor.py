"""
2. “Digit-Extractor and Digit-Stats from Mixed String”

Problem: Given a string that may contain letters, digits, punctuation, spaces etc., extract all digit
characters, treat them as numbers (single digits), then compute and output: (1) their sum, (2) their average
(as float), (3) their maximum digit, (4) their minimum digit. If no digits — print an appropriate message.

"""
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
