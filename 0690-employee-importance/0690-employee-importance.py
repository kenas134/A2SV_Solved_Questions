"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for node in employees:
            i,im,neigbour = node.id,node.importance,node.subordinates
            graph[i].append(im)
            graph[i].append(neigbour)

        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            size = graph[node][0]
            for neigbour in graph[node][1]:
                size += dfs(neigbour)
            return size
        return dfs(id)

        

        

