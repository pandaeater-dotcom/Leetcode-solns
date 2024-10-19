class Solution {
private:
  bool checkAttack(const vector<pair<int, int>>& cur, int i, int j) {
    for (const auto& queen : cur) {
      if (queen.first == i || queen.second == j) return true;
      if (abs(queen.first - i) == abs(queen.second - j)) return true;
    }
    return false;
  }
  void recursiveQueens(vector<vector<string>>& solns, vector<string>& queens, vector<pair<int, int>>& cur, int row, int n) {
    if (queens.size() == n) {
      solns.push_back(queens);
      return;
    }
    if (row >= n) {
      return;
    }

    string queen = "";

    for (int col = 0; col < n; ++col) {
      if (checkAttack(cur, row, col)) {
        queen += ".";
        continue;
      }
      queen += "Q";
      for (int i = queen.length(); i < n; ++i) {
        queen += ".";
      }
      queens.push_back(queen);
      cur.push_back({row, col});
      recursiveQueens(solns, queens, cur, row + 1, n);
      queens.pop_back();
      cur.pop_back();
      for (int i = col; i < n; ++i) {
        queen.pop_back();
      }
      queen += ".";
    }
  }
public:
  vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> solns;
    vector<string> queens;
    vector<pair<int, int>> cur;

    recursiveQueens(solns, queens, cur, 0, n);
    return solns;
  }
};
