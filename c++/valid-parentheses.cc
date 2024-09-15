class Solution {
public:
    bool isValid(string s) {
        stack<char> curParen;
        unordered_map<char, char> parens = {{'{', '}'}, {'[', ']'}, {'(', ')'}};
        
        for (const auto& c : s) {
            if (parens.contains(c)) {
                curParen.push(c);
                continue;
            }
            if (!curParen.empty() && parens[curParen.top()] == c) {
                curParen.pop();
            } else {
                return false;
            }
        }
        return curParen.empty();
    }
};
