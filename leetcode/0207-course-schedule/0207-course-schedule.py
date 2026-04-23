class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)


        visited = [2]*numCourses

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 0:
                return True
            
            visited[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 0
            return True

        for i in range(numCourses):
            if visited[i] == 2:
                if not dfs(i):
                    return False
        return True
