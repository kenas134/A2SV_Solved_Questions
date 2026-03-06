class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        summ = 1
        ans = 1
        for i in range(n):
            summ += nums[i]
            if summ < 1:
                ans += 1 - summ
                summ = 1
        return ans
