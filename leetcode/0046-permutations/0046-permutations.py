class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        check = [False]*len(nums)

        ans = []

        def dfs(i,arr):
            if i == len(nums):
                ans.append(arr[:])
                return
            
            for j in range(len(nums)):
                if check[j]:
                    continue
                
                arr.append(nums[j])
                check[j] = True

                dfs(i+1,arr)

                arr.pop()
                check[j] = False
        dfs(0,[])
        return ans
        
                

