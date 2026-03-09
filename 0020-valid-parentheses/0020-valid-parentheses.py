class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {"{":"}","(":")","[":"]"}


        stack = []
        for i in range(len(s)):
            if s[i] in "{([":
                stack.append(s[i])
            else:
                if stack and pair[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        return not stack
