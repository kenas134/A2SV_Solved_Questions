
n = int(input())
arr = sorted(map(int,input().split()))
k = 1
for i in range(n):
    if arr[i] >= k:
        k += 1
print(k-1)
