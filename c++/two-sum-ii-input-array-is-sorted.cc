class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        while (l < r)
        {
            if (numbers.at(l) + numbers.at(r) > target)
                r--;
            else if (numbers.at(l) + numbers.at(r) < target)
                l++;
            else
                return {l + 1, r + 1};
        }
        return {0};
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> hashmap;
        for (int i = 0; i < numbers.size(); i++) {
            auto it = hashmap.find(numbers[i]);
            if (it != hashmap.end()) {
                return {it->second + 1, i + 1};
            }
            hashmap[target - numbers[i]] = i;
        }
        return {};
    }
};
