

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = []

    if n == 2:
        print(n)
        print(*arr)
        continue

    ans.append(arr[0])

    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1] or  arr[i-1] > arr[i] < arr[i+1]:
            ans.append(arr[i])
    ans.append(arr[-1])
    print(len(ans))
    print(*ans)
