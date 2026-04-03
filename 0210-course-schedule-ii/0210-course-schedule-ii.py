class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indeg = defaultdict(int)
        for c,p in prerequisites:
            graph[p].append(c)
            indeg[c] += 1
        

        
        queue = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            for neb in graph[cur]:
                indeg[neb] -= 1
                if indeg[neb] == 0:
                    queue.append(neb)
        if len(ans) == numCourses:
            return ans
        return []

        