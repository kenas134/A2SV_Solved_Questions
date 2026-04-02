class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        self.minn = float("inf")
        kid = [0]*k
        def dfs(idx):
            if idx == len(cookies):
                self.minn = min(self.minn,max(kid))
                return
            for i in range(k):
                kid[i] += cookies[idx]
                dfs(idx+1)
                kid[i] -= cookies[idx]
                if kid[i] == 0:
                    return

        dfs(0)
        return self.minn
