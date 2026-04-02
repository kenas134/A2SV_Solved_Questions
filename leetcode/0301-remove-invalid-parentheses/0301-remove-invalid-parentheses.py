class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = set()
        self.maxx = -1
        def dfs(idx,op,cl,arr):
            if idx == len(s):
                if op == cl:
                    if len(arr) > self.maxx:
                        self.maxx = len(arr)
                        ans.clear()
                        ans.add("".join(arr))
                    elif len(arr) == self.maxx:
                        ans.add("".join(arr))
                return

            cur = s[idx]

            if cur == "(":
                arr.append("(")
                dfs(idx+1,op+1,cl,arr)
                arr.pop()
                dfs(idx+1,op,cl,arr)
            elif cur == ")":
                dfs(idx+1,op,cl,arr)
                if op > cl:
                    arr.append(")")
                    dfs(idx+1,op,cl+1,arr)
                    arr.pop()
            else:
                arr.append(cur)
                dfs(idx+1,op,cl,arr)
                arr.pop()
        dfs(0,0,0,[])
        return list(ans)               
                 

    