class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbour in rooms[node]:
                dfs(neighbour)

            if len(visited) == len(rooms):
                return True
            return False
        return dfs(0)