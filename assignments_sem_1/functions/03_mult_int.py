"""3. Create a function to multiply two numbers and the numbers should pass as parameter and
return the result."""
def mult(a,b):
    res=a*b
    return res
int1=int(input("Enter first num: "))
int2=int(input("Enter second num: "))
result=mult(int1,int2)
print(f"Result: {result}")