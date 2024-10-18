class Solution {
private:
    void recursiveCombinations(vector<int>& candidates,
                               vector<vector<int>>& combinations,
                               vector<int>& cur, int curSum, int index,
                               int target) {
        if (curSum > target) {
            return;
        } else if (curSum == target) {
            combinations.push_back(cur);
        }
        if (index == candidates.size())
            return;

        cur.push_back(candidates[index]);
        recursiveCombinations(candidates, combinations, cur,
                              curSum + candidates[index], index + 1, target);
        cur.pop_back();
        while (index < candidates.size() - 1 &&
               candidates[index] == candidates[index + 1]) {
            index++;
        }
        recursiveCombinations(candidates, combinations, cur, curSum, index + 1,
                              target);
    }

public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> combinations;
        vector<int> cur;

        vector<vector<int>> uniqueCombinations;
        recursiveCombinations(candidates, combinations, cur, 0, 0, target);
        if (combinations.empty())
            return {};

        sort(combinations.begin(), combinations.end());
        uniqueCombinations.push_back(combinations[0]);

        for (int i = 1; i < combinations.size(); ++i) {
            if (uniqueCombinations.back() == combinations[i])
                continue;
            uniqueCombinations.push_back(combinations[i]);
        }

        return uniqueCombinations;
    }
};
