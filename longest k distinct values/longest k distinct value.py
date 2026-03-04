import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = {}
distinct = 0
l = 0

best_l, best_r = 0, 0

for r in range(n):
    # Add a[r]
    if a[r] not in cnt or cnt[a[r]] == 0:
        distinct += 1
        cnt[a[r]] = 1
    else:
        cnt[a[r]] += 1

    # If too many distinct values, shrink from the left
    while distinct > k:
        cnt[a[l]] -= 1
        if cnt[a[l]] == 0:
            distinct -= 1
        l += 1

    # Update best segment
    if r - l > best_r - best_l:
        best_l, best_r = l, r

# Print 1-based indices
print(best_l + 1, best_r + 1)
