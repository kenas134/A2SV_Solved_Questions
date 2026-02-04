class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        chk = Counter(list(s1))
        a = Counter(list(s2[:k]))
        if a == chk:
            return True
        for i in range(k,len(s2)):
            a[s2[i-k]] -= 1
            a[s2[i]] += 1
            if a == chk:
                return True
        return False

