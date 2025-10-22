class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        longestSubstring = 1
        left, right = 0, 1
        curChars = set()
        curChars.add(s[left])
        while left <= right and right < len(s):
            if s[right] in curChars:
                while (s[right] in curChars) and left <= right:
                    curChars.remove(s[left])
                    left += 1
            else:
                longestSubstring = max(longestSubstring, right - left + 1)
                curChars.add(s[right])
                right += 1

        return longestSubstring
