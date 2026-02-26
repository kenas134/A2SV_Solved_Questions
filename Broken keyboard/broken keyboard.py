

t = int(input())
for _ in range(t):
    s = input()
    if len(s) == 1:
        print(s)
        continue
    ans = [0]*26
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            i += 2
        elif s[i] != s[i+1]:
            ans[ord(s[i])-97] = 1
            i += 1
        if i == len(s)-1:
            ans[ord(s[i])-97] = 1
    res = []
    for i in range(26):
        if ans[i] == 1:
            res.append(chr(i+97))
    if res:
        print("".join(res))
    else:
        print()
