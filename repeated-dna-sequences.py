class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        hash = {}
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq not in hash:
                hash[seq] = 1
            else:
                hash[seq] += 1
        return [seq for seq in hash if hash[seq] > 1]
        
