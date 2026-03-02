

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    cur = s[:k].count("W")
    minn = cur
    for i in range(k,n):
        cur -= (s[i-k] == "W")
        cur += (s[i] == "W")
        minn = min(cur,minn)
    print(minn)
