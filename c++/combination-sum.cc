class Solution {
public:

  void recursiveBacktrack(const vector<int>& candidates, vector<vector<int>>& combinations, vector<int>& current, int curSum, int index, int target) {
    if (curSum > target || index == candidates.size()) {
      return;
    } else if (curSum == target) {
      combinations.push_back(current);
      return;
      // current.clear();
    }
    current.push_back(candidates[index]);
    recursiveBacktrack(candidates, combinations, current, curSum + candidates[index], index, target);
    current.pop_back();
    recursiveBacktrack(candidates, combinations, current, curSum, index + 1, target);
  }

  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> combinations;
    vector<int> current;
    recursiveBacktrack(candidates, combinations, current, 0, 0, target);

    return combinations;
  }
};
