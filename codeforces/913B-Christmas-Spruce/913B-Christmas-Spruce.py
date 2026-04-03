from collections import defaultdict


n = int(input())
tree = defaultdict(list)


for i in range(n-1):
    cur = int(input())
    tree[cur].append(i+2)

for key in tree.keys():
    count = 0
    for num in tree[key]:
        if tree.get(num,[]) == []:
            count += 1

    if count < 3:
        print("No")
        break
else:
    print("Yes")