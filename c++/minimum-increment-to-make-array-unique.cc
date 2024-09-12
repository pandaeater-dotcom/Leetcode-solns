class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int counter = 0;
        int curLargest = -1;

        for (int num : nums) {
            if (num > curLargest) {
                curLargest = num;
            } else {
                counter += curLargest - num + 1;
                curLargest++;
            }
        }

        return counter;
    }
};