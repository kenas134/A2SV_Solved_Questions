class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def rec(i, j):
            if i == j:
                return nums[i]
            
            pick_left = nums[i] - rec(i+1, j)
            pick_right = nums[j] - rec(i, j-1)
            
            return max(pick_left, pick_right)
        
        return rec(0, len(nums)-1) >= 0