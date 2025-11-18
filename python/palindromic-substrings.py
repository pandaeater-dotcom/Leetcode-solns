class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = len(s)
        count = 0
        cache = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    cache[i][j] = True
                elif j == i + 1:
                    cache[i][j] = s[i] == s[j]
                else:
                    cache[i][j] = s[i] == s[j] and cache[i + 1][j - 1]
                if cache[i][j]:
                    count += 1
        return count
