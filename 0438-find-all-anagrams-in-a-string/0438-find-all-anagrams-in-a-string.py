class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        check = Counter(p)
        k,n = len(p),len(s)
        cur = Counter(s[:k])
        ans = []
        if cur == check:
            ans.append(0)

        for i in range(k,n):
            cur[s[i]] += 1
            cur[s[i-k]] -= 1
            if check == cur:
                ans.append(i-k+1)
        return ans 
