class Solution:
    def smallestNumber(self, pattern: str) -> str:
        taken = [False]*10
        def dfs(idx,s):
            if idx == len(pattern):
                if len(s) == len(pattern)+1:
                    return s
                return ""

            for i in range(1,10):
                if taken[i]:
                    continue
                if pattern[idx] == "I" and i < int(s[-1]):
                    continue
                if pattern[idx] == "D" and i > int(s[-1]):
                    continue

                taken[i] = True
                cur = dfs(idx+1,s+str(i))
                if cur:
                    return cur
                taken[i] = False




        for i in range(1,10):
            taken[i] = True
            cur = dfs(0,str(i))
            if cur:
                return cur
            taken[i] = False
        