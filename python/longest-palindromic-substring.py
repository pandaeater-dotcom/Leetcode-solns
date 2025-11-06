class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else longest

        def expand(start, end):
            nonlocal longest
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            
            if end - start - 1 > len(longest):
                longest = s[start + 1: end]

        if s[0] == s[1]:
            expand(0, 1)
        for i in range(2, len(s)):
            if s[i] == s[i - 1]:
                expand(i - 1, i)
            if s[i] == s[i - 2]:
                expand(i - 2, i)
        
        return longest   
            
