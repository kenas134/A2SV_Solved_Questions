class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)
        maxx = max(heights)
        arr = [0]*(maxx+1)
        for i in range(n):
            arr[heights[i]] = names[i]

        x = []
        for i in range(maxx,-1,-1):
            if arr[i] != 0:
                x.append(arr[i])
        return x


            