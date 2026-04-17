def dnc(left , right):
    if left == right:
        return [[arr[left]],0]
    
    mid = (left+right)//2

    lefthalf,l = dnc(left,mid)
    righthalf,r = dnc(mid+1,right)

    if l == -1 or r == -1:
        return [[],-1]
    return merge(lefthalf,righthalf,l+r)
def merge(lefthalf,righthalf,n):
    if lefthalf[0] <= lefthalf[-1] <= righthalf[0]:
        return [lefthalf+righthalf,n]
    elif righthalf[0] <= righthalf[-1] <= lefthalf[0]:
        return [righthalf+lefthalf,n+1]
    else:
        return [[],-1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    x,nm = dnc(0,n-1)
    print(nm)