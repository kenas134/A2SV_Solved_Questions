

t = int(input())
for _ in range(t):
    n,x,s = map(int,input().split())
    st = input().strip()
    yes = False
    ans = 0
    j = 0

    #check if it reach zero

    for i in st:
        if j < s:
            if i == "R":
                ans += 1
            else:
                ans -= 1
            j += 1
            if ans + x == 0:
                yes = True
                break
    # if yes chech loop
    loop = False
    if yes:
        ans = 0
        r = 0
        for i in st:
            if i == "L":
                ans -= 1
            else:
                ans += 1
            r += 1
            if ans == 0:
                break
    if not yes:
        print(0)
    elif ans:
        print(1)
    else:
        print((s-j)//r + 1)


        

    

