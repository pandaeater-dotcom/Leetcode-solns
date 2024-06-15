class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num in hash.keys():
                return True
            else:
                hash[num] = 1
        return False
