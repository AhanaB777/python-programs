"""C. Write a program that create a dictionary with the frequency of the 
vowels from an inputted string. For example: input:'institute'. 
Output:{'i':2,'u':1,'e':1}"""

s="institute"
vowels="aeiouAEIOU"
new_s=""
for i in s:
    if i in vowels :
        new_s+=i
d={}
for i in new_s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)