t=int(input())
for _ in range(t):
    n=int(input())
    nlis=list(map(int,input().split()))
    m=int(input())
    mlis=list(map(int,input().split()))
    check=0
    sum1=0
    for i in range(len(nlis)):
        sum1+=nlis[i]
        check=max(check,sum1)
    check1=0
    sum2=0
    for i in range(len(mlis)):
        sum2+=mlis[i]
        check1=max(check1,sum2)
    print(check1+check)
