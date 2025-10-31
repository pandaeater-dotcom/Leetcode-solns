class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        combinations = []

        def placeable(x: int, y: int, queens: set[tuple[int, int]]) -> bool:
            for queen in queens:
                if x == queen[0] or y == queen[1]:
                    return False
                if abs((y - queen[1]) / (x - queen[0])) == 1:
                    return False
            return True

        def recursiveBacktrack(index: int, current: list[str], queens: set[tuple[int, int]]) -> None:
            if index >= n * n:
                if len(queens) == n:
                    combinations.append(current)
                return
            y = index // n
            x = index % n

            canPlace = placeable(x, y, queens)
            if canPlace:
                oldString = current[y]
                current[y] = current[y][:x] + "Q" + current[y][x + 1:]
                recursiveBacktrack(index + 1, current[:], queens.union({(x, y)}).copy())
                current[y] = oldString
            recursiveBacktrack(index + 1, current, queens)

        board = []
        for _ in range(n):
            board.append("." * n)
        recursiveBacktrack(0, board, set())
        return combinations
