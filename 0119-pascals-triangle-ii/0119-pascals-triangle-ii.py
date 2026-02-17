class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(n):
            if n == 0:
                return [1]
            elif n == 1:
                return [1,1]
            prev = pascal(n-1)
            arr = [1]
            for i in range(1,n):
                arr.append(prev[i-1]+prev[i])
            arr.append(1)
            return arr
        return pascal(rowIndex)

