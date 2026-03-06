class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxx = nums[0]

        for i in range(len(nums)):
            cur += nums[i]
            if cur > maxx:
                maxx = cur
               
            if cur < 0:
                cur = 0

        return maxx