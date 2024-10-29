class Solution {
public:
  int minElements(vector<int>& nums, int limit, int goal) {
    long total = 0;
    for (int num : nums) {
      total += num;
    }
    long diff = abs(goal - total);
    int count = diff / limit;
    if (diff % limit) count++;
    return count;
  }
};
