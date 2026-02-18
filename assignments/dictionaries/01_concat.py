""" concat two dictionaries """

dic1={1:10,2:10}
dic2={3:30,4:40}
dic3={5:50,6:60}

#method 1
res1=dic1|dic2|dic3

#method2
res2={}
res2.update(dic1)
res2.update(dic2)
res2.update(dic3)

print(res1)
print(res2)