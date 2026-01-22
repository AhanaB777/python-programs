"""
4. “Longest Increasing-Digit-Sum Substring (Contiguous)”

Problem: Given a string consisting of positive-integer numbers separated by spaces (for example: "12 3
45 9 10 2 100"), treat each number as an integer, compute the digit-sum of each number, then find
the longest contiguous subsequence (sub-string-of-numbers) where each number's digit-sum is strictly
greater than the previous number's digit-sum. Print the subsequence (as original numbers) and its length.

"""
s=input("Enter number separated by spaces: ").split()
num=[]
for i in s:
    num.append(i)
print("Original numbers: ",num)

ds=[]
for i in num:
    s=0
    for d in i:
        s+=int(d)
    ds.append(s)
print("Digit sums: ",ds)

max_len = 1
max_start = 0

cur_len = 1
cur_start = 0

for i in range(1, len(ds)):
    if ds[i] > ds[i-1]:
        cur_len += 1
    else:
        if cur_len > max_len:
            max_len = cur_len
            max_start = cur_start
        cur_len = 1
        cur_start = i
if cur_len > max_len:
    max_len = cur_len
    max_start = cur_start

ls= num[max_start:max_start+max_len]

print("Longest increasing-digit-sum subsequence:", ls)
print("Length of subsequence:", max_len)