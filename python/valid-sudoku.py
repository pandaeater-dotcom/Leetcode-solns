class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sideLen = 9
        colSets = [set() for _ in range(sideLen)]
        boxSets = [set() for _ in range(sideLen)]
        
        for row in range(sideLen):
            rowSet = set()
            for square in range(sideLen):
                num = board[row][square]
                if num == '.':
                    continue
                boxIndex = row // 3 * 3 + square // 3
                if num in rowSet or num in colSets[square] or num in boxSets[boxIndex]:
                    return False
                rowSet.add(num)
                boxSets[boxIndex].add(num)
                colSets[square].add(num)

        return True

