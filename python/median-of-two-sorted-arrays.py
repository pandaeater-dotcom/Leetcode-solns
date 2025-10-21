class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            smallMid = (left + right) // 2
            largeMid = (m + n + 1) // 2 - smallMid

            maxSmallLeft = nums1[smallMid - 1] if smallMid > 0 else float('-inf')
            maxLargeLeft = nums2[largeMid - 1] if largeMid > 0 else float('-inf')

            minSmallRight = nums1[smallMid] if smallMid < m else float('inf')
            minLargeRight = nums2[largeMid] if largeMid < n else float('inf')

            if maxSmallLeft <= minLargeRight and maxLargeLeft <= minSmallRight:
                if (m + n) % 2 == 0:
                    return (max(maxSmallLeft, maxLargeLeft) + min(minSmallRight, minLargeRight)) / 2
                return max(maxSmallLeft, maxLargeLeft)
            elif maxSmallLeft > minLargeRight:
                right = smallMid - 1
            else:
                left = smallMid + 1
