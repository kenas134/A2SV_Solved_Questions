class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        posdiag = set()
        negdiag = set()
        col = []
        ans = []
        def backtrack(row):
            if row == n:
                cur  = []
                for i in range(n):
                    a = col[i]
                    res = "."*(a)+"Q"+"."*(n-a-1)
                    cur.append(res)
                ans.append(cur)
                return

            for i in range(n):

                if i + row not in negdiag and i-row not in posdiag and i not in col:
                    col.append(i)
                    posdiag.add(i-row)
                    negdiag.add(i+row)
                    backtrack(row+1)
                    col.pop()
                    posdiag.remove(i-row)
                    negdiag.remove(i+row)
        backtrack(0)
        return ans


        
