from collections import deque, defaultdict
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for _ in range(n)]
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # Build graph and compute in-degree
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Initialize queue with nodes having in-degree 0
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])
                
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return [sorted(list(anc)) for anc in ancestors]