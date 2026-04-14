class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        visited = [[0]*COL for i in range(ROW)]

        di = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        def bfs(i,j):
            queue.append((i,j))
            visited[i][j] = 1
            while queue:
                cx,cy = queue.popleft()

                for dx,dy in di:
                    x = cx + dx
                    y = cy + dy

                    if 0<= x < ROW and 0 <= y < COL and not visited[x][y] and grid[x][y] == "1":
                        queue.append((x,y))
                        visited[x][y] = 1




        ans = 0
        for i in range(ROW):
            for j in range(COL):
                if not visited[i][j] and grid[i][j] == "1":
                    ans += 1
                    bfs(i,j)

        return ans

        