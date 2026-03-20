class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)

        minn = nums[n-1]
        maxx = nums[0]

        start = -1
        end = -2

        for i in range(1, n):
            maxx = max(maxx, nums[i])
            if nums[i] < maxx:
                end = i
                
        for i in range(n-2, -1, -1):
            minn = min(minn, nums[i])
            if nums[i] > minn:
                start = i

        return end - start + 1