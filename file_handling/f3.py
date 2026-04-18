f=open("example.txt","r")
# data=f.read()
# unique_cap=set()
# for i in data:
#     if i.isupper() :
#         unique_cap.add(i)
    
# print("Number of capital letters: ",len(unique_cap))
count=1
for line in f:
    print(count, line.strip())
    count+=1
f.close()