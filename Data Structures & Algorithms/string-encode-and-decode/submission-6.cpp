class Solution {
public:
    string encode(vector<string>& strs) {
        string s = "";
        for (string str : strs) {
            s += std::to_string(str.size()) + "#" + str;
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        int i=0;
        while (i < s.size()) {
            int j=i;
            while (s[j] != '#') j++;
            int length = stoi(s.substr(i,j-i));
            ans.push_back(s.substr(j+1, length));
            i = j + 1 + length;
        }
        return ans;
    }
};