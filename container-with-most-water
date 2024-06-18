class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int maxVol = (r - l) * min(height[l], height[r]);
        while (l < r) {
            if (height[l] < height[r]) l++;
            else r--;
            int vol = (r - l) * min(height[l], height[r]);
            if (vol > maxVol) maxVol = vol;
        }

        return maxVol;
    }
};
