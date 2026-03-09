class Solution:
    def scoreOfParentheses(self, s: str) -> int:





        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                stack.pop()
                if s[i-1] == "(":
                    ans += 2 ** len(stack)

        return ans
