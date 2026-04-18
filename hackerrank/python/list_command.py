# s="insert 0 5"
# l=s.split()
# r=[]
# i=int(l[1])
# e=int(l[2])
# r.insert(i,e)
# print(r)

n=int(input("enter no. of comamnds: "))
l=[]
for i in range(0,n):
    s=input().split()
    if s[0] == "insert" :
        # i=int(s[1])
        # e=int(s[2])
        l.insert(int(s[1]),int(s[2]))

    if s[0] == "print" :
        print(l)

    if s[0] == "remove":
        l.remove(int(s[1]))

    if s[0] == "append" :
        l.append(int(s[1]))
    
    if s[0] == "sort" :
        l.sort()

    if s[0] == "pop":
        l.pop()

    if s[0] == "reverse" :
        l.reverse()

    