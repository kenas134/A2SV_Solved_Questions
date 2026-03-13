class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]


        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        minutes = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()

                for x,y in directions:
                    new_row, new_col = row + x, col + y
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            minutes += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes-1 if minutes != 0 else 0
                    
        
        
        
