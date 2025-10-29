class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def recursiveBacktrack(startIndex: int = 0, currElems: List[int] = [], currSum: int = 0):
            if currSum == target:
                combinations.append(currElems[:])
            elif currSum > target:
                return

            for index in range(startIndex, len(candidates)):
                if index > startIndex and candidates[index] == candidates[index - 1]:
                    continue
                currElems.append(candidates[index])
                recursiveBacktrack(index + 1, currElems[:], currSum + candidates[index])
                currElems.pop()

        recursiveBacktrack()
        return combinations
