class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {"{":"}","(":")","[":"]"}


        stack = []
        for i in range(len(s)):
            if s[i] in "{([":
                stack.append(s[i])
            else:
                if stack:
                    cur = stack.pop()
                    if pair[cur] != s[i]:
                        return False
                else:
                    return False
        return not stack
