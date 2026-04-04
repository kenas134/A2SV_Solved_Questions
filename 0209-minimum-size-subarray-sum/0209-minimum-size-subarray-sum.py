class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pref = [0]
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            pref.append(summ)

        ans = float("inf")
        for i in range(len(nums)):

            need = pref[i] + target

            j = bisect_left(pref,need)

            if j <= len(nums):
                ans = min(j-i,ans)
        return ans if ans != float("inf") else 0

            