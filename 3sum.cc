class Solution {
public:
    void mergeSort(vector<int>& A, int l, int r) {
        if (l >= r)
            return;
        int m = floor((l + r)/2);
        mergeSort(A, l, m);
        mergeSort(A, m + 1, r);
        merge(A, l, m, r);
    }
    void merge(std::vector<int>& arr, int left, int middle, int right) {
        int n1 = middle - left + 1;
        int n2 = right - middle;

        std::vector<int> leftArr(n1);
        std::vector<int> rightArr(n2);

        for (int i = 0; i < n1; ++i)
            leftArr[i] = arr[left + i];
        for (int j = 0; j < n2; ++j)
            rightArr[j] = arr[middle + 1 + j];

        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {
            if (leftArr[i] <= rightArr[j]) {
                arr[k] = leftArr[i];
                ++i;
            } else {
                arr[k] = rightArr[j];
                ++j;
            }
            ++k;
        }

        while (i < n1) {
            arr[k] = leftArr[i];
            ++i;
            ++k;
        }

        while (j < n2) {
            arr[k] = rightArr[j];
            ++j;
            ++k;
        }
    }
    vector<vector<int>> threeSum(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        set<vector<int>> triplets;
        for (int i = 0; i < nums.size(); i++)
        {
            int j = i + 1;
            int k = nums.size() - 1;
            while (j < k)
            {
                int sum = nums.at(i) + nums.at(j) + nums.at(k);
                if (sum == 0)
                {
                    triplets.insert({nums.at(i), nums.at(j), nums.at(k)});
                    j++;
                    k--;
                }
                else if (sum > 0)
                    k--;
                else if (sum < 0)
                    j++;
            }
        }
        vector<vector<int>> tripletsVector;
        for (auto it : triplets)
            tripletsVector.push_back(it);
        return tripletsVector;
    }
};
