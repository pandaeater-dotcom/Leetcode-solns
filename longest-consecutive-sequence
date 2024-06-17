class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty())
            return 0;
        else if (nums.size() == 1)
            return 1;

        int maxSequence = 1;
        unordered_map<int, bool> isPresent;

        for (const auto& num : nums)
            isPresent[num] = true;
        for (const auto& num : nums)
            if (isPresent.find(num + 1) == isPresent.end() || isPresent.find(num - 1) != isPresent.end())
                isPresent[num] = false;

        for (const auto& [key, val] : isPresent)
        {
            if (!val)
                continue;
            int sequence = 0;
            int elem = key;
            while (isPresent.find(elem) != isPresent.end())
            {
                sequence++;
                elem++;
            }
            if (sequence > maxSequence)
                maxSequence = sequence;
        }
        return maxSequence;
    }
};

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();
        unordered_set<int> nums_set;

        int maxSeqCt = 1;
        for (const auto& num : nums) nums_set.insert(num);

        for (const auto& num : nums) {
            if (nums_set.find(num - 1) != nums_set.end()) continue;
            int it = num + 1;
            int seqCt = 1;
            while (nums_set.find(it) != nums_set.end()) {
                seqCt++;
                it++;
            }
            if (seqCt > maxSeqCt) maxSeqCt = seqCt;
        }
        return maxSeqCt;
    }
};
