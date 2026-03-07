import sys
input = sys.stdin.readline

n,m = map(int,input().split())

mat = [""]*(n+1)
mat[0] = "#"*(m+1)

for i in range(1,n+1):
    mat[i] = "#" + input().strip()

hor = [[0]*(m+1) for _ in range(n+1)]
ver = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):

        if mat[i][j]=='.' and mat[i][j-1]=='.':
            hor[i][j] = 1

        if mat[i][j]=='.' and mat[i-1][j]=='.':
            ver[i][j] = 1

for i in range(1,n+1):
    for j in range(1,m+1):
        hor[i][j] += hor[i-1][j] + hor[i][j-1] - hor[i-1][j-1]
        ver[i][j] += ver[i-1][j] + ver[i][j-1] - ver[i-1][j-1]

q = int(input())

for _ in range(q):

    r1,c1,r2,c2 = map(int,input().split())

    h = hor[r2][c2] - hor[r2][c1] - hor[r1-1][c2] + hor[r1-1][c1]
    v = ver[r2][c2] - ver[r2][c1-1] - ver[r1][c2] + ver[r1][c1-1]

    print(h+v)
