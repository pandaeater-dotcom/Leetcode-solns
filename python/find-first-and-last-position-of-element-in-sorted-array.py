class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = [len(nums), -1]

        def binarySearch(left: int, right: int, upper: bool = False) -> None:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif upper:
                    pos[1] = max(pos[1], mid)
                    left = mid + 1
                else:
                    pos[0] = min(pos[0], mid)
                    right = mid - 1

        binarySearch(0, len(nums) - 1)
        binarySearch(0, len(nums) - 1, True)
        if pos[0] == len(nums):
            pos[0] = -1

        return pos
