a=5
for i in range(1,a+1):
    for j in range(i):
        print(i, end=" ")
    print()

for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end=" ")
    for k in range(i):
        print(i,end=" ")
    print()

for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(i,end=" ")
    print()

for i in range(a,0,-1):
    for j in range(i):
        print(i,end = ' ')
    print()

for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end="")
    for k in range(i):
        print(i,end=" ")
    print()

for i in range(a,0,-1):
    for j in range(a-i):
        print(" ",end =" ")
    for k in range(i):
        print(i,end=" ")
    print()

for i in range(a+1):
    ch=chr(64+i)
    for j in range(i):
        print(ch, end=" ")
    print()