class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []
        changed.sort()
        chk = Counter(changed)

        ans = []
        for x in changed:
            if chk[x] == 0:
                continue
            if chk[2*x] == 0:
                return []
            
            ans.append(x)
            chk[x] -= 1
            chk[2*x] -= 1
        return ans

