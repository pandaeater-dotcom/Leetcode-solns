class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerBound = 1
        upperBound = max(piles)
        minViableRate = upperBound

        def bananaCheck(rate) -> bool:
            minHours = 0
            for pile in piles:
                minHours += ceil(pile / rate)
            return minHours <= h

        while lowerBound <= upperBound:
            curRate = lowerBound + (upperBound - lowerBound) // 2
            canFinish = bananaCheck(curRate)
            if not canFinish:
                lowerBound = curRate + 1
            else:
                minViableRate = curRate
                upperBound = curRate - 1

        return minViableRate
