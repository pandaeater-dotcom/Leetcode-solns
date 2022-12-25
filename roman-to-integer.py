class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for x in range(len(s)):
            if x < len(s) - 1 and romanMap[s[x]] < romanMap[s[x + 1]]:
                num -= romanMap[s[x]]
            else:
                num += romanMap[s[x]]
        return num
