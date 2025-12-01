"""
4. “Longest Increasing-Digit-Sum Substring (Contiguous)”

Problem: Given a string consisting of positive-integer numbers separated by spaces (for example: "12 3
45 9 10 2 100"), treat each number as an integer, compute the digit-sum of each number, then find
the longest contiguous subsequence (sub-string-of-numbers) where each number's digit-sum is strictly
greater than the previous number's digit-sum. Print the subsequence (as original numbers) and its length.

"""
s=input("Enter number separated by spaces: ").split()
num_list=[]
for i in s:
    num_list.append(i)
print("Original numbers: ",num_list)

d_sum=[]
for i in num_list:
    s=0
    for d in i:
        s+=int(d)
    d_sum.append(s)
print("Digit sums: ",d_sum)

max_len = 1
max_start = 0

current_len = 1
current_start = 0

for i in range(1, len(d_sum)):
    if d_sum[i] > d_sum[i-1]:
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
            max_start = current_start
        current_len = 1
        current_start = i
if current_len > max_len:
    max_len = current_len
    max_start = current_start

ls= num_list[max_start:max_start+max_len]

print("Longest increasing-digit-sum subsequence:", ls)
print("Length of subsequence:", max_len)