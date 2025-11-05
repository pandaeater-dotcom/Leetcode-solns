class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def exploreIsland(x: int, y: int) -> None:
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == '0':
                return
            grid[y][x] = '0'
            exploreIsland(x + 1, y)
            exploreIsland(x - 1, y)
            exploreIsland(x, y + 1)
            exploreIsland(x, y - 1)
        
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    numIslands += 1
                    exploreIsland(j, i)
        
        return numIslands
