class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        seen = set()
        def dfs(node):
            seen.add(node)
            for nei in rooms[node]:
                if nei not in seen:
                    dfs(nei)
        dfs(0)
        return len(seen) == len(rooms)