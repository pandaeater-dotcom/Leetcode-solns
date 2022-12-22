class Solution:
    def reverse(self, x: int) -> int:
        finalstr = ''
        for char in str(x)[::-1]:
            finalstr += char
        if finalstr[-1] == '-':
            finalstr = '-' + finalstr[:-1]
        finalint = int(finalstr)
        if finalint < -2**31 or finalint > 2**31 - 1:
            return 0
        return finalint
