class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def recursiveVisit(index: int):
            nonlocal visited
            visited.add(index)
            for room in rooms[index]:
                if room not in visited:
                    recursiveVisit(room)
        
        recursiveVisit(0)
        return len(visited) == len(rooms)
