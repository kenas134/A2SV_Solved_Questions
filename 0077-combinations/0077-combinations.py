class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i,arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            if i > n:
                return
            arr.append(i)
            backtrack(i+1,arr)
            arr.pop()
            backtrack(i+1,arr)
        backtrack(1,[])
        return ans