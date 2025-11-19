class Solution:
    def findLargerIndex(self, nums: List[List[int]], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid][1] > target:
                right = mid - 1
            elif nums[mid][1] < target:
                left = mid + 1
            else:
                return mid
        return left

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        innerSeq = []
        for envelope in envelopes:
            index = self.findLargerIndex(innerSeq, envelope[1])
            if index >= len(innerSeq):
                innerSeq.append(envelope)
            else:
                innerSeq[index] = envelope
        return len(innerSeq)
