class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for c,p in prerequisites:
            graph[p].append(c)

        def dfs(node,gray):
            if node in gray:
                return False

            gray.add(node)
            
            for neb in graph[node]:
                if neb not in visited:
                    if not dfs(neb,gray):
                        return False
            ans.append(node)
            gray.remove(node)
            visited.add(node)
            return True
            

        visited = set()
        ans = []
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i,set()):
                    return []
        return ans[::-1]
        
        