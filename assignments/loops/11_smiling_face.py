"""
    Write a program to fill the entire screen with a smiling face. (The smiling face has an ASCII value
    1)
"""
smile = chr(1)

while True:
    for i in range(100):
        print(smile, end="")
    print()
