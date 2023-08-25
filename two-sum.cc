class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashTable;
        for (int i = 0; i < nums.size(); i++)
        {
            if (hashTable.find(nums.at(i)) == hashTable.end())
                hashTable[target - nums.at(i)] = i;
            else
                return {i, hashTable[nums.at(i)]};
        }
        return {0, 0};
    }
};
