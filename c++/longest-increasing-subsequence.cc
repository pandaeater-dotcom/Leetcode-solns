class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j)
                if (nums[i] > nums[j] && dp[i] <= dp[j]) {
                    dp[i] = dp[j] + 1;
                }
        }
        return *max_element(dp.begin(), dp.end());
    }
};

class Solution {
private:
    int binSearch(const vector<int>& arr, int num) {
        int left = 0;
        int right = arr.size() - 1;
        int mid, ans;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (arr[mid] >= num) {
                right = mid - 1;
                ans = mid;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> sub;

        for (int num : nums) {
            if (sub.empty() || num > sub[sub.size() - 1]) {
                sub.push_back(num);
            } else {
                int index = binSearch(sub, num);
                sub[index] = num;
            }
        }
        return sub.size();
    }
};