# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d={}
for i in range(0,n):
    a=0
    s=input().split()
    d[s[a]]=s[a+1]
while True:
    try:
        q=input()
        if q in d:
            print(f"{q}={d[q]}")
        else:
            print("Not found")
    except EOFError:
        break