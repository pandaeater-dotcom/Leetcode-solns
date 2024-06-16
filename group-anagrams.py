class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(string)) for string in strs]
        grouped_strs = []

        hashmap = {}
        for i in range(len(strs)):
            sorted_str = sorted_strs[i]
            if sorted_str not in hashmap:
                hashmap[sorted_str] = len(grouped_strs)
                grouped_strs.append([])
            grouped_strs[hashmap[sorted_str]].append(strs[i])
        
        return grouped_strs
