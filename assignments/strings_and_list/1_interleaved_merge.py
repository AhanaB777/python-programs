"""
1. “Interleaved Merge with Reversed Half”

Problem: Given two strings s1 and s2, build a new string by taking characters alternately: first character
of s1, then last character of s2, then second character of s1, then second-last of s2, and so on. If one
string is longer, append the leftover characters at the end (in their original order if from s1, or reversed
order if from s2).

input: abcde, abcdef
output: afbecddceba 
"""
s1=input("Enter first string: ")
s2=input("Enter second string: ")
s3=""

rev_s2=s2[::-1]

i=0
j=0
while i<len(s1) and j<len(s2) :
    s3+=s1[i]+rev_s2[j]
    i+=1
    j+=1
if i<len(s1):
    s3+=s1[i:]
if j<len(s2):
    s3+=rev_s2[j:]
print(s3)

