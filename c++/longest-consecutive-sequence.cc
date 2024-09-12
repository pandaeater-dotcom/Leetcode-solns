class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();
        unordered_set<int> nums_set;

        int maxSeqCt = 1;
        for (const auto& num : nums) nums_set.insert(num);

        for (const auto& num : nums_set) {
            if (nums_set.contains(num - 1)) continue;
            int seqCt = 1;
            while (nums_set.contains(num + seqCt)) {
                seqCt++;
            }
            maxSeqCt = max(seqCt, maxSeqCt);
        }
        return maxSeqCt;
    }
};
