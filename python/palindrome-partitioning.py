class Solution:
    def partition(self, s: str) -> List[List[str]]:
        combinations = []

        def recursiveBacktrack(startIndex: int = 0, currElems: List[str] = []):
            if startIndex == len(s):
                combinations.append(currElems[:])
                return
            for index in range(startIndex + 1, len(s) + 1):
                curString = s[startIndex:index]
                if curString == curString[::-1]:
                    recursiveBacktrack(index, currElems + [curString])

        recursiveBacktrack()
        return combinations
