class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> hashmap;
        int l = 0;
        int maxLen = 0;
        int maxFreq = 0;

        for (int r = 0; r < s.size(); r++) {
            hashmap[s[r]]++;
            maxFreq = max(maxFreq, hashmap[s[r]]);
            while (r - l + 1 - maxFreq > k) {
                hashmap[s[l]]--;
                maxFreq = max(maxFreq, hashmap[s[l]]);
                l++;
            }
            maxLen = max(maxLen, r - l + 1);            
        }
        return maxLen;
    }
};