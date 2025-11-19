class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        totalSum = sum(nums)

        def isFeasible(total: int) -> Tuple[bool, int]:
            index = 0
            stopsLeft = k
            localMax = 0
            cur = 0
            while index < len(nums) and stopsLeft:
                if cur + nums[index] <= total:
                    cur += nums[index]
                    index += 1
                else:
                    stopsLeft -= 1
                    localMax = max(localMax, cur)
                    cur = 0
            localMax = max(localMax, cur)
            return (index == len(nums), localMax)

        left = totalSum // k
        right = totalSum
        lowest = right
        while left <= right:
            mid = (left + right) // 2
            feasible, minSum = isFeasible(mid)
            if feasible:
                lowest = min(lowest, minSum)
                right = mid - 1
            else:
                left = mid + 1

        return lowest
