"""
    Write a program to print all prime numbers from 1 to 300. (Hint: Use nested loops, break and
    continue)
"""
num=1
while num<=300 :
    if num == 1:
        num+=1
        continue
    temp = num
    div = 2
    while div<=temp//2 :
        if temp%div == 0 :
            break
        else:
            div+=1
            continue
    else:
        print(num)
    num+=1
