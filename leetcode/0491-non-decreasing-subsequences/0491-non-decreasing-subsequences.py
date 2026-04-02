class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def dfs(start,arr):
            if len(arr) >= 2:
                ans.append(arr[:])
            sett = set()    
            for i in range(start,len(nums)):
                if (nums[i] in sett) or (arr  and nums[i] < arr[-1]) :
                    continue
                arr.append(nums[i])
                sett.add(nums[i])
                dfs(i+1,arr)
                arr.pop()
        dfs(0,[])
        return ans
