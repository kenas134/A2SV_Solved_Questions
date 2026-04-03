class Solution:
    def splitString(self, s: str) -> bool:
        

        ans = []

        def dfs(idx):

            if idx == len(s) and len(ans) >= 2:
                return True
            
            for i in range(idx,len(s)):
                if not ans or int(ans[-1])  == int(s[idx:i+1])+1:
                    ans.append(s[idx:i+1])
                    if dfs(i+1):
                        return True
                    ans.pop()
                elif int(ans[-1])  < int(s[idx:i+1]):
                    break
            return False
        return dfs(0)


