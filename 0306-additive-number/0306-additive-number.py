class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
         
        def dfs(idx,arr):
            if idx == len(nums):
                return len(arr) >= 3
            
            for i in range(idx,len(nums)):
                if nums[idx] == "0" and i > idx:
                    break
                cur = int(nums[idx:i+1])
                if len(arr) >= 2:
                    if arr[-1] + arr[-2] > cur:
                        continue
                    if arr[-1] + arr[-2] < cur:
                        break
                    
                arr.append(cur)
                if dfs(i+1,arr):
                    return True
                arr.pop()
            return False
        return dfs(0,[])
