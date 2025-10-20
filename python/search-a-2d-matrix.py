class Solution:        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def numToPos(num):
            y = num // n
            x = num % n
            return (x, y)

        left = 0
        right = m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            midX, midY = numToPos(mid)
            value = matrix[midY][midX]
            print(mid, midY, midX, value)

            if value > target:
                right = mid - 1
            elif value < target:
                left = mid + 1
            else:
                return True

        return False
