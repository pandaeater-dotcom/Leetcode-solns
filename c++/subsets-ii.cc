class Solution {
private:
  void recursiveSubset(vector<int>& nums, vector<vector<int>>& combinations, vector<int>& cur, int index) {
    combinations.push_back(cur);
    for (int i = index; i < nums.size(); ++i) {
      cur.push_back(nums[i]);
      recursiveSubset(nums, combinations, cur, i + 1);
      cur.pop_back();
    }
  }
public:
  vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> combinations;
    vector<int> cur;

    recursiveSubset(nums, combinations, cur, 0);
    sort(combinations.begin(), combinations.end());

    vector<vector<int>> uniqueCombinations;
    uniqueCombinations.push_back(combinations[0]);

    for (int i = 1; i < combinations.size(); ++i) {
      if (uniqueCombinations.back() == combinations[i]) continue;
      uniqueCombinations.push_back(combinations[i]);
    }

    return uniqueCombinations;
  }
};
