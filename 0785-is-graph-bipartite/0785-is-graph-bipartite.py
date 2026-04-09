class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*(len(graph))

        def bfs(i):
            if color[i]:
                return True
            color[i] = -1

            queue = deque([i])
            while queue:
                i = queue.popleft()
                for nei in graph[i]:
                    if color[nei] == color[i]:
                        return False
                    elif not color[nei]:
                        color[nei] = color[i]*-1
                        queue.append(nei)

            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True