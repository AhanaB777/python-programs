"""
Alternating Sequence Filter
● Problem statement: Write a program to read a sequence of integers until the end (or
given length). 
Then produce a new list by selecting numbers according to this rule: 
- you begin expecting an even number; when you encounter an even number you accept it,
- then switch expectation to odd; when you next encounter an odd number you accept it,
- switch expectation to even, and so on. If a number does not meet the current
    expectation you skip it and keep going. At the end print the accepted list.
● Input: A list of integers.
● Output: A list of integers (the accepted ones) printed in their original order.
"""
n = int(input("Enter number of terms: "))
count=0
result=""
while count<n :
    val = int(input("Enter a number: "))
    
    if count%2==0 and val%2==0:
        result=result+" "+str(val)

    elif count%2!=0 and val%2!=0:
        result=result+" "+str(val)  
    else:
        count+=1
        continue
    count+=1  
print(result)  