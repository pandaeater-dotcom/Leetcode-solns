class Solution {
public:
  int minSteps(string s, string t) {
    unordered_map<char, int> hashMap;
    for (int i = 0; i < s.length(); ++i) {
      hashMap[t[i]]++;
      hashMap[s[i]]--;
    }

    int steps = 0;
    for (const auto& [k, v] : hashMap) {
      if (v < 0) continue;
      steps += v;
    }

    return steps;
  }
};
