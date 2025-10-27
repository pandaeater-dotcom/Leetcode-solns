class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []

        def backtrack(index: int = 0, curr: List[int] = []):
            combinations.append(curr[:])
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack()

        return combinations
