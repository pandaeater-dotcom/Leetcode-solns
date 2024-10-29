class Solution {
public:
  bool exploreIsland(vector<vector<int>>& grid1, vector<vector<int>>& grid2, pair<int, int> pos) {
    grid2[pos.first][pos.second] = 0;
    array<bool, 5> checks;
    checks.fill(true);
    if (!grid1[pos.first][pos.second]) checks[0] = false;
    if (pos.first > 0 && grid2[pos.first - 1][pos.second]) {
      if (!exploreIsland(grid1, grid2, {pos.first - 1, pos.second})) checks[1] = false;
    }
    if (pos.first + 1 < grid2.size() && grid2[pos.first + 1][pos.second]) {
      if (!exploreIsland(grid1, grid2, {pos.first + 1, pos.second})) checks[2] = false;
    }
    if (pos.second > 0 && grid2[pos.first][pos.second - 1]) {
      if (!exploreIsland(grid1, grid2, {pos.first, pos.second - 1})) checks[3] = false;
    }
    if (pos.second + 1 < grid2[0].size() && grid2[pos.first][pos.second + 1]) {
      if (!exploreIsland(grid1, grid2, {pos.first, pos.second + 1})) checks[4] = false;
    }
    for (bool check : checks) {
      if (!check) return false;
    }
    return true;
  }
  int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
    int counter = 0;
    for (int i = 0; i < grid2.size(); ++i) {
      for (int j = 0; j < grid2[0].size(); ++j) {
        if (!grid2[i][j]) continue;
        if (exploreIsland(grid1, grid2, {i, j})) counter++;
      }
    }
    return counter;
  }
};
