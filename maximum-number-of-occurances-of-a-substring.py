class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = {}

        for i in range(len(s)-minSize+1):
            sub = s[i:i+minSize]        
            if len(set(sub)) > maxLetters:
                continue
            if sub in d:
                d[sub] += 1
            else:
                d[sub] = 1
        if (not d):
            return 0
        return max(d.values())
