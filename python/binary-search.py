class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            value = nums[mid]
            print(mid, value)
            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                index = mid
                break
        
        return index
