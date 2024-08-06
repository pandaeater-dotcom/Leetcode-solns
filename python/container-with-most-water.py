class Solution:
    def maxArea(self, height: List[int]) -> int:
        cur, high = 0, 0
        l, r = 0, len(height) - 1
        while (l < r):
            cur = (r - l)*min(height[l], height[r])
            high = max(high, cur)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return high
