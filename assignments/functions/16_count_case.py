"""16. Write a Python function that accepts a string and calculate the number of upper case letters
and lower case letters."""
def countCase(s):
    count_cap=0
    count_small=0
    for i in s:
        if i.isupper():
            count_cap+=1
        else:
            count_small+=1
    return count_cap,count_small

s="HelloWorlD"
cap,small=countCase(s)
print(f"Uppercase: {cap}\nLowercase: {small}")