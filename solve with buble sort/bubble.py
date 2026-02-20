t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    
    ans = []
    for i in range(n):
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ans.append([1,j+1])
    
    for i in range(n):
        
        for j in range(0, n - i - 1):
            if brr[j] > brr[j + 1]:
                brr[j], brr[j + 1] = brr[j + 1], brr[j]
                ans.append([2,j+1])
    for i in range(n):
        if arr[i] > brr[i]:
            ans.append([3,i+1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
    
