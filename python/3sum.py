class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        unique_combos = []

        for i in range(len(sortedNums) - 2):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = sortedNums[i] + sortedNums[left] + sortedNums[right]
                if total == 0:
                    unique_combos.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1

                    while left < right and sortedNums[left] == sortedNums[left - 1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
        return unique_combos
