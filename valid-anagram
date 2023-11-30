class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
        std::unordered_map<char, int> hashTable;
        for (int i = 0; i < s.length(); i++)
        {
            hashTable[s.at(i)]++;
            hashTable[t.at(i)]--;
        }
        for (const auto& [key, val] : hashTable)
        {
            if (val != 0)
                return false;
        }
        return true;
    }
};
