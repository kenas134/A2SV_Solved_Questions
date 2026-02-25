class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        maxx = cur 
        for i in range(k,len(nums)):
            cur += (nums[i]-nums[i-k])
            maxx = max(cur,maxx)
        return maxx/k