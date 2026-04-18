def average(array):
    # your code goes here
    s=set(array)
    total=sum(s)
    a=total/len(s)
    return a
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)