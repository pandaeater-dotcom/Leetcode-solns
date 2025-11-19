class Solution:
    def findLargerIndex(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for i in range(len(nums)):
            index = self.findLargerIndex(sub, nums[i])
            if index >= len(sub):
                sub.append(nums[i])
            else:
                sub[index] = nums[i]
        
        return len(sub)
