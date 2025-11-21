class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        deficit = 0
        bottleneck = -1
        tank = 0

        for i in range(n):
            diff = gas[i] - cost[i]
            if tank + diff >= 0:
                tank += diff
            else:
                bottleneck = i
                deficit += diff + tank
                tank = 0
        if bottleneck == -1:
            return 0
        return -1 if tank + deficit < 0 else bottleneck + 1
