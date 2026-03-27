class Solution:
    def splitString(self, s: str) -> bool:
        # splitted = []
        # def back_track(idx):
        #     if idx >= len(s) and len(splitted) >= 2:
        #         return True
            
        #     for i in range(idx, len(s)):
        #         if not splitted or int(splitted[-1]) - int(s[idx:i+1]) == 1:
        #             splitted.append(s[idx:i+1])
        #             if back_track(i+1):
        #                 return True
        #             splitted.pop()
        #     return False
        # return back_track(0)

        def dfs(idx,prev):

            if idx == len(s):
                return True
            for j in range(idx,len(s)):
                val = int(s[idx:j+1])
                if val + 1 == prev and dfs(j+1,val):
                    return True
                    


        for i in range(len(s)-1):
            val = int(s[:i+1])
            if dfs(i+1,val):
                return True
        return False