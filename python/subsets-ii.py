class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()

        def recursiveBacktracking(startIndex: int = 0, currSet: List[int] = []):
            for index in range(startIndex, len(nums)):
                if index > startIndex and nums[index] == nums[index - 1]:
                    continue
                currSet.append(nums[index])
                subsets.append(currSet[:])
                recursiveBacktracking(index + 1, currSet[:])
                currSet.pop()
        recursiveBacktracking()
        return subsets
