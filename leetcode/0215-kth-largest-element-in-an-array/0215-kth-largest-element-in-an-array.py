class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        i = 0 
        while i < k:
            if i == k-1:
                return -1*heapq.heappop(nums)
            heapq.heappop(nums)
            i += 1

