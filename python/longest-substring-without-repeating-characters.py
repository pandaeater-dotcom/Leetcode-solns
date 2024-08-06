class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        cur = ''
        for char in s:
            if char not in cur:
                cur += char
            else:
                if len(cur) > len(longest):
                    longest = cur
                cur = cur[cur.index(char)+1:] + char
        if len(cur) > len(longest):
            longest = cur
        return len(longest)
