class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        pp = Counter(p)
        ss = Counter(s)
        cur = Counter(s[:len(p)])
        ans = []
        if cur == pp:
            ans.append(0)
        for i in range(len(p),len(s)):
            cur[s[i-k]] -= 1
            cur[s[i]] += 1
            if cur == pp:
                ans.append(i-k+1)
        return ans

