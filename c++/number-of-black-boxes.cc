class Solution {
public:
  vector<long long> countBlackBlocks(int m, int n, vector<vector<int>>& coordinates) {
    vector<long long> freq(5);
    map<pair<int, int>, int> hashMap;

    for (const auto& coord: coordinates) {
      int i = coord[0]; int j = coord[1];
      if (i < m - 1 && j < n - 1) hashMap[{i, j}]++;
      if (i > 0 && j < n - 1) hashMap[{i - 1, j}]++;
      if (i < m - 1 && j > 0) hashMap[{i, j - 1}]++;
      if (i > 0 && j > 0) hashMap[{i - 1, j - 1}]++;
    }

    for (const auto& [k, v] : hashMap) {
      freq[v]++;
    }
    freq[0] = (long long)(m - 1)*(long long)(n - 1) - hashMap.size();

    return freq;
  }
};
