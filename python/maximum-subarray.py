class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for num in nums[1:]:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)

        return maxSum
