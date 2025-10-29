class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def recursiveCombinationSum(startIndex: int = 0, currSet: List[int] = [], currSum: int = 0):
            if currSum > target:
                return
            for index in range(startIndex, len(candidates)):
                currSet.append(candidates[index])
                currSum += candidates[index]
                if currSum == target:
                    combinations.append(currSet[:])
                recursiveCombinationSum(index, currSet[:], currSum)
                # recursiveCombinationSum(index + 1, currSet[:], currSum)
                currSum -= candidates[index]
                currSet.pop()
        recursiveCombinationSum()
        return combinations
