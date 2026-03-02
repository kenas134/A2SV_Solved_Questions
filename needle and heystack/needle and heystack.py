

from collections import Counter

n = int(input())
for _ in range(n):
    t = input()
    s = input()

    tt = Counter(t)    
    ss = Counter(s)
    x = False
    for j in tt:
        if tt[j] > ss[j]:
            x = True
            break
    if x:
        print("Impossible")
        continue
    left = []
    for j in ss:
        left.append(j*(ss[j]-tt[j]))

    ans = []
    left.sort()
    j = 0
    i = 0
    while i < len(left) and j < len(t):
        if left[i] < t[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(t[j])
            j += 1

    ans.extend(left[i:])
    ans.append(t[j:])
    print("".join(ans))



