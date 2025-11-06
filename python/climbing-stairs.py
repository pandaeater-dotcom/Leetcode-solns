class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)
        cache[0] = 1
        for i in range(1, n + 1):
            if i > 0:
                cache[i] += cache[i - 1]
            if i > 1:
                cache[i] += cache[i - 2]

        return cache[-1]
