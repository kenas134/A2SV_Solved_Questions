import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    g = [input().strip() for _ in range(n)]
    
    p = list(range(n))
    
    def cmp(x, y):
        if g[x][y] == '1':
            return x - y
        else:
            return y - x
    
    # Python doesn't support cmp directly in sort, so use functools
    from functools import cmp_to_key
    p.sort(key=cmp_to_key(cmp))
    
    print(*[x + 1 for x in p])

t = int(input())
for _ in range(t):
    solve()