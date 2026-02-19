
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = [(list(map(int,input().split()))) for i in range(n)]
    arr.sort()
    for l,r,m in arr:
        if k >= l and m > k:
            k = m
    print(k)
        
    
