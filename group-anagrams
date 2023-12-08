class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> anagramGroups;
        std::unordered_map<std::string, std::vector<std::string>> sorted_anagrams;
        for (const auto& str : strs)
        {
            std::string sorted_str = str;
            sort(sorted_str.begin(), sorted_str.end());
            sorted_anagrams[sorted_str].push_back(str);
        }
        for (const auto& [key, val] : sorted_anagrams)
        {
            anagramGroups.push_back(val);
        }
        return anagramGroups;
    }                                                                                                       
};
