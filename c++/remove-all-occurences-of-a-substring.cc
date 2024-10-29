class Solution {
public:
  string removeOccurrences(string s, string part) {
    if (s.length() < part.length()) return s;
    string curString = "";

    stack<char> curStack;
    for (char c : s) {
      curStack.push(c);
      curString.push_back(c);
      if (curString.length() < part.length()) continue;
      if (curString.substr(curString.length() - part.length(), part.length()) != part) continue;
      for (int i = 0; i < part.length(); ++i) {
        curStack.pop();
        curString.pop_back();
      }
    }

    return curString;
  }
};
