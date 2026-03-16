class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        i = 0

        need = 1
        ans = 0
        while need <= n:
            if i < len(nums) and nums[i] <= need:
                need += nums[i]
                i += 1
            else:
                need *= 2
                ans += 1
        return ans