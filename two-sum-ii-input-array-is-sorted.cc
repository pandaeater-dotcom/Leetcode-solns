class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> hashmap;
        for (int i = 0; i < numbers.size(); i++) {
            if (hashmap.find(numbers[i]) != hashmap.end()) {
                return {hashmap[numbers[i]] + 1, i + 1};
            }
            hashmap[target - numbers[i]] = i;
        }
        return {};
    }
};
