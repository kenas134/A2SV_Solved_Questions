from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # Step 1: Build reverse graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

        # DFS function
        def dfs(node, visited):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, visited)

        # Step 2: Run DFS for each node
        res = []
        for i in range(n):
            visited = set()
            dfs(i, visited)
            res.append(sorted(visited))

        return res