class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        left = 0
        ans = float("inf")
        for i in range(len(nums)):
            summ += nums[i]
            while summ >= target:
                ans = min(i-left+1,ans)
                summ -= nums[left]
                left += 1
        return ans if ans != float("inf") else 0
            

            