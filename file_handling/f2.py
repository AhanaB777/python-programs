
with open("example.txt","w") as f:
    f.write("Welcome to the best college of the Universe!")

file=open("example.txt","r")
data=file.read()
l=data.lower().split()
print(l)
count=0
for i in l:
    if i == "to" or i=="the" :
        count+=1
print(count)
file.close()
