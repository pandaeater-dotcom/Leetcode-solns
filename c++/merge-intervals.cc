class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> mergedIntervals;
        mergedIntervals.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i) {
            auto& lastElem = mergedIntervals[mergedIntervals.size() - 1];
            if (intervals[i][0] <= lastElem[1]) {
                lastElem[1] = max(intervals[i][1], lastElem[1]);
            } else {
                mergedIntervals.push_back(intervals[i]);
            }
        }
        return mergedIntervals;
    }
};