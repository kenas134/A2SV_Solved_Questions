class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        negdig = set()
        posdig = set()
        col = [False]*n

        def dfs(row):
            if row == n:
                self.ans += 1
            for i in range(n):
                if not col[i] and i + row not in posdig and  i - row not in negdig:
                    negdig.add(i-row)
                    posdig.add(i+row)
                    col[i] = True
                    dfs(row+1)
                    negdig.remove(i-row)
                    posdig.remove(i+row)
                    col[i] = False
        dfs(0)
        return self.ans                 