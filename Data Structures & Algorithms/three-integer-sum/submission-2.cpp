class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        map<vector<int>, int>m;
        vector<vector<int>>ans;

        for (int i=0;i<nums.size();i++) {
            int l = i+1;
            int r = nums.size() - 1;
            while (l < r) {
                if (nums[i] + nums[l] + nums[r] == 0) {
                    m[{nums[i], nums[l], nums[r]}] = 0;
                    l++;
                }
                else if (nums[i] + nums[l] + nums[r] > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }

        for (auto it : m) {
            ans.push_back({it.first[0], it.first[1], it.first[2]});
        }
        return ans;
    }
};
