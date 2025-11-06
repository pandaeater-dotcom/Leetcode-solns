class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        kCount = 0
        curSum = 0

        for num in nums:
            curSum += num
            req = curSum - k
            kCount += prefixSum[req]
            prefixSum[curSum] += 1

        return kCount
