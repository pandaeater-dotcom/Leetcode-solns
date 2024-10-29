class Solution {
public:
  int kthSmallest(vector<vector<int>>& matrix, int k) {
    int n = matrix.size();
    struct Compare{
      bool operator()(tuple<int, int, int>& a, tuple<int, int, int>& b) {
        return get<0>(a) > get<0>(b);
      }
    };
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, Compare> minHeap;
    for (int i = 0; i < n; ++i) {
      minHeap.push({matrix[i][0], i, 0});
    }

    int counter = 0;
    int elem = 0;
    while (counter < k) {
      auto [value, i, j] = minHeap.top();
      elem = value;
      if (j + 1 < n) {
        minHeap.push({matrix[i][j + 1], i, j + 1});
      }
      minHeap.pop();
      counter++;
    }
    return elem;
  }
};
