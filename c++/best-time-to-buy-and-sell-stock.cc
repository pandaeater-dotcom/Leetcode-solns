class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 1) return 0;
        int lowest = prices.at(0);
        int maxProfit = 0, curProfit = 0;
        for (int price : prices)
        {
            if (price < lowest)
                lowest = price;
            curProfit = price - lowest;
            if (curProfit > maxProfit)
                maxProfit = curProfit;
        }
        return maxProfit;
    }
};
