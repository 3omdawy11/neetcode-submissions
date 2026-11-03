class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int>map1;
        for (int i=0;i<nums.size();i++) {
            map1[nums[i]] = i+1;
        }
        for (int i=0;i<nums.size();i++) {
            if (map1[target-nums[i]] - 1 == i) continue;
            if(map1[target-nums[i]]) return {i, map1[target-nums[i]] - 1};
        }
    }
};
