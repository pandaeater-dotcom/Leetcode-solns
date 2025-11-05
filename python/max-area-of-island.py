class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def exploreIsland(x: int, y: int) -> None:
            nonlocal curArea
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == 0:
                return
            grid[y][x] = 0
            curArea += 1
            exploreIsland(x + 1, y)
            exploreIsland(x - 1, y)
            exploreIsland(x, y + 1)
            exploreIsland(x, y - 1)
        
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curArea = 0
                    exploreIsland(j, i)
                    maxArea = max(maxArea, curArea)

        
        return maxArea
