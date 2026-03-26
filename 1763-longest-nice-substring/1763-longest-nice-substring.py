class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        sett = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in sett:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        return s