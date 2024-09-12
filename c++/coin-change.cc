class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (!amount) return 0;
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;

        for (int am = 1; am <= amount; am += 1) {
            for (int coin : coins) {
                if (am < coin) continue;
                dp[am] = min(dp[am], dp[am - coin] + 1);
            }
        }
        return dp[amount] != amount + 1 ? dp[amount] : -1;
    }
};
