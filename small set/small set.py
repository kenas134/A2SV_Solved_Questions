from collections import Counter


n,k = map(int,input().split())
arr = list(map(int,input().split()))

sett = Counter()
left = 0
count = 0
for i in range(n):
    sett[arr[i]] += 1
    while left < n and len(sett) > k:
        sett[arr[left]] -= 1
        if sett[arr[left]] == 0:
            del sett[arr[left]]
        left += 1
    count += i-left+1

print(count)
    
