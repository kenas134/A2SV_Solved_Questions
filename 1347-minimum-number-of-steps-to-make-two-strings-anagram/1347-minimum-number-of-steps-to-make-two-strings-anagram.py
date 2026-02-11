class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s2 = Counter(s)
        t2 = Counter(t)
        ans = 0
        for key in t2.keys():
            if key in s2:
                ans += max(0,t2[key]-s2[key])
            else:
                ans += t2[key]
        return ans

