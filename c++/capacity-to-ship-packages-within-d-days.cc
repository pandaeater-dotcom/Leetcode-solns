class Solution {
private:
    bool canFit(vector<int>& weights, int days, int capacity) {
        int dayCount = 0;
        int curSum = 0;
        for (const auto& weight : weights) {
            if (curSum + weight > capacity) {
                curSum = 0;
                dayCount++;
            }
            curSum += weight;
        }
        dayCount++;
        return dayCount <= days;
    }
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int mn = weights[0];
        int mx = 0;
        int maxElement = weights[0];
        int minCapacity;

        for (const auto& weight : weights) {
            maxElement = max(maxElement, weight);
            mx += weight;
        }
        mn = maxElement;

        while (mn <= mx) {
            int mid = mn + (mx - mn) / 2;
            if (canFit(weights, days, mid)) {
                minCapacity = mid;
                mx = mid - 1;
            } else {
                mn  = mid + 1;
            }
        }
        return minCapacity;
    }
};