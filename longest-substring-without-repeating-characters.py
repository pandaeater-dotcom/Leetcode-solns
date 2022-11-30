class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        accum = ""
        highest = 0
        for x in s:
            if x not in accum:
                accum += x
            else:
                if (highest < len(accum)):
                    highest = len(accum)
                accum += x
                accum = accum[accum.index(x)+1:]
        if highest < len(accum):
            return len(accum)
        return highest
