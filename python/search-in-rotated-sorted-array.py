class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = nums[mid]

            if value > target:
                if nums[right] >= target and value > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif value < target:
                if nums[left] <= target and value < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return mid

        return -1
