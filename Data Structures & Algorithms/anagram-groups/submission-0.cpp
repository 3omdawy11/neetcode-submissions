class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, vector<string>> groups;
        for (string& s : strs) {
            map<char, int> freq;
            for (char c : s)
                freq[c]++;
            groups[freq].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& [_, group] : groups)
            ans.push_back(group);

        return ans;
    }
};