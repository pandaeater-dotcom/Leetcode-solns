class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // using set 
        std::unordered_set<int> num_check;
        for (auto& it : nums)
        {
            if (num_check.count(it) > 0)
                return true;
            else
                num_check.insert(it);
        }
        return false;
    }
};
