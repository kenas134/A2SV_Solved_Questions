class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        op = 0
        prev = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                k = ceil(nums[i]/prev)
                op += k-1
                prev = nums[i]//k
        return op
