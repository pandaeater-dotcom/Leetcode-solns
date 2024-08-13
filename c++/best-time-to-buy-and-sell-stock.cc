class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int buy = prices[0];

        for (int price : prices) {
            if (price < buy) {
                buy = price;
            } else {
                maxProfit = max(maxProfit, price - buy);
            }
        }
        return maxProfit;
    }
};