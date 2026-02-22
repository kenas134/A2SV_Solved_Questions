class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        check = [False] * len(nums)
        def backtrack(arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return
            for i in range(len(nums)):
                if not check[i]:
                    arr.append(nums[i])
                    check[i] = True
                    backtrack(arr)
                    arr.pop()
                    check[i] = False

        backtrack([])
        return ans
                
                

