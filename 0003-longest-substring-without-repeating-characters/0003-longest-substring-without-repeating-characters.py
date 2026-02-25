class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        left = 0
        sett = set()
        for i in range(len(s)):
            if s[i] not in sett:
                sett.add(s[i])
                maxx = max(maxx,len(sett))
            else:
                while s[i] in sett:
                    sett.remove(s[left])
                    left += 1
                sett.add(s[i])
        return maxx