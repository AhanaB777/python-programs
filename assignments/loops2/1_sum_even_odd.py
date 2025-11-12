"""
 “Sum Even and Odd Separately”
● Problem statement: Given a list of integers, compute two sums: one for all even
numbers, and one for all odd numbers. Then print both sums.
● Input: First integer n, then n integers.
● Output: Two integers: sum_of_evens, sum_of_odds.
"""
n=int(input("Enter number of terms: "))
count=1
even_sum=0
odd_sum=0
while count<=n :
    value=int(input("Enter a number: "))
    
    if value%2== 0 :
        even_sum+=value
    else :
        odd_sum+=value    

    count+=1
print(f"Sum of even terms is {even_sum}")
print(f"Sum of  odd terms is {odd_sum}")