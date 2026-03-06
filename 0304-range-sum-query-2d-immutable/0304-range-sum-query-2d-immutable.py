class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        n = len(matrix)
        m = len(matrix[0])
        self.pref = [[0] * (m + 1) for _ in range(n+1) ]

        for i in range(n):
            for j in range(m):
                self.pref[i][j] = self.matrix[i][j] + self.pref[i-1][j] + self.pref[i][j-1] -self.pref[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        box = self.pref[row2][col2] 
        left = self.pref[row2][col1-1]
        right = self.pref[row1-1][col2]
        overlap = self.pref[row1-1][col1-1]
        return box - left - right + overlap
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)