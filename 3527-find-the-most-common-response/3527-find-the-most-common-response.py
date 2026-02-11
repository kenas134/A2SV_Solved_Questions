class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ans = []
        for i in responses:
            ans += list(set(i))
        count = Counter(ans)
        maxx = max(count.values())
        arr = []
        for key, value in count.items():
            if value == maxx:
                arr.append(key)
            
        arr.sort()
        return arr[0]
