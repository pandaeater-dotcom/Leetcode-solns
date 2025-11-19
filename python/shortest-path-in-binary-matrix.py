class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1))
        n = len(grid)
        queue = deque()
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        queue.append((0, 0, 1))
        grid[0][0] = 1
        while queue:
            i, j, dist = queue.popleft()
            if i == n - 1 and j == n - 1:
                return dist
            for di, dj in dirs:
                newi, newj = i + di, j + dj
                if newi < 0 or newi > n - 1 or newj < 0 or newj > n - 1 or grid[newi][newj]:
                    continue
                grid[newi][newj] = 1
                queue.append((newi, newj, dist + 1))
        return -1
