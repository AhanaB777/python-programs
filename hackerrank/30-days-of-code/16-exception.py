S = input("Enter a string: ")
try:
    int(S)
    print(S)         
except ValueError:
    print("Bad String")