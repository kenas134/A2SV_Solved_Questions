class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def dfs(k,n):
            cur = 2 ** n
            if k == 1:
                return "0"
            elif k == cur//2:
                return "1"
            elif k < cur//2:
                return dfs(k,n-1)
            else:
                ans = dfs(cur-k,n-1)
                return "0" if ans == "1" else "1"
        return dfs(k,n)


