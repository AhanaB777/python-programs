"""
Q1. Consecutive Prime Sum 
    Some prime numbers can be expressed as a sum of other consecutive prime numbers. 
    For example 5 = 2 + 3, 17 = 2 + 3 + 5 + 7, 41 = 2 + 3 + 5 + 7 + 11 + 13. Your task is to 
    find out how many prime numbers which satisfy this property are present in the range 3 
    to N subject to a constraint that summation should always start with number 2. 

    Write code to find out the number of prime numbers that satisfy the above-mentioned 
    property in a given range. 

    Input Format: First line contains a number N 
    Output Format: Print the total number of all such prime numbers which are less than or 
        equal to N. 
    Constraints: 2<N<=12,000,000,000

"""
n=int(input("Enter value of n: "))
l=[]
for i in range(2,n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        l.append(i)
            
print(l)

# l=[2,3,5,7,11,13,17,19,23]

a=[]
for i in range(2,len(l)):
    var=0
    for j in range(0,i):
        var+=l[j]
        if var==l[i]:
            a.append(l[i])
            break
print(a)
print(len(a))