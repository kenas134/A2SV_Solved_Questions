class Solution:
    def isValid(self, s: str) -> bool:
        def open(s1):
            return s1 in "{(["
        def closed(s1,j):
            return s1 == "{" and j == "}" or s1 == "(" and j == ")" or s1 == "[" and j == "]" 


        stack = []
        for i in range(len(s)):
            if open(s[i]):
                stack.append(s[i])
            else:
                if stack:
                    cur = stack.pop()
                    if not closed(cur,s[i]):
                        return False
                else:
                    return False
        return not stack
