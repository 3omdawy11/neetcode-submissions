class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int,int>> st;
        vector<int>res;
        int index = temperatures.size() - 1;
        for (; index>=0; index--) {
            while (!st.empty() && st.top().first <= temperatures[index]) {
                st.pop();
            }
            if (st.empty()) res.push_back(0);
            else {
                res.push_back(st.top().second - index);
            }
            st.push({temperatures[index], index});

        }

        reverse(res.begin(), res.end());
        return res;
    }
};