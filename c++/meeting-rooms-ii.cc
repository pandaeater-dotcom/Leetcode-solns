class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        int reqRooms = 0;

        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        for (const auto interval: intervals) {
            cout << interval[0] << " " << interval[1] << endl;
            while (!minHeap.empty() && minHeap.top() <= interval[0]) {
                minHeap.pop();
            }

            minHeap.push(interval[1]);
            reqRooms = max(reqRooms, (int) minHeap.size());
        }

        return reqRooms;
    }
};