from collections import deque, defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build graph
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Ancestor sets
        ancestors = [set() for _ in range(n)]
        
        # Topological queue
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        while queue:
            node = queue.popleft()
            
            for nei in graph[node]:
                # Add current node
                ancestors[nei].add(node)
                # Add all ancestors of current node
                ancestors[nei].update(ancestors[node])
                
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        # Convert to sorted list
        return [sorted(list(a)) for a in ancestors]