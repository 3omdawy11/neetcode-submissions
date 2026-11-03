class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int,int>counter;
        for (int i=0;i<nums.size();i++) {
            counter[nums[i]]++;
            //cout << nums[i] << " " << counter[nums[i]] << endl;
            if (counter[nums[i]] > 1) return true;
        }
        return false;
    }
};