class Solution:
    def wordBreak(self, st: str, wordDict: List[str]) -> List[str]:
        

        ans = []
        def dfs(idx,s,arr):
            if idx == len(st) and s == "":
                ans.append(" ".join(arr))
                return
            if idx == len(st):
                return
                

            dfs(idx+1,s+st[idx],arr)
            if s+st[idx] in wordDict:
                arr.append(s+st[idx])
                dfs(idx+1,"",arr)
                arr.pop()
        dfs(0,"",[])
        return ans

