class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def can(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            cur = 0
            for i in range(n):
                cur += diff[i]
                if cur < nums[i]:
                    return False
            return True

        left, right = 0, len(queries)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
