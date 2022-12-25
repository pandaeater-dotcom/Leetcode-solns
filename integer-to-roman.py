class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        romanMap = {0: ('I', 'V'), 1: ('X', 'L'), 2: ('C', 'D'), 3: ('M', 'M')}
        size = len(str(num))-1
        while num != 0:
            msd = num // 10**size
            if msd == 9:
                roman += romanMap[size][0] + romanMap[size + 1][0]
            elif msd >= 5:
                roman += romanMap[size][1] + romanMap[size][0]*(msd - 5)
            elif msd == 4:
                roman += romanMap[size][0] + romanMap[size][1]
            else:
                roman += romanMap[size][0]*msd
            if num < 10:
                num = 0
            else:
                num = int(str(num)[1:])
            size = len(str(num)) - 1
        return roman
