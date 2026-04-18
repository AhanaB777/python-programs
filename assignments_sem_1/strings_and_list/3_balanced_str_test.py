"""
3. “Balanced-String Test (All chars present)”

Problem: Given two strings a and b, test whether a is “balanced” in b: i.e. whether all characters in a
appear somewhere in b. Then print True or False. Optionally, also print which characters of a are
missing in b.

"""
a=input("Enter first string: ")
b=input("Enter second string: ")

c=""
for i in a :
    if i in b:
        found=True
    else:
        found=False
        c+=i
if found:
    print("True")
else:
    print("False")

if len(c)==0:
    print("No characters of a is missing in b")
else:
    print(f"Characters of a missing in b: {c}")