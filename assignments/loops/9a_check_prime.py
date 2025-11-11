n=int(input("Enter a number: "))
div=2
while div<=n//2 :
    if n%div == 0 :
        print(f"{n}is not a prime number")
        break
    else :
        div+=1
        continue
else :
    print(f"{n} is a prime number")