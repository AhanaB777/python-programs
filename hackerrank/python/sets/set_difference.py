""" Goal : Print the symmetric difference of two sets in ascending order """

m=int(input("Number of elements of set a: "))
a=input("Enter space separated elements: ").split()
lis_a=list(map(int,a))
set_a=set(lis_a)

n=int(input("Number of elements of set b: "))
b=input("Enter space separated elements: ").split()
lis_b=list(map(int,b))
set_b=set(lis_b)

res=set_a.symmetric_difference(set_b)
res_list=list(res) 
res_list.sort()
print("Symmetric difference of set a and set b: ")
for i in res_list:
    print(i)