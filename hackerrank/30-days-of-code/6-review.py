# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(0,t):
    a=input()
    for i in range(0,len(a)):
        if i%2==0:
            print(a[i],end="")
    print(" ",end="")
    for i in range(0,len(a)):
        if i%2!=0:
            print(a[i],end="")
    print('\n',end="")
