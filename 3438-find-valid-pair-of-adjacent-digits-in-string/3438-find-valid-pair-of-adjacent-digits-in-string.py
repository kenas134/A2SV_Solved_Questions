class Solution:
    def findValidPair(self, s: str) -> str:
        ans = Counter(s)
        for i in range(len(s)-1):
            if s[i] != s[i+1] and ans[s[i]] == int(s[i]) and ans[s[i+1]] == int(s[i+1]):
                return s[i]+s[i+1]
        return ""