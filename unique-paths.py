class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n  == 1:
            return 1
        memo = [[0]*n for _ in range(m)]
        memo[0] = [1]*n
        for i in range(m):
            memo[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[-1][-1]
