class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lst = ['' for x in range(numRows)]
        # charMap = {}
        col = 0
        row = -1
        for x in s:
            if col % (numRows - 1) == 0 and row < numRows - 1:
                row += 1
                lst[row] += x
                # charMap[(row, col)] = x
            else:
                row -= 1
                col += 1
                lst[row] += x
                # charMap[(row, col)] = x
        finalstr = ''
        for x in lst:
            finalstr += x
        return finalstr     
