"""8. Create a function to calculate and return HCF of two numbers."""
def hcf(a,b):
    if a>b:
        a,b=b,a
    while(b):
            a,b=b,a%b
    return a

a=30
b=9
res=hcf(a,b)
print(res)