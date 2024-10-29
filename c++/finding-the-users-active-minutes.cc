class Solution {
public:
  vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
    vector<int> freq(k);
    sort(logs.begin(), logs.end());

    if (logs.empty()) return freq;
    int curUser = logs[0][0];
    int prev = -1;
    int activeMins = 0;

    for (const auto& log : logs) {
      if (log[0] != curUser) {
        freq[activeMins - 1]++;
        activeMins = 1;
        prev = log[1];
        curUser = log[0];
        continue;
      }
      if (log[1] != prev) {
        activeMins++;
      }
      prev = log[1];
    }
    freq[activeMins - 1]++;

    return freq;
  }
};
