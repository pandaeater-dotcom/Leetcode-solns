class Solution {
public:
    string minWindow(string s, string t) {
        int len = s.size();
        if (t.size() > len) return "";

        unordered_map<char, int> target;
        set<char> unique;

        for (char c : t) {
            target[c]++;
            unique.insert(c);
        }

        int left = 0;
        int right = 0;
        int matched = 0;

        int ansLeft = 0;
        int ansLen = 0;

        while (right < len && !unique.contains(s[right])) {
            right++;
        }
        if (right >= len) return "";
        left = right;

        for (; right < len; right++) {
            if (!unique.contains(s[right])) continue;
            if (--target[s[right]] == 0) matched++;

            if (s[right] == s[left]) {
                while (!unique.contains(s[left]) || target[s[left]] < 0 && left < right) {
                    if (unique.contains(s[left])) target[s[left]]++;
                    left++;
                }
            }   
            if (matched == unique.size() && !ansLen || ansLen > right - left + 1) {
                ansLen = right - left + 1;
                ansLeft = left;
            }
        }
        if (ansLen) return s.substr(ansLeft, ansLen);
        return "";
    }
};