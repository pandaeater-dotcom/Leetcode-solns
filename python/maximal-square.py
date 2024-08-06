class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = [[0]*(n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    memo[i][j] = 1 + min(memo[i + 1][j], memo[i][j + 1], memo[i + 1][j + 1])
        for row in matrix:
            print(row)
        for row in memo:
            print(row)
        return max([max(row) for row in memo])**2
        
            
