class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        visited = set(nums)

        for num in visited:
            if num - 1 in visited:
                continue

            length = 1
            while num + length in visited:
                length += 1

            longest = max(longest, length)

        return longest
