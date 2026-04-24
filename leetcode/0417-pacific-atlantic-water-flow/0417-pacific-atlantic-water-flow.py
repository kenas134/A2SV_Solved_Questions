class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prev_height):
            # bounds + height check
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        # Pacific (top + left)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
        
        # Atlantic (bottom + right)
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        # Intersection
        return list(pacific & atlantic)