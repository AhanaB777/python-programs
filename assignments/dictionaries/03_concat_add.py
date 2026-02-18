"""Concat and add"""

dic1={1:10,2:20,4:6}
dic2={3:30,4:40,5:2}
dic3={5:50,6:60}
d4=dic1
d5=dic2|dic3

for i in d5.keys():
    if i in d4.keys():
        d4[i]+=d5[i]
    else:
        d4[i]=d5[i]
print(d4) 