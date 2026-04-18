"""7. Write a Python program to understand the use of double asterisk(*) character declared in a
function."""

def display(**data):
    for key in data:
        print(key, ":", data[key])

display(name="Ahana", age=21, course="MCA")
