"""
    If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine
    the youngest of the three. 
"""
age_ram=int(input("Enter age of Ram: "))
age_shyam=int(input("Enter age of Shyam: "))
age_ajay=int(input("Enter age of Ajay: "))

if age_ram<age_shyam and age_ram<age_ajay:
    print("Ram is the youngest")
elif age_shyam<age_ram and age_shyam<age_ajay:
    print("Shyam is the youngest")
elif age_ajay<age_shyam and age_ajay<age_ram:
    print("Ajay is the youngest")
else:
    print("Nobody is youngest among the three as two or more people have the same age!")