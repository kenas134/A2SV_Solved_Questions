class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        maxx = cur 
        left = 0
        for right in range(k,len(nums)):
            cur += (nums[right]-nums[left])
            maxx = max(cur,maxx)
            left += 1
        return maxx/k