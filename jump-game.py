class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        end = len(nums) - 1
        for cur in range(len(nums) - 2, -1, -1):
            if nums[cur] >= end - cur:
                if nums[0] >= cur:
                    return True
                end = cur
        return False
