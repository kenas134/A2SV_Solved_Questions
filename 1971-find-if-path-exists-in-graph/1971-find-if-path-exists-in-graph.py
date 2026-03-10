class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            if node == destination:
                return True
            visited.add(node)

            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True
            return False

        return dfs(source)

