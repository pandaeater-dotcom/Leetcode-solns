class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while (l < r):
            if nums[l] > nums[r]:
                l += 1
                r -= 1
            elif nums[l] < nums[r]:
                if nums[l] < nums[l - 1]:
                    return nums[l]
                return nums[r + 1]
        if nums[r + 1] < nums[r]:
            return nums[r + 1]
        else:
            return nums[r]
