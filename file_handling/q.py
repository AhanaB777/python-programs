""" Create a input file with name input.txt 
        content: around 20 lines of numbers

    WAP in python to :
    - take input from the input file, 
    - count number of elements, 
    - calculate sum of elements
    - create a list of all the elements
    - count and sum 

    write everything in output.txt
    content of output.txt:
        20 iput items and sum= {sum of 20 elements}
        [list of all elements]
        {count: number of elemnts, sum: sum of elements}

"""
import json
with open("D:\example.txt","r") as file:
    count=0
    s=0
    l=[]
    d={}
    for i in file:
        count+=1
        s+=int(i)
        l.append(int(i))
    d["count"]=count
    d["sum"]=s
print("Number of elements: ",count)
print("Sum: ",s)
print("List: ",l)
print(d)

f2=open("file_handling\output.txt","w")

count=str(count)
s=str(s)

f2.write(f"Number of elements = {count}\n")
f2.write(f"Sum = {s}\n")

json.dump(l,f2)
f2.write("\n")
json.dump(d,f2)
file.close()
f2.close()