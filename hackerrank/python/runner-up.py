if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    m=next(arr)
    sm=None
    for i in arr:
        if i>m:
            sm=m
            m=i
        elif i!=m and (sm is None or i>sm):
            sm=i
    print(sm)