class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*(len(graph))

        def dfs(i,c):
            if color[i] != 0:
                return True
            color[i] = c
            for nei in graph[i]:
                if color[nei] != 0 and  color[nei] == color[i]:
                    return False
                if color[nei] != 0:
                    continue
                if not dfs(nei,-1*c):
                    return False
            return True


        for i in range(len(graph)):
            if not dfs(i,-1):
                return False
        return True