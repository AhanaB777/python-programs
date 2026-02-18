"""Check whether key already exists """

d={1: 10, 2: 10, 3: 30, 4: 40, 5: 50, 6: 60}
key=int(input("Enter key: "))
l=list(d.keys())
k=[]
if key in l:
    print("Key exists")
else:
    print("key doesnt exists")
        