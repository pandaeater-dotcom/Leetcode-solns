class Solution {
public:
  int trap(vector<int>& height) {
    int n = height.size();
    vector<int> maxLeft(n, 0);
    vector<int> maxRight(n, 0);
    int volume = 0;

    int curMax = height[0];
    for (int i = 1; i < n; ++i) {
      maxLeft[i] = curMax;
      curMax = max(curMax, height[i]);
    }
    curMax = height[n - 1];
    for (int i = n - 2; i > -1; --i) {
      maxRight[i] = curMax;
      curMax = max(curMax, height[i]);
    }

    for (int i = 0; i < n; ++i) {
      volume += max(0, min(maxLeft[i], maxRight[i]) - height[i]);
    }

    return volume;
  }
}
