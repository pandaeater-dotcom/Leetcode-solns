class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int maxSubstr = 0;
        set<char> usedChars;

        for (char r : s) {
            if (!usedChars.contains(r)) {
                usedChars.insert(r);
                maxSubstr = max(maxSubstr, (int) usedChars.size());
                continue;
            }
            while (usedChars.contains(r)) {
                usedChars.erase(s[l]);
                l++;
            }
            usedChars.insert(r);
        }
        return maxSubstr;
    }
};
