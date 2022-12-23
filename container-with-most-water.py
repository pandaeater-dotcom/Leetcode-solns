class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxStore = 0
        x = 0
        y = len(height) - 1

        while x < y:
            h = min(height[x], height[y])
            maxStore = max(maxStore, (y-x)*h)
            if height[x] < height[y]:
                x += 1
            else:
                y -= 1
        return maxStore
