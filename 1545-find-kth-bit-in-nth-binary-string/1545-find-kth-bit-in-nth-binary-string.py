class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            s = s[::-1]
            x = []
            for i in s:
                if i == "1":
                    x.append("0")
                else:
                    x.append("1")
            return "".join(x)

        arr = ["0"]

        for i in range(n):
            s = arr[-1]
            arr.append(s+"1"+invert(s))

        return arr[n-1][k-1]

