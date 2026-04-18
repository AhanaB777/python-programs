"""5. Write a Python program to understand the use of global and nonlocal variables declared
in a function."""

x = 10   # Global variable

def outer():
    y = 20   # Enclosing variable

    def inner():
        global x
        nonlocal y

        x = x + 5
        y = y + 5

        print("Inside inner → x:", x, " y:", y) # x=15 , y=25

    inner()
    print("Inside outer → y:", y) # y=25

outer()
print("Outside → x:", x) # x=15
