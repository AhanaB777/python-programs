f1=open("D:\learn.txt","r")
txt=f1.read()
# print(txt)

for i in range(0,5):
    txt1=f1.readline()

print(txt1)

f2=open("file_handling\output.txt","w")
f2.write(txt)

with open("D:\learn.txt","r") as f3:
    for t in f3:
        print(t)
        
f1.close()
f2.close()
f3.close()