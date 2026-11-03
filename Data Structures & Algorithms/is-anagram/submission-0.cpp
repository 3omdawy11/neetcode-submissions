class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        map<char,int>map1;
        map<char,int>map2;

        for (int i=0;i<s.size();i++) {
            map1[s[i]]++;
            map2[t[i]]++;
        }

        if (map1.size() != map2.size()) return false;

        auto it1 = map1.begin();
        auto it2 = map2.begin();
        while (it1 != map1.end()) {
            if (it1->first != it2->first || it1->second != it2->second) return false;
            ++it1;
            ++it2;
        }
        return true;

    }
};
