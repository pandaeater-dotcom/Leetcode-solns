class Solution {
public:
    int minSwaps(vector<int>& data) {
        int numOnes = 0;
        for (int num : data) {
            if (!num) continue;
            numOnes++;
        }
        if (!numOnes) return 0;


        int left = 0;
        int curOnes = 0;
        for (int i = 0; i < numOnes - 1; ++i) {
            if (!data[i]) continue;
            curOnes++;
        }

        int numSwaps = numOnes;

        for (; left + numOnes <= data.size(); ++left) {
            if (data[left + numOnes - 1]) curOnes++;
            numSwaps = min(numSwaps, numOnes - curOnes);
            if (data[left]) curOnes--;
        }
        return numSwaps;
    }
};