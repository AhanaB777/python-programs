"""20. Write a Python function to check whether a number is perfect or not."""

def isPerfect(n):
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s += i

    if s == n:
        print(n, "is Perfect Number")
    else:
        print(n, "is NOT Perfect Number")

# Test
isPerfect(6)
isPerfect(10)
