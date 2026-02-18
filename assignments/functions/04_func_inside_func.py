"""4. Write a Python program to access a function inside a function."""

def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")

    inner()   # calling inner inside outer

outer()
