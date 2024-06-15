class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            if t[i] in d:
                d[t[i]] -= 1
            else:
                d[t[i]] = -1
        for value in d.values():
            if value != 0:
                print(value)
                return False
        return True
            
