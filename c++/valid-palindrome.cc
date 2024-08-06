class Solution {
public:
    bool isPalindrome(string s) {
        string clean_string;
        for (const auto& chr : s) {
            if (!isalnum(chr)) continue;
            clean_string += tolower(chr);
        }

        for (int i = 0; i < clean_string.size()/2; i++) {
            if (clean_string.at(i) != clean_string.at(clean_string.size() - 1 - i)) return false;
        }

        return true;
    }
};
