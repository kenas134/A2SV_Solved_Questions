class Solution:
    def isValid(self, s: str) -> bool:
        
        def closed(s1,j):
            return s1 == "{" and j == "}" or s1 == "(" and j == ")" or s1 == "[" and j == "]" 


        stack = []
        for i in range(len(s)):
            if s[i] in "{([":
                stack.append(s[i])
            else:
                if stack:
                    cur = stack.pop()
                    if not closed(cur,s[i]):
                        return False
                else:
                    return False
        return not stack
