

from collections import Counter


n,k = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0
left = 0
count = 0
for i in range(n):
    ans += arr[i]
    while ans>=k:
        count+=n-i
        ans -= arr[left]
        left += 1
    
print(count)
    
