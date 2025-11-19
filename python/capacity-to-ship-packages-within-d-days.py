class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        left = total // days
        right = total
        lowest = right

        def canShip(capacity: int):
            daysLeft = days
            index = 0
            while daysLeft and index < len(weights):
                cur = 0
                while cur <= capacity and index < len(weights):
                    if cur + weights[index] <= capacity:
                        cur += weights[index]
                        index += 1
                    else:
                        break
                daysLeft -= 1
            return index == len(weights)

        while left <= right:
            mid = (left + right) // 2
            possible = canShip(mid)
            if possible:
                lowest = min(mid, lowest)
                right = mid - 1
            else:
                left = mid + 1
        return lowest
