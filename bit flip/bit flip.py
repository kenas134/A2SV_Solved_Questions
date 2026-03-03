import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    prefix = 0
    balanced = [False] * n

    for i in range(n):
        if a[i] == '1':
            prefix += 1
        else:
            prefix -= 1
        if prefix == 0:
            balanced[i] = True

    flip = 0
    possible = True

    for i in range(n - 1, -1, -1):
        current = a[i]
        if flip % 2 == 1:
            current = '1' if current == '0' else '0'

        if current != b[i]:
            if not balanced[i]:
                possible = False
                break
            flip ^= 1

    print("YES" if possible else "NO")
