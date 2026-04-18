"""8. Create a function to calculate and return LCM of two numbers."""

def lcm(a, b):
    max_num = a if a > b else b

    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

# Driver code
x = 12
y = 18
print("LCM =", lcm(x, y)) # 36
