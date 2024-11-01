class Solution {
public:
  int maxPoints(vector<vector<int>>& points) {
    int highest = 0;

    for (const auto& point : points) {
      unordered_map<double, int> slopes;
      for (const auto& other : points) {
        if (point[0] == other[0] && point[1] == other[1]) continue;

        double slope = INT_MIN;
        if (point[0] != other[0]) {
          slope = (double) (point[1] - other[1])/(point[0] - other[0]);
        }

        highest = max(highest, ++slopes[slope]);
      }
    }
    return highest + 1;
  }
};
