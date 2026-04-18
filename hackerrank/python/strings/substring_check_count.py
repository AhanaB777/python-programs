"""In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left."""
s1="abcdcdc"
s2="cdc"
count=0
# for i in range(len(s1)):
#     if s1[i]==s2[i]:
#         i+=1
#         continue
#     i+=1
for i in range(len(s1)):
    if s1[i:i+len(s2)]==s2:
        count+=1
print(count)
