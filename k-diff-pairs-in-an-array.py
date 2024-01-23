class Solution:
    # def binarySearch(self, nums: List[int], k: int) -> int:
    #     l = 0
    #     r = len(nums) - 1

    #     while l <= r:
    #         m = (l + r)//2
    #         if k > nums[m]:
    #             l = m + 1
    #         elif k < nums[m]:
    #             r = m - 1
    #         else:
    #             return m

    #     return -1

    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        pairset = set()
        nums.sort()
        l = 0
        r = 1
        while l < r and r < len(nums):
            if nums[l] + k == nums[r]:
                pairset.add(nums[l])
                r += 1
            elif nums[l] + k < nums[r]:
                if (l == r - 1):
                    r += 1
                l += 1
            else:
                r += 1
            
        return len(pairset)
            
