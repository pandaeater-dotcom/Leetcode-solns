class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        for i in range(0, m):
            cache[i][0] = 1
        for j in range(0, n):
            cache[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
        
        return cache[-1][-1]
