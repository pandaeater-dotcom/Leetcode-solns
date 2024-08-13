class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()) return false;
        
        map<char, int> firstTable;
        map<char, int> curTable;

        int len = s1.size();

        for (char c : s1) firstTable[c]++;
        for (char c : s2.substr(0, len)) curTable[c]++;

        for (const auto& [key, value]: firstTable) {
            curTable[key] -= value;
            if (!curTable[key]) curTable.erase(key);
        }

        if (curTable.empty()) return true;
        else if (s2.size() == s1.size()) return false;

        for (int i = len; i < s2.size(); i++) {
            curTable[s2[i]]++;
            if (!curTable[s2[i]]) curTable.erase(s2[i]);
            curTable[s2[i - len]]--;
            if (!curTable[s2[i - len]]) curTable.erase(s2[i - len]);
            if (curTable.empty()) return true;
        }
        return false;
    }
};