""" Function to accept a string and count the number of upper and lower case letters """
def count_case(s):
    count_lower=0
    count_upper=0
    for i in s:
        if i.isupper():
            count_upper+=1
        else:
            count_lower+=1
    return count_lower,count_upper
        

st=input("Enter a string: ")
a,b=count_case(st)
print(f"Number of lowercase letters {a}\nNumber of uppercase letters {b}")