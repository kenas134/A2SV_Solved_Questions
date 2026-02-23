class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(i,arr):
            if i == len(nums):
                ans.append(arr[:])
                return 

            arr.append(nums[i])
            backtrack(i+1,arr)
            arr.pop()

            
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            backtrack(i+1,arr)
        backtrack(0,[])
        return ans
            