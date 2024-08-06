class Solution:
    def robHelper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        r1, r2 = 0, 0
        for num in nums:
            r1, r2 = r2, max(r1 + num, r2)
        return r2
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
