class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        chk = defaultdict(list)
        n = len(mat)
        m = len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                chk[i+j].append(mat[i][j])

        ans = []
        for i in range(n+m+1):
            if i % 2 == 0:
                ans += chk[i][::-1]
            else:
                ans += chk[i]
        return ans

        
