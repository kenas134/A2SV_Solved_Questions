def dfs(idx,t,n,x):
    if idx == len(t) and n == x:
        ans[0] += 1
        return
    elif idx == len(t):
        ans[1] += 1
        return
    
    if t[idx] == "+":
        n += 1
        dfs(idx+1,t,n,x)
    elif t[idx] == "-":
        n -= 1
        dfs(idx+1,t,n,x)
    else:
        n += 1
        dfs(idx+1,t,n,x)
        n -= 2
        dfs(idx+1,t,n,x)

dfs(0,t,0,x)
print(ans[0]/(ans[0]+ans[1]))