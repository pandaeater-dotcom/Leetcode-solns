class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() <= 1)
            return s.length();

        int maxLen = 1, curLen = 1;
        int l = 0, r = l + 1;
        unordered_set<int> substr = {s.at(l)};
        while (l <= r && r < s.length())
        {
            if (substr.insert(s.at(r)).second == false)
            {
                substr.erase(s.at(l));
                l++;
                curLen--;
            }
            else
            {
                curLen++;
                r++;
                maxLen = max(maxLen, curLen);
            }
        }
        return maxLen;
    }
};
