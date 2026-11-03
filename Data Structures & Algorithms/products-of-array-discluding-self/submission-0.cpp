class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // int leftPrefix[nums.size()], rightPrefix[nums.size()];
        vector<int> leftPrefix(nums.size());
        vector<int> rightPrefix(nums.size());
        for (int i=0;i<nums.size();i++) {
            if (i == 0) {
                leftPrefix[i] = nums[i];
                continue;
            }
            leftPrefix[i] = nums[i] * leftPrefix[i-1];
        }

        for (int i=nums.size() - 1; i>=0;i--) {
            if (i == nums.size() - 1) {
                rightPrefix[i] = nums[i];
                continue;
            }
            rightPrefix[i] = nums[i] * rightPrefix[i+1];
        }

        vector<int>ans;
        for (int i=0;i<nums.size();i++) {
            int left,right;
            left = i != 0 ? leftPrefix[i-1] : 1;
            right = i != nums.size() - 1 ? rightPrefix[i + 1] : 1;
            ans.push_back(left * right);

        }
        return ans;
    }
};



