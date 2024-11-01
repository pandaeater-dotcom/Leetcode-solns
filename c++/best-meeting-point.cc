class Solution {
public:
  int minTotalDistance(vector<vector<int>>& grid) {
    vector<int> row;
    vector<int> col;
    pair<int, int> meetingPoint;
    for (int i = 0; i < grid.size(); ++i) {
      for (int j = 0; j < grid[0].size(); ++j) {
        if (!grid[i][j]) continue;
        row.push_back(i);
        col.push_back(j);
      }
    }

    int i = 0; int j = row.size() - 1;
    int total = 0;
    sort(row.begin(), row.end());
    sort(col.begin(), col.end());

    while (i < j) {
      total += row[j] - row[i] + col[j] - col[i];
      i++;
      j--;
    }

    return total; 
  }
};
