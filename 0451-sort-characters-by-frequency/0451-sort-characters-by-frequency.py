class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        ans = list(count.items())
        print(ans)
        ans2 = sorted(ans,reverse=True,key=lambda x:x[1])
        arr = []
        for i,j in ans2:
            t  = 0
            while t < j:
                arr.append(i)
                t += 1
        return "".join(arr) 
