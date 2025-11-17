class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        m, n = len(board), len(board[0])

        def exploreRegion(x: int, y: int) -> None:
            if x < 0 or x > n - 1 or y < 0 or y > m - 1 or board[y][x] == 'X' or (x, y) in visited:
                return
            visited.add((x, y))
            board[y][x] = 'S'
            exploreRegion(x + 1, y)
            exploreRegion(x - 1, y)
            exploreRegion(x, y + 1)
            exploreRegion(x, y - 1)

        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'X' or (j, i) in visited:
                    continue
                exploreRegion(j, i)
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'X' or (j, i) in visited:
                    continue
                exploreRegion(j, i)

        for i in range(m):
            for j in range(n):
                elem = board[i][j]
                print(elem)
                if elem == 'X':
                    continue
                board[i][j] = 'O' if elem == 'S' else 'X'
