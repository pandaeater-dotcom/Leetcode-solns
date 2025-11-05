class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1
        while index > 0 and nums[index - 1] >= nums[index]:
            index -= 1

        if index == 0:
            nums.reverse()
            return

        pivot = index
        index = len(nums) - 1
        while index > pivot - 1 and nums[index] <= nums[pivot - 1]:
            index -= 1
        nums[pivot - 1], nums[index] = nums[index], nums[pivot - 1]
        nums[pivot:] = reversed(nums[pivot:])
