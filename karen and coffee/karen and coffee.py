

import sys
input = sys.stdin.readline

MAXT = 200000

n, k, q = map(int, input().split())

temp = [0] * (MAXT + 2)
for i in range(n):
    l,r = map(int, input().split())
    temp[l] += 1
    temp[r+1] -= 1
for i in range(1,len(temp)):
    temp[i] = temp[i] + temp[i-1]

ans = [0]*(MAXT + 1)

for i in range(1,len(ans)):
    if temp[i] >= k:
        ans[i] = ans[i-1] + 1
    else:
        ans[i] = ans[i-1]


for i in range(q):
    l,r = map(int,input().split())
    print(ans[r]-ans[l-1])

 
