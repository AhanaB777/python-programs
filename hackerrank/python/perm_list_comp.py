"""given four integers: x, y, z, n.
You must:
Generate all possible lists [i, j, k]
Where:
i ranges from 0 to x
j ranges from 0 to y
k ranges from 0 to z
Exclude the lists where i + j + k == n
Using list comprehension"""
if __name__ == '__main__':
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    z = int(input("Enter value of z: "))
    n = int(input("Enter value of n: "))
    a=[x,y,z]
    l=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
    print(l)