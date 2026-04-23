class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(i,j):
            grid[i][j] = "0"

            for dx,dy in dir:
                nx,ny = i+dx,j+dy

                if 0<= nx < ROW and 0 <= ny < COL and grid[nx][ny] == "1":
                    dfs(nx,ny)


        ans = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans