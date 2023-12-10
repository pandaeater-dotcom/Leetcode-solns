class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        bool hasZero = false;
        int zeroIndex;
        vector<int> exceptSelf;
        vector<int> answer(nums.size(), 0);

        for (int i = 0; i < nums.size(); i++)
        {
            if (nums.at(i) == 0 && !hasZero)
            {
                zeroIndex = i;
                hasZero = true;
            }
            else if (nums.at(i) == 0 && hasZero)
                return answer;
            else
                product *= nums.at(i);
        }
        if (hasZero)
        {
            answer.at(zeroIndex) = product;
            return answer;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            answer.at(i) = product / nums.at(i);
        }
        return answer;
    }
};
