class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.op = "abc"
        self.cur = 0
        def dfs(idx,s):
            if idx == n:
                self.cur += 1

                if self.cur == k:
                    return s
                return ""
            for i in self.op:
                if  s and s[-1] == i:
                    continue
                c = dfs(idx+1,s+i)
                if c:
                    return c
            return ""
        return dfs(0,"")
            




