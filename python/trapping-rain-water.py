class Solution:
    def trap(self, height: List[int]) -> int:
        prevHighest = 0
        prevLeft = len(height)
        prevRight = -1
        rainVolume = 0

        left = 0
        right = len(height) - 1
        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]
            curHeight = min(leftHeight, rightHeight)
            if prevLeft < left:
                rainVolume -= min(leftHeight, prevHighest)
                prevLeft = left
            if prevRight > right:
                rainVolume -= min(rightHeight, prevHighest)
                prevRight = right
            if curHeight > prevHighest:
                rainVolume += (curHeight - prevHighest) * (right - left - 1)
                prevHighest = curHeight
                prevLeft = left
                prevRight = right
            if leftHeight <= rightHeight:
                left += 1
            else:
                right -= 1

        return rainVolume
