class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        x = 1
        i = 0
        while len(arr) > 1:
            if x == k:
                arr.pop(i)
                x = 1
            else:
                i = (i+1)%len(arr)
                x += 1
        return arr[0]

            