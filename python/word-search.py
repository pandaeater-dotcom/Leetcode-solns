class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxY = len(board) - 1
        maxX = len(board[0]) - 1
        visitedSet = set()

        def recursiveCheck(x: int, y: int, curIndex: int = 0) -> bool:
            if curIndex == len(word):
                return True
            if (x, y) in visitedSet or x > maxX or x < 0 or y > maxY or y < 0 or board[y][x] != word[curIndex]:
                return False

            curIndex += 1
            visitedSet.add((x, y))
            res = False
            res = recursiveCheck(x + 1, y, curIndex) or recursiveCheck(x - 1, y, curIndex) or recursiveCheck(x, y + 1, curIndex) or recursiveCheck(x, y - 1, curIndex)
            visitedSet.remove((x, y))
            return res

        for j in range(maxY + 1):
            for i in range(maxX + 1):
                if board[j][i] != word[0]:
                    continue
                if len(word) == 1 or recursiveCheck(i, j):
                    return True

        return False
