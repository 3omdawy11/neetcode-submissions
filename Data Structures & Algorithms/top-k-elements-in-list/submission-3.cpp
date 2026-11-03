class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        map<int,int> freq; // number, freq;
        for (int num: nums) {
            freq[num]++;
        }
        multimap<int,int, greater<>> ans; // freq, number;
        for (auto it: freq) {
            //cout << it.second << endl;
            ans.insert({it.second, it.first});
        }

        vector<int>n;
        for (auto it = ans.begin(); it != ans.end() && k > 0; ++it, k--) {
            n.push_back(it->second);
        }

        return n;

    }
};