class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        currentMaxRange = 0

        for i in range(n - 1):
            farthest = max(farthest, nums[i] + i)
            if i == currentMaxRange:
                currentMaxRange = farthest
                jumps += 1

        return jumps
