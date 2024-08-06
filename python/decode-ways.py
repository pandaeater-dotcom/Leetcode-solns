class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp [1] = 1 if s and s[0] != "0" else 0

        for i in range(1, len(s)):
            cur = int(s[i])
            pair = int(s[i-1:i+1])
            if cur > 0:
                dp[i + 1] += dp[i]
            if pair > 9 and pair < 27:
                dp[i + 1] += dp[i - 1]
        print(dp)
        return dp[-1]
