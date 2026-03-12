class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                x = ""
                while stack[-1] != "[":
                    x += stack.pop()[::-1]
                stack.pop()
                y = ""
                while stack and stack[-1].isdigit():
                    y += stack.pop()

                stack.append(x[::-1]*int(y[::-1]))
            else:
                stack.append(s[i])
        return "".join(stack)
