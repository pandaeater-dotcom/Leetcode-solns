class Solution:
    def __init__(self):
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        minutes = -1
        counter = len(queue)
        while queue:
            i, j = queue.popleft()
            for dir in self.dirs:
                y, x = i + dir[0], j + dir[1]
                if x < 0 or y < 0 or y > len(grid) - 1 or x > len(grid[0]) - 1 or grid[y][x] != 1:
                    continue
                grid[y][x] = 2
                queue.append((y, x))
            counter -= 1
            if not counter:
                minutes += 1
                counter = len(queue)
                print(minutes, counter)

        for row in grid:
            if 1 in row:
                return -1

        return max(0, minutes)
