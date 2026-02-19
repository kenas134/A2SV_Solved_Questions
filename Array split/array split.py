

n,k = map(int,input().split())
arr = list(map(int,input().split()))

diff = []
for i in range(1,n):
    diff.append([i,arr[i]-arr[i-1]])
diff.sort(key=lambda x:x[1],reverse=True)

cut = []
for i in range(k-1):
    cut.append(diff[i][0])

cut.sort()

summ = 0
l = arr[0]
for i in range(len(cut)):
    summ += arr[cut[i]-1]-l
    l = arr[cut[i]]
summ += arr[-1]-l
print(summ)


    
    
