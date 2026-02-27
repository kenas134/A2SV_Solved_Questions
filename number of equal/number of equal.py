from collections import Counter
n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
i = 0 
j = 0
cur = 0
for j in range(len(b)):
    if j > 0 and b[j] == b[j-1]:
        count += cur
        j += 1
    else:
        cur = 0
        while i < len(a) and a[i] <= b[j]:
            if b[j] == a[i]:
                cur += 1
            i += 1
        count += cur
        j += 1
print(count)
