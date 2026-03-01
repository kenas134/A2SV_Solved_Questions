class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        x = 1
        cur = 0
        point = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            elif x == 1:
                x = 0
                point = i
            else:
                cur = i - point - 1
                point = i 
            ans = max(cur,ans)
        if len(nums) == ans:
            ans -= 1
        return ans
