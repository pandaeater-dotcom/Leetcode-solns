class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        needed = len(t)
        acquired = 0
        diffMap = Counter(t)
        windowStart = 0
        windowLen = 0

        left = 0
        for right in range(len(s)):
            curElem = s[right]
            if curElem in diffMap:
                if diffMap[curElem] > 0:
                    acquired += 1
                diffMap[curElem] -= 1
            if acquired < needed:
                continue

            while acquired == needed:
                if not windowLen or windowLen > right - left + 1:
                    windowStart = left
                    windowLen = right - left + 1
                if s[left] in diffMap:
                    diffMap[s[left]] += 1
                    if diffMap[s[left]] > 0:
                        acquired -= 1
                left += 1

        return s[windowStart:windowStart + windowLen] if windowLen > 0 else ""
