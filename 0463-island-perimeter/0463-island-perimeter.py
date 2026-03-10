class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def explore(i,j):
            rowInBound = 0<=i<len(grid)
            colInBound = 0<=j<len(grid[0])

            if (i,j) in visited:
                return 0
            
            if not rowInBound or not colInBound:
                return 1

            if grid[i][j] == 0:
                return 1
            visited.add((i,j))
            size = 0
            size += explore(i,j+1)
            size += explore(i,j-1)
            size += explore(i+1,j)
            size += explore(i-1,j)
            return size

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return explore(i,j)



