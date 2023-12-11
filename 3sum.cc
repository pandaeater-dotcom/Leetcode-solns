class Solution {
    public:
        vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> triplets;
        vector<vector<int>> tripletsVector;

        sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i++)
        {
            int l = i + 1;
            int r = nums.size() - 1;
            int target = -nums.at(i);
            while (l < r)
            {
                int left = nums.at(l);
                int right = nums.at(r);
                if (left + right > target)
                    r--;
                else if (left + right < target)
                    l++;
                else
                {
                    if (triplets.insert({nums.at(i), left, right}).second)
                        tripletsVector.push_back({nums.at(i), left, right});
                    r--;
                    l++;
                }
            }
        }
        return tripletsVector;
    }
};
