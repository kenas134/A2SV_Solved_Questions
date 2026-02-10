import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = float('inf')

    for i in range(n):
        cntA = cntB = cntC = 0
        
     
        for length in range(1, 8):
            if i + length > n:
                break

            ch = s[i + length - 1]
            if ch == 'a':
                cntA += 1
            elif ch == 'b':
                cntB += 1
            else:
                cntC += 1

            if length >= 2:
                if cntA > cntB and cntA > cntC:
                    ans = min(ans, length)

    print(ans if ans != float('inf') else -1)
