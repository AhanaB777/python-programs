n=10
count=0
max_count=0
while n!=0:
    rem=n%2
    if rem==1:
        count+=1
        if count>max_count:
            max_count=count
    else: 
        count=0
    n//=2
print(max_count)