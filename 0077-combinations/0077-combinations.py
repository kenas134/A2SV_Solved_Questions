class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        # def backtrack(i,arr):
        #     if len(arr) == k:
        #         ans.append(arr[:])
        #         return
        #     if i > n:
        #         return
        #     arr.append(i)
        #     backtrack(i+1,arr)
        #     arr.pop()
        #     backtrack(i+1,arr)
        

        def backtrack(start,arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            for i in range(start,n+1):
                arr.append(i)
                backtrack(i+1,arr)
                arr.pop()
        backtrack(1,[])
        return ans