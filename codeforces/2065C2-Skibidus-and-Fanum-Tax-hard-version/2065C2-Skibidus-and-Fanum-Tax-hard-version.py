from bisect import bisect_left


t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    lst = sorted(map(int,input().split()))
    prev = min(arr[0],lst[0]-arr[0])
    for i in range(1,n):
        idx = bisect_left(lst,prev+arr[i])
        if idx == m and arr[i] < prev:
            print("NO")
            break
        elif idx == m:
            prev = arr[i]
        else:
            if arr[i] >= prev:
                prev = min(lst[idx]-arr[i],arr[i])
            else:
                prev = lst[idx]-arr[i]
    else:
        print("YES")