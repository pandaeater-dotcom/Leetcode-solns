class Solution:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        queue = deque()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if not rooms[i][j]:
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            distance = rooms[i][j] + 1
            for dir in self.dirs:
                y, x = i + dir[0], j + dir[1]
                if x < 0 or y < 0 or y > m - 1 or x > n - 1 or rooms[y][x] != 2147483647:
                    continue
                rooms[y][x] = distance
                queue.append((y, x))
