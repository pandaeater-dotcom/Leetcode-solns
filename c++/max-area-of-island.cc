class Solution {
private:
  int scourIsland(vector<vector<int>>& grid, int i, int j) {
    int area = 0;
    queue<pair<int, int>> bfsq;
    bfsq.push({i, j});
    while (!bfsq.empty()) {
      auto coord = bfsq.front();
      bfsq.pop();
      if (!grid[coord.first][coord.second]) continue;

      area++;
      grid[coord.first][coord.second] = 0;

      if (coord.first > 0 && grid[coord.first - 1][coord.second]) {
        bfsq.push({coord.first - 1, coord.second});
      }
      if (coord.first < grid.size() - 1 && grid[coord.first + 1][coord.second]) {
        bfsq.push({coord.first + 1, coord.second});
      }
      if (coord.second  > 0 && grid[coord.first][coord.second  - 1]) {
        bfsq.push({coord.first, coord.second  - 1});
      }
      if (coord.second  < grid[0].size() - 1 && grid[coord.first][coord.second  + 1]) {
        bfsq.push({coord.first, coord.second  + 1});
      }
    }

    return area;
  }
public:
  int maxAreaOfIsland(vector<vector<int>>& grid) {
    int maxArea = 0;

    for (int i = 0; i < grid.size(); ++i) {
      for (int j = 0; j < grid[0].size(); ++j) {
        if (!grid[i][j]) continue;
        maxArea = max(maxArea, scourIsland(grid, i, j));
      }
    }

    return maxArea;  
  }
}
