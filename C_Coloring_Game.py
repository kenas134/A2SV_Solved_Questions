
import sys
input = sys.stdin.readline
from bisect import bisect_left


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    ans = 0

    for i in range(n-1,1,-1):
        for j in range(i-1,0,-1):
            num1 = arr[i]
            num2 = arr[j]
            num3 = max(arr[-1]-num1-num2+1,num1-num2+1)
            k = bisect_left(arr,num3)

            if k < j:
                ans += j-k
    print(ans)
