

from collections import Counter


t = int(input())
for _ in range(t):
    n,l,r = map(int,input().split())
    arr = list(map(int,input().split()))
    left = arr[:l]
    right = arr[l:]
    left.sort()
    right.sort()
    Nl = []

    Nr = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] == right[j]:
            i += 1
            j += 1
        elif left[i] > right[j]:
            Nr.append(right[j])
            j += 1
        else:
            Nl.append(left[i])
            i += 1

    Nr.extend(right[j:])
    Nl.extend(left[i:])



    

    if len(Nl) < len(Nr):
        Nl, Nr = Nr, Nl

    
    l_rem = len(Nl)
    r_rem = len(Nr)
    
    diff = l_rem - r_rem
    count = 0
    

    i = 0
    Nl.sort()
    
    while i + 1 < len(Nl) and diff > 0:
        if Nl[i] == Nl[i + 1]:
            count += 1
            diff -= 2
            i += 2
        else:
            i += 1
    
    count += diff

    remaining = (l_rem + r_rem - (l_rem - r_rem)) // 2
    count += remaining
    
    print(count)
