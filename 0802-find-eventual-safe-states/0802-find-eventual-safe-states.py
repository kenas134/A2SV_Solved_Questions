class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()
        unsafe = set()

        def dfs(node):
            if node in visited:
                return True
            if node in unsafe or node in visiting:
                return False

            visiting.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    visiting.remove(node)
                    unsafe.add(node)
                    return False
            visited.add(node)
            visiting.remove(node)
            return True

        return [i for i in range(len(graph)) if dfs(i)]
            
