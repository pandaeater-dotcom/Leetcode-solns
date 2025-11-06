class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [0] * (amount + 1)
        cache[0] = 1
        for index in range(len(coins) - 1, -1, -1):
            for value in range(coins[index], amount + 1):
                cache[value] += cache[value - coins[index]]

        return cache[amount]
