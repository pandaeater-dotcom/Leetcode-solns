class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        unsigned long left = 1;
        unsigned long right = maxSum;
        unsigned long mid, ans;
        while (left <= right) {
            mid = left + (right - left) / 2;
            
            if (check(n, index, maxSum, mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left - 1;

    }

    bool check(int n, int index, unsigned long maxSum, unsigned long maxVal) {
        unsigned long count = maxVal;
        unsigned long first = index;
        unsigned long last = (n - index - 1);

        if (maxVal > maxSum) return false;

        if (maxVal <= last) {
            count += maxVal * (maxVal - 1) / 2;
            count += last - maxVal + 1;
        } else {
            count += last * maxVal - last * (last + 1) / 2;
        }

        if (maxVal <= first) {
            count += maxVal * (maxVal - 1) / 2;
            count += first - maxVal + 1;
        } else {
            count += first * maxVal - first * (first + 1) / 2;
        }

        return count <= maxSum;
    }
};