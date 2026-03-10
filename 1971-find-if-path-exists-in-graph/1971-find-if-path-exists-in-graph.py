class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs():
            visited = set()
            stack = [source]

            while stack:
                cur = stack.pop()
                if cur == destination:
                    return True
                if cur not in visited:
                    visited.add(cur)
                    stack.extend(graph[cur])
            return False
            


        return dfs()
