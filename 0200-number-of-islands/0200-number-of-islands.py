class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        visited = set()
        ans = 0
        def bfs(i,j):
            queue = deque()
            visited.add((i,j))
            queue.append((i,j))
            while queue:
                cr,cc = queue.popleft()
                
                for dr,dc in dir:
                    r = cr + dr
                    c = cc + dc
                    if   0 <= r < ROW and 0 <= c < COL and grid[r][c] == "1" and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))


        for i in range(ROW):
            for j in range(COL):
                if 0 <= i < ROW and 0 <= j < COL and grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    ans += 1
        return ans
