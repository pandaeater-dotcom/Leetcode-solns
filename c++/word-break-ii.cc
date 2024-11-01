class Solution {
public:
  void recursiveWordBreak(vector<string>& sentences, string s, unordered_set<string>& dict, vector<string>& vecDict) {
    string cur = "";
    for (char chr : s) {
      cur.push_back(chr);
      if (!dict.contains(cur)) continue;

      if (cur == s) {
        sentences.push_back(s);
        continue;
      }

      auto inter = wordBreak(s.substr(cur.size()), vecDict);
      for (const auto& str : inter) {
        sentences.push_back(cur + " " + str);
      }
    }
  }

  vector<string> wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> dict(wordDict.begin(), wordDict.end());

    vector<string> sentences;
    recursiveWordBreak(sentences, s, dict, wordDict);
    return sentences;
  }
};
