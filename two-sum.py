class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for x in range(len(nums)):
            val = nums[x]
            if target - val in hashTable:
                return [nums.index(target - val), x]
            if val not in hashTable:
                hashTable[val] = target - val
