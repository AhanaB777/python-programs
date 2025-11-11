"""
    When interest compounds q times per year at an annual rate of r % for n years, the principle p
    compounds to an amount a as per the following formula. Write a program to read 10 sets of p, r,
    n & q and calculate the corresponding as.
    a = p(1 + r/q)^(np)
"""
num = 1
while num <=10 :
    print(f"Taking values of p,r,n & q for set number {num}")
    p=float(input("Enter value of principle p: "))
    r = float(input("Enter annual rate r: "))
    n = int(input("Enter years n: "))
    q = int(input("Enter compounding times per year q: "))

    base = 1+(r/q)

    exponent = n * q
    power = 1
    i = 1

    while i <= exponent:
        power = power * base
        i += 1

    # Step 3: final amount
    a = p * power

    print("Amount =", a)
    print()

    num+=1